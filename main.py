from os.path import basename
import pandas

from articles.newsAPIdata4good import get_newsapi_articles, OUTPUT_FILENAME
from clustering.clustering_news import newsjsontocsv, datacsv
from fact_checking.source.fact_checking import fact_check


## NewsAPI > tunis.json + tunis.csv
def newsapi():
    get_newsapi_articles()

    newsapi_csv_name = basename(OUTPUT_FILENAME).split('.')[0] + ".csv"
    newsjsontocsv(OUTPUT_FILENAME, newsapi_csv_name)

    # newsapi_dataframe = pandas.read_csv(newsapi_csv_name, encoding="utf8")
    # csv_line_index_start = 5
    # csv_line_index_end = 6
    # one line: newsapi_dataframe[csv_line_index_start:csv_line_index_end])
    # one column, 'content': newsapi_dataframe.content
    # one cell: newsapi_dataframe.content[csv_line_index_start:csv_line_index_end]


# NewsAPI clustering > out-clusteringVocabALL.txt + out-articlesClusters.csv
#                    > out-wc_Title_X.png + out-wc_Content_X.png 
def newsapi_clustering():
    datacsv(newsapi_csv_name)


## MosaïqueFM > mosaique.csv
def mosaique_fm():
    import articles.mosaique_fm

MOSAIQUE_OUTPUT_PATH = './mosaique.csv'

# fact checking
def fact_checking():
    mosaique_dataframe = pandas.read_csv(MOSAIQUE_OUTPUT_PATH, encoding="utf8")

    article = mosaique_dataframe[2:3].Article.values[0]
    list_facts = [
        ('personnalité', 'Zied Lakhdar'), 
        ('élection', 'circonscription'),
        ("budget","dette")]
    return fact_check(article, list_facts)


# newsapi()
# newsapi_clustering()
# mosaique_fm()
print(fact_checking())
