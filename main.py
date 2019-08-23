from os.path import basename
import pandas

from articles.newsAPIdata4good import get_newsapi_articles, OUTPUT_FILENAME
from articles.mosaique_fm import get_mosaique_articles
from clustering.clustering_news import newsjsontocsv, datacsv
from fact_checking.source.fact_checking import fact_check
from fact_checking.source.key_words import key_words_list


## NewsAPI > tunis.json + tunis.csv
def newsapi():
    print("> NewsAPI : recherche des derniers articles...")
    get_newsapi_articles()

    newsapi_csv_name = basename(OUTPUT_FILENAME).split('.')[0] + ".csv"
    newsjsontocsv(OUTPUT_FILENAME, newsapi_csv_name)

    # newsapi_dataframe = pandas.read_csv(newsapi_csv_name, encoding="utf8")
    # csv_line_index_start = 5
    # csv_line_index_end = 6
    # one line: newsapi_dataframe[csv_line_index_start:csv_line_index_end])
    # one column, 'content': newsapi_dataframe.content
    # one cell: newsapi_dataframe.content[csv_line_index_start:csv_line_index_end]
    return newsapi_csv_name


# NewsAPI clustering > out-clusteringVocabALL.txt + out-articlesClusters.csv
#                    > out-wc_Title_X.png + out-wc_Content_X.png 
def newsapi_clustering(newsapi_csv_name):
    print("> NewsAPI : calcul des nuages de mots...")
    datacsv(newsapi_csv_name)


## MosaïqueFM > mosaique.csv
def mosaique_fm():
    print("> MosaïqueFM : recherche des derniers articles...")
    return get_mosaique_articles()


# > out-wc_Title_9_mosaique.png
# > out-wc_Content_9_mosaique.png
# Et fichiers auxiliaires :
# > out-articlesClusters_mosaique.csv
# > out-clusteringVocabALL_mosaique.txt
def mosaique_clustering(mosaique_csv_path):
    print("> MosaïqueFM : calcul des nuages de mots...")
    datacsv(mosaique_csv_path)


# fact checking
def fact_checking(csv_path):
    print(f"> {csv_path} : recherche de faits à vérifier...")
    csv_dataframe = pandas.read_csv(csv_path, encoding="utf8")

    for i, row in csv_dataframe.iterrows():
        print("---", i)
        
        article = row.article
        facts = fact_check(article, key_words_list)
        
        if not facts:
            print('✗', row.url, '\n')
        else:
            print('✓', row.url, '\n')
            
            # for one article, highlight identified facts
            for theme, fact in facts:
                article = article.replace(fact, f"\033[44;43m{fact}\033[m")
            print(article, '\n')


newsapi_csv_path = newsapi()
newsapi_clustering(newsapi_csv_path)
fact_checking(newsapi_csv_path)

mosaique_csv_path = mosaique_fm()
mosaique_clustering(mosaique_csv_path)
fact_checking(mosaique_csv_path)
