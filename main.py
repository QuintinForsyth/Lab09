import random
movie = {"Title":"Doctor Strange","Year":"2016","Rated":"PG-13","Released":"04 Nov 2016","Runtime":"115 min","Genre":"Action, Adventure, Fantasy","Director":"Scott Derrickson","Writer":"Jon Spaihts, Scott Derrickson, C. Robert Cargill","Actors":"Benedict Cumberbatch, Chiwetel Ejiofor, Rachel McAdams","Plot":"While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.","Language":"English","Country":"United States","Awards":"Nominated for 1 Oscar. 20 wins & 68 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BNjgwNzAzNjk1Nl5BMl5BanBnXkFtZTgwMzQ2NjI1OTE@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.5/10"},{"Source":"Rotten Tomatoes","Value":"89%"},{"Source":"Metacritic","Value":"72/100"}],"Metascore":"72","imdbRating":"7.5","imdbVotes":"691,025","imdbID":"tt1211837","Type":"movie","DVD":"28 Feb 2017","BoxOffice":"$232,641,920","Production":"N/A","Website":"N/A","Response":"True"}


def blog_generator (movie):
  blog = ""
  blog += headline_generator (movie['Title'])
  
  blog += first_paragraph(movie)
  
  blog += second_paragraph(movie)

  return (blog)
  
  
def second_paragraph(movie):
  num  = random.randint(0,1)
  line = ""
  if movie['Rated'] == "PG":
    if num == 0:
      line = 'The '+movie['Title']+' is film the whoile family can enjoy with it being rated as a ' + movie['Rated'] + 'movie'
    else:
      line = 'everyone and their dog will enjoy '+movie['Title']+ ', the age rating for this masterpiece is '+ movie['Rated']
  elif movie['Rated'] == "PG-13":
    if num == 0:
      line ='With a age rating of ' +movie['Rated'] +', the '+movie['Title']+' film is a must watch for everyone over the age of 13!'
    else: 
      line = 'The movie '+movie['Title']+' is a great film to watch with your rebelious teens, with an age rating of '+movie['Rated']+'.'
  elif movie['Rated'] == "G":
    if num == 0:
      line = 'The movie'+ movie["Title"] + ', can be enjoyed by everyone with a rating of' + movie['Rated']+ '.'
    else:
      line = movie['Title'] + ' is a a wonderous film to experience with the whole familly, with a age rating of'+ movie['Rated']+ ' the whole familly can enjoy the film.'
  else:
    if num == 0:
      line = movie['Title'] +' is a great movie to watch with your fellow adults with an age rating of '+movie['Rating']+' you wont have to deal with those pesky kids making noises while you enjoy your movie.'
    else:
      line = 'The film'+ movie['Title'] + 'is rated '+movie['Rating']+' with less kid like comedy and more mature themes this movie is a must for those who arent interested in cartoons.' 
  # ignoring nc-17 since its basically R
  line = line + ' The movie is ' + movie['Runtime'] + ' long but is worth every second!'
  ratings = movie['Ratings']
  good_words = ["good","great","nicely","well"]
  bad_words = ["bad","unfavourably","terrible", "poorly"]
 
  for i in range(len(ratings)):
    ran = random.randint(0,1)
    if ratings[i]['Source'] == "Internet Movie Database":
      l = rate_placer(i,ratings)
      l = source(l,good_words,ratings,bad_words)
      if ran == 1:
        lline = f" Over at {ratings[i]['Source']} the film did {l} with a rating of {ratings[i]['Value']}."
      else:
        lline = f" The film did {l} with the critics over at {ratings[i]['Source']} with a over all rating of {ratings[i]['Value']}."
    elif ratings[i]['Source'] == "Rotten Tomatoes":
      r = rate_placer(i,ratings)
      r = source(r,good_words,ratings,bad_words)
      if ran == 1:
        rline = f" Over at {ratings[i]['Source']} the film did {r} with a rating of {ratings[i]['Value']}."
      else:
        rline = f" The film did {r} with the critics over at {ratings[i]['Source']} with a over all rating of {ratings[i]['Value']}."
    elif ratings[i]['Source'] == "Metacritic":
      m = rate_placer(i,ratings)
      m = source(m,good_words,ratings,bad_words)
      if ran == 1:
        mline = f" Over at {ratings[i]['Source']} the film did {m} with a rating of {ratings[i]['Value']}."
      else:
        mline = f" The film did {m} with the critics over at {ratings[i]['Source']} with a over all rating of {ratings[i]['Value']}."
  

    
  line = line + lline+mline+rline    
  if movie['Awards'] is not None:
    line = line + ' '+movie['Title'] + ' also was '+movie['Awards'] +'! '
  return line
  
def rate_placer(i,ratings):
  im = ratings[i]['Value']
  imd = im[0]
  imdi = int(imd)
  if imdi > 6:
    return True
  return False

def source(single,good_words,ratings,bad_words):
  nums = random.randint(0,3)
  if single == True:
    single = good_words[nums]
  elif single == None:
    single = 'Unrated'
  else:
    single = bad_words[nums]
  return single
  
def first_paragraph(movie):
  special_word = worder(spec = "")
  high = ""
  line = 'in ' +movie['Year']
  box = movie['BoxOffice']
  office = box[1:]
  if (int(office.replace(',','')) > 10000000):
    high = "whopping "
  elif (int(office.replace(',','')) < 10000000):
    high = "measly "
  if movie['Year'] == "2022":
    line = 'this year'
    num  = random.randint(0,1)

  plot = movie['Plot']
  if plot is None:
    if num == 0:
      plot = ' Keeping spoilers to a minimum I wont be discussing anything about the plot in this blog'
    else:
      plot = ' for more information on the plot I\'d suggest you watch the movie... just so you dont get spoiled.'

  
    
  return 'The '+movie['Title']+' movie was released '+line+ ' and starred'+people_split(movie['Actors'])+'. The movie was written by'+people_split(movie['Writer']) +' and was directed by the ' +special_word+ ' '+movie['Director'] + '. ' +movie['Title']+' earned a '+high+movie['BoxOffice']+ ' at the Box Office. The plot of this movie is \"'+plot+'\" Sounds interesting right? well thats not it the movie also has these loved genres '+movie['Genre']+'!\n\n'


      #could have gone through all genres but stuck with some basic ones (fantasy and scifi are too similar so i didnt add them since most movies hit that anyways)
def people_split(typ):
  '''
  puts and for last person
  '''
  pep = list(typ.split(" "))
  line = ""
  for i in range(len(pep)):
    if i != len(pep)-2:
      line = line + " " +pep[i]
    else:
      line = line + " and " + pep[i]
  return line
  
def worder(spec):
  while(True):
    compliments = ["brilliant", "amazing","clever","splendid","respectable","intelligent","talented"]
    num = random.randint(0,len(compliments)-1)
    compliment = compliments[num]
    if compliment != spec:
      return compliment
    continue
  
def headline_generator(title):
  num = random.randint(0,1)
  if num == 0:
    return 'Can you believe what they are saying about '+title+'?\n\n'
  else:
    return 'Is '+title+' the best movie ever?\n\n'
    

blog = blog_generator(movie)
print(blog)
  



