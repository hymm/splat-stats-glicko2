import formatter
import html.parser
import os
import urllib.robotparser
import socket
import string
import _thread
import threading
import urllib.request, urllib.parse, urllib.error
import urllib.parse

#
# Class to wrap up a URL nicely and make it easy to deal with
#
class URL:
    """Internal representation of a URL.  Provides functions for
testing the URL to see if it is appropriate for Web crawling, and for
retrieving the name of the Web site pointed to by the URL."""

    #
    # Dictionary of all sites that have already had their robots.txt
    # files fetched.  Each entry in the dictionary is a robotparser.
    #
    __robotDictionary = {}

    def __init__(self, url):
        """Construct a URL instance by splitting a provided string into
its components."""
        #
        # All the work is done by urlparse, which has a clumsy return
        # syntax but is pretty powerful.
        #
        [self.__scheme, self.__site, self.__path, self.__parameters, \
          self.__query, self.__fragment] = \
            urllib.parse.urlparse(url)

    def __repr__(self):
        """Generate a printable representation of a URL"""
        return urllib.parse.urlunparse([self.__scheme, self.__site, self.__path, \
          self.__parameters, self.__query, self.__fragment])

    def isSimpleURL(self):
        """Return True if the represented URL is simple (i.e., no query)"""
        return self.__parameters == ''  and  self.__query == ''

    def isCrawlable(self):
        """Return True if the represented URL is simple enough to be
followed by a Web crawler.  Note that isCrawlable does NOT check
robots.txt."""
        if self.__scheme != 'http':
            return False
        #
        # Huge hack to check whether the host is allowed.  We
        # accept hosts inside Claremont and on gutenberg.org.
        #
        try:
            ip = socket.gethostbyname(self.__site)
        except socket.gaierror:
            return False        # No such IP => not crawlable
        if len(ip) < 8:
            return False
        # if not ip[0:8] == '134.173.'  and  not ip == '152.46.7.81':
        #     return False
        return self.isSimpleURL()

    class __neverFetch:
        """Class to substitute for a robot when fetching robots.txt fails.
In this case, the class always informs users that files cannot be fetched."""
        def __init__(self):
            pass

        @staticmethod
        def can_fetch(userAgent, url):
            return False

    def isForbidden(self):
        """Return True if the represented URL is forbidden by the site's
robots.txt file."""
        if self.__site not in self.__robotDictionary:
            robotRules = urllib.robotparser.RobotFileParser()
            robotRules.set_url('http://' + self.__site + '/robots.txt')
            try:
                robotRules.read()
            except IOError:
                robotRules = self.__neverFetch()
                print("Can never fetch from", self.__site, "(URL", str(self) + ")")
            self.__robotDictionary[self.__site] = robotRules
        return not self.__robotDictionary[self.__site].can_fetch('*',
          str(self))

    def scheme(self):
        """Return scheme used by the URL."""
        return self.__scheme

    def site(self):
        """Return the Web site represented by the URL.  Note that the
site name is not canonicalized, so it is possible for apparently
different URLs to refer to the same site."""
        return self.__site

    def path(self):
        """Return the path represented by the URL."""
        return self.__path

class WebPage(html.parser.HTMLParser):
    """Class used to hold a (parsed) Web page.  Fetches the page from the
server, parses it, and makes its elements available to users."""

    MAX_URL_WAIT_TIME = 15.0

    @staticmethod
    def __timeoutHandler():
        """Raise a KeyboardInterrupt in the main thread in case an operation
           times out"""
        _thread.interrupt_main()

    def __init__(self, url):
        """Read and parse a Web page found at the given URL.  The URL must
           be a member of the URL class."""
        self.__url = url
        self.__anchorlist = []
        self.__text = ''
        if not self.__url.isCrawlable() or  self.__url.isForbidden():
            raise Exception("Attempt to fetch non-crawlable page")
        html.parser.HTMLParser.__init__(self, formatter.NullFormatter())
        self.__rawContents = ''
        timeout = \
          threading.Timer(self.MAX_URL_WAIT_TIME, self.__timeoutHandler)
        try:
            timeout.start()
            urlFile = urllib.request.urlopen(str(url))
            self.__rawContents = urlFile.read().decode()
        except (IOError, KeyboardInterrupt):
            pass
        try:
            urlFile.close()
        except (IOError, KeyboardInterrupt, UnboundLocalError):
            pass
        finally:
            timeout.cancel()
        #
        # Now it's time to parse the page contents
        #
        try:
            self.feed(self.__rawContents)
        except html.parser.HTMLParseError:
            pass                # We simply ignore HTML errors
        del self.__rawContents

    def anchor_bgn(
            self,
            href,               # HREF field of the anchor
            name,               # NAME field of the anchor
            type):              # TYPE field of the anchor
        """Process an anchor (<A>) tag.  The tag is converted to
absolute format, then checked to see if it is an HTTP reference.  If
so, it is saved in the list of unique links; otherwise it is silently
discarded.

NOTE: This function is for internal use.  It should not be called
externally."""
        if href == '':
            return
        href = self.__canonicalizeURL(href)
        if href != '':
            self.__anchorlist += [href]

    def handle_starttag(self, tag, attrs):
        if tag == 'a' or tag == 'A':
            for attr in attrs:
                if attr[0].lower() == 'href':
                    self.__anchorlist += [attr[1]]
        

    def handle_endtag(self, tag):
        return

    def handle_data(
            self,
            data):              # Data to be dealt with
        """Handle data within a Web page.  The data is just saved for later
use.

NOTE: This function is for internal use.  It should not be called
externally."""
        self.__text += data

    def urls(self):
        """Return the URLs referenced by the Web page."""
        return self.__anchorlist

    def text(self):
        """Return the text contained within a Web page."""
        return self.__text

    #
    # Make a URL absolute, and canonicalize it for further searching.
    #
    def __canonicalizeURL(
            self,
            URL):               # URL to convert
        """Canonicalize a URL by making it absolute and discarding
the fragment."""
        (scheme, location, path, parameters, query, fragment) = \
          urllib.parse.urlparse(URL)
        if scheme == '':
            scheme = self.__url.scheme()
        if scheme != 'http':
            return URL          # Non-HTTP URLs are left unchanged
        if location == ''  and  path == '':
            return ''           # Turn fragment-only URLs into nothing
        fragment = ''
        if location != ''  or  path == '':
            #
            # The URL is absolute.  Just return it.
            #
            return urllib.parse.urlunparse((scheme, location, path, parameters,
              query, fragment))
            #
            if location == '':
                location = self.__url.site()
            if path[0] == '/':
                #
                # The URL is a reference to the top directory on the
                # current site.  Rebuild it without the leading slash.
                #
                return urllib.parse.urlunparse(
                  (scheme, location, path[1:], parameters, query, fragment))
            else:
                #
                # The URL is relative.  Add the base directory of the URL.
                #
                baseDir = self.__url.path()
                if baseDir == '':
                    baseDir = '/'
                elif baseDir[-1] != '/':
                    #
                    # The base directory is the path, stripped of its
                    # last component.
                    #
                    lastSlash = string.rfind(baseDir, '/')
                    if lastSlash > 0:
                        #
                        # Strip the last component from the path,
                        # leaving the slash.
                        #
                        baseDir = baseDir[0:string.rindex(baseDir, '/') + 1]
                    else:
                        #
                        # There is no last component.  The base
                        # directory is just "/".
                        #
                        baseDir = '/'
                return urllib.parse.urlunparse((scheme, location,
                  os.path.normpath(baseDir + path), parameters,
                  query, fragment))

#
# Global function to get HTML information in a form convenient for CS5
# projects.
#
def getHTML(url):
    """
    Takes a url string as input and returns a 2-tuple (TEXT, URLS)
    where TEXT is a string containing the text on the web page
    referred to by the given url and URLS is a list of the urls
    appearing on that web page.  The text is returned all in lowercase.
    """
    urlObject = URL(url)
    if not urlObject.isCrawlable()  or  urlObject.isForbidden():
        return ('', [])
    page = WebPage(urlObject)
    return (page.text(), page.urls())


#print(getHTML("http://tlab-login.cs.northwestern.edu/~ict992/page1.html"))
