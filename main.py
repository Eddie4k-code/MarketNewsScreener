import finnhub
import requests



finnhub_client = finnhub.Client(api_key=' ') #ENTER API KEY HERE





global var
current_news = (finnhub_client.general_news('general', min_id=0))


'''
NEWS SCREENER
'''
def result():
    for dict in current_news:

        title = (dict['headline'])
        source = (dict['source'])
        summmary = (dict['summary'])
        link = (dict['url'])


        print('-------------------------------------------------------------------------------')
        print(f'Title: {title}')
        print(f'Source: {source}')
        print(f'Summary: {summmary}')
        print(f'Link: {link}')


def update(): #Will check if article has already been displayed (set this on a while loop)

    for dict in current_news:


        title = (dict['headline'])
        source = (dict['source'])
        summmary = (dict['summary'])
        link = (dict['url'])


        old_news = []

        old_news.append(title)
        old_news.append(source)
        old_news.append(summmary)
        old_news.append(link)


        if link in old_news:
            pass
        elif source in old_news:
            pass
        elif title in old_news:
            pass
        elif summmary in old_news:
            pass
        else:
            result()

news_on = True
result()
while news_on:
    for dict in current_news:

       update()
