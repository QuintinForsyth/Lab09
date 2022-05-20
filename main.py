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
      line = 'The '+movie['Title']+' is film the whoile family can enjoy with it being rated as a ' + movie['Rated'] + 'movie\n\n'
    else:
      line = 'everyone and their dog will enjoy '+movie['Title']+ ', the age rating for this masterpiece is '+ movie['Rated']
  elif movie['Rated'] == "PG-13":
    if num == 0:
      return 'With a age rating of ' +movie['Rated'] +', the '+movie['Title']+' film is a must watch for everyone over the age of 13!\n\n'
    else: 
      line = 'The movie '+movie['Title']+' is a great film to watch with your rebelious teens, with an age rating of '+movie['Rated']+'.'
  elif movie['Rated'] == "G":
    if num == 0:
      line = 'The movie'+ movie["Title"] + ', can be enjoyed by everyone with a rating of' + movie['Rated']+ '.'
    else:
      line = movie['Title'] + ' is a a wonderous film to experience with the whole familly, with a age rating of'+ movie['Rated']+ ' the whole familly can enjoy the film.'
  else:
    if num == 0:
      line = movie['Title'] +' is a great movie to watch with your fellow adults with an age rating of '+movie['Rating']+' you wont have to deal with those pesky kids making noises while you enjoyyour movie.'
    else:
      line = 'The film'+ movie['Title'] + 'is rated '+movie['Rating']+' with less kid like comedy and more mature themes this movie is a must for those who arent interested in cartoons.' 
  # ignoring nc-17 since its basically R
  ratings = movie['Rating']
  rates = ""
  for i in range(len(ratings)):
    if ratings[i][1] == "Internet Movie Database":
      l = rate_placer(i,ratings)
    elif (ratings[i][1] == "Rotten Tomatoes"):
      r = rate_placer(i,ratings)
    elif (ratings [i][1] == "Metacritic"):
      m = rate_placer(i,ratings)
    rates += f"{ratings[i][1]} + {ratings[i][3]}"
  num  = random.randint(0,1)
  good_words = ["good","great","nicely","well"]
  l = source(l,good_words,ratings)
  r = source(r,good_words,ratings)
  m = source(m,good_words,ratings)
  line = line+ movie['Title']
  return line

def rate_placer(i,ratings):
  im = ratings[i][3]
  imd = im[0]
  imdi = int(imd)
  if imdi > 6:
    return True
  return False

def source(single,good_words,ratings):
  if single == True:
    nums = random.randint(0,3)
    single = good_words[nums]
  elif single == None:
    
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
  return 'The '+movie['Title']+' movie was released '+line+ ' and starred'+people_split(movie['Actors'])+'. The movie was written by'+people_split(movie['Writer']) +' and was directed by the ' +special_word+ ' '+movie['Director'] + '. ' +movie['Title']+' earned a '+high+movie['BoxOffice']+ ' at the Box Office. The plot of this movie is \"'+movie['Plot']+'\" sounds interesting right? \n\n'
  
    
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
  



