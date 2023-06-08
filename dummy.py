import datetime
import random

def create_dummy_data(channels, service_info):
    types = [
        'Channel Overview', 
        'Video & Comment Analysis', 
        'Keyword Analysis', 
        'Channel Controversy Check', 
        'Ad View Estimation', 
        'Advertiser Overview', 
        'To YouTuber Proposal', 
        'Youtuber Recommendation'
    ]
  # 'Channel A' through 'Channel Z'

    history = []
    today = datetime.date.today()

    i = 0
    
    for type in types:
        rand_day = random.randint(i, i+30)
        day = today - datetime.timedelta(days=rand_day)
        date = day.strftime('%b %d, %Y')  # Format date as 'May 16, 2023'
        
        # Randomly select 0 to 5 channels
        channel = random.sample(channels, k=random.randint(0, 5))
        
        if channel == [] :
            channel = ['-']

        history.append({
            'type': type,
            'channel': channel,
            'date': date,
        })
        i = rand_day + 10
    
    service = []

    types = [
        'service', 
        'details', 
        'purchaseDate', 
        'feedbackSubmitted'
    ]

    k = random.randint(1, 4)
    i = 0

    types = random.sample(sorted(service_info), k)

    for type in types:
        rand_day = random.randint(i, i+30)
        day = today - datetime.timedelta(days=rand_day)
        date = day.strftime('%b %d, %Y')  # Format date as 'May 16, 2023'

        service.append({
            'service': type,
            'details': service_info[type],
            'purchaseDate': date,
            'feedbackSubmitted' : False
        })

        i = rand_day + 10

    return history, service