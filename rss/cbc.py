import json
import datetime
import urllib.request
import xml.etree.ElementTree as etree


def write_to_db(stories):
    # here we will write the stories to some database format
# end def write_to_db


def read_rss_feed(rss_feed):
    """
    """

    read_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    stories = []
    ids = []

    result = urllib.request.urlopen(rss_feed['url'])
    xml_data = result.read().decode(result.headers.get_content_charset())
    rss_data = etree.fromstring(xml_data)

    for child in root[0].findall('item'):
        id = child.find('guid')
        title = child.find('title')
        link = child.find('link')
        publish_date = child.find('pubDate')
        author = child.find('author')
        category = child.find('category')

        if id.text not in ids:
            ids.append(id.text)
            stories.append([id.text, title.text, link.text, publish_date.text, author.text, category.text])

    print(len(ids), "novel news reports found.")

    return True
# end def read_rss_feed


def open_feed_file(json_file="feeds/cbc.json"):
    """
    This function will open the CBC rss feeds listed in the specified JSON file.

    json_file: String
        The path to the JSON file to be loaded and read for RSS feeds.

    return: Boolean
        System will return True value upon successful run.

    """

    # Open JSON file and parse into JSON object
    json_data = json.load(open(json_file))

    # Loop through all RSS feeds and send to reader function
    for rss_feed in json_data['feeds']:
        read_rss_feed(rss_feed)
        print "All " + rss_feed['category'] + " stories pulled from " + rss_feed['source']

    return True
# end def open_feed_file


if __name__ == '__main__':
    open_feed_file("feeds/cbc.json")
