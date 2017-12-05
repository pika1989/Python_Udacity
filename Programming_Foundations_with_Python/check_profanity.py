"""Checks text to profanity."""

import urllib


def read_text(file):
    """Reads data from file.
    
    :Parameters:
        - file: str, file's name

    :Return:
        - file's data as string
    """
    with open(file) as quotes:
        return quotes.read()


def check_profanity(text_to_check):
    """Checks text to profanity by using a special site.
    
    :Parameters:
        - text_to_check: str, text for checking
    """
    url_with_query = 'http://www.wdylike.appspot.com/?q=%s' % (text_to_check)
    connection =  urllib.urlopen(url_with_query)
    response = connection.read()
    connection.close()

    if 'true' in response:
        print 'Profanity Alert!!'
    elif 'false' in response:
        print 'This document has no curse words!'
    else:
        print 'Could not scan the document properly.'


def main():
    file_path = 'movie_quotes.txt'
    contents_of_file = read_text(file_path)
    check_profanity(contents_of_file)


if __name__ == '__main__':
    main()
