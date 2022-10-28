import requests, bs4, praw


url = 'https://deadbydaylight.gamepedia.com/Shrine_of_Secrets'
r = requests.get(url)

trigger = '!ShrineAlert'

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('shrinealertbot')

soup = bs4.BeautifulSoup(r.content, 'html.parser')
shrine_table = soup.find('table', class_ = 'wikitable')

perks = []
for row in shrine_table.find_all('tr'):
    for cell in row.find_all('td',limit=1):
        perks.append(cell.text.rstrip())


for element in perks:
    element = element.title()


for comment in subreddit.stream.comments():
     print('Submission title: ' + comment.submission.title)
     print('Author: ' + comment.author.name)
     print(comment.body)
     print(len(comment.body)*'-')
     if trigger in comment.body:
         comment.reply('Reply.')



print("Insert the perk you want to be notified about.") # Placeholder, will get this from comment.body later
search = str(input()).title()


print(search)


if search in perks: #These will be sent to the user via PM in the future
    print(search + ' is on the shrine!')
else:
    print(search + " is currently not on the shrine. You'll be notified when it is")
print(perks)