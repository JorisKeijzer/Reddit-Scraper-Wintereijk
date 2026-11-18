# Label-batch batch_0073

## Instructies
Je bent een marktonderzoeker voor een Nederlands e-commercemerk dat koperen inlegzolen gaat verkopen. Je codeert Reddit-threads over voeten, voetklachten, schoenen en inlegzolen volgens een vast codeboek.

Regels:
- Citaten (quotes.text) zijn ALTIJD letterlijk en exact uit de bron overgenomen, inclusief spelfouten. Nooit samenvatten, vertalen of verbeteren in dat veld. nl_meaning is een getrouwe vertaling, geen reclametekst.
- Codeer alleen wat er staat. Verzin geen beroep, diagnose of situatie die niet genoemd wordt; gebruik dan null of een lege lijst.
- Scheid eigen ervaring (first_hand=true) van advies uit de tweede hand, diagnoses door vreemden en reclame van fabrikanten.
- Neem ook tegengeluiden en negatieve ervaringen mee: wat NIET werkt is net zo waardevol als wat wel werkt.
- Noteer elke vermelding van koper, magneten, acupressuur of reflexologie, ook sceptische, in 'copper'.
- Een Reddit-reactie bewijst geen klinische werking. Zet claims_risk op 'medical' bij aandoeningen of behandelclaims, 'material' bij materiaalclaims (koper, antibacterieel, geur), anders 'comfort_only'.
- medical_red_flag bij diabetes, neuropathie, gevoelloosheid, branden/tintelen, infectie, (stress)fracturen of ernstige zwelling.
- marketing_insight_nl is een hypothese voor ons merk, geen feit; beloof daarin nooit genezing of pijnvermindering.
- Is de thread niet over voeten/schoeisel/zolen (bijv. een toevallige zoekmatch), zet relevant=false en houd de rest minimaal.

## Opdracht
Label elke thread hieronder volgens het schema `ThreadLabel` in `vocscraper/schema.py`.
Schrijf het resultaat naar `batch_0073.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: 6q8q7z, 1f0wrfr).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 6q8q7z ===
SUBREDDIT: r/Teachers
DATUM: 2017-07-29  SCORE: 50  REACTIES: 134
TITEL: Best teaching shoes? Going into my first year and have yet to find a comfy pair of shoes to look good but also not hurt my feet.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dkvh867] (score 35, diepte 0) I'm a first year teacher too, and I'd be curious how others respond, but Clarks are pretty comfortable professional shoes. I think some of their styles can look a little frumpy though
[dkvj5fr] (score 35, diepte 0) Nike running shoes. Extra wide with the mesh for air flow. Been rocking the same pair for 2 years now.
[dkvxnyj] (score 28, diepte 5) I have to respectfully disagree. We are professionals, and we want to be treated like professionals, but we also are interacting with students. Many teachers spend all day on their feet, most executives do not. I suspect if they did, there would be more options as far as professional shoes with a higher level of comfort and support. 

As far as nice shoes, shirt, and tie for male teachers, that's not necessarily true. I grew up in a rural area and while there were a couple of people who dressed up, most teachers dressed more business casual. I think this is good for students to see. Most students are not going to be company executives, business casual is important for students to be able to recognize. 
I feel that it's helpful for teachers to dress more nicely than their students, so if the school requires polo shirts, teachers should avoid them. 

I agree that I don't necessarily want to see my doctor in cut off jeans and flipflops, but I also don't expect to see him wearing a formal suit under his white coat. It's all about reasonable expectations for the job being performed. Khakis, shoes barely on the dressy side of athletic, and a polo shirt are good enough for my doctor, why shouldn't they be for me?
[dkvk09o] (score 17, diepte 0) Get a good pair of insoles. Honestly, you can rock a shoe that fits with a nice inside. I got some knock off Tom's at Target today that are super cute. I'm just going to throw some insoles in there!
[dkvwv76] (score 16, diepte 3) I believe I would do better as a teacher in a pair of athletic shoes than dress shoes. When I'm comfortable, I'm happier and more likely to be engaged with students. I know some dress shoes can be comfortable but I have a tough time with shoes in general. I would love to see a blended shoe that looks nicer while offering support and staying on my feet. And no, I don't want the ugly blocky shoes made for the elderly.
[dkvow6p] (score 15, diepte 1) I love this comment, but I wear formal shoes.
[dkvtkjs] (score 15, diepte 0) Dansko professionals all the way. I've tried a lot of different ones to try to switch it up Keens, Clarks (don't fit me well), and Merrells. If I'm doing a field trip I wear my Hoka sneakers. They actually came out with a lower profile trail runners that see mostly black. Super comfortable.
[dkvl803] (score 13, diepte 0) I love me some Clark's. Comfortable and durable.
[dkvqket] (score 12, diepte 1) Came here to say Clarks too. They do a great job of looking professional but being comfortable. And in the summer they usually have a two-for-$99 sale. Can you beat that.
[dkvxxf5] (score 12, diepte 5) Aren't scrubs basically pajamas?
[dkvsnpc] (score 12, diepte 0) Find a sketchers outlet. They have every type of design, from tennis shoes to more formal. I usually opt for some black, nice material bobs. They are all memory foam. I literally wore the same pair everyday. Alleviated any leg and back pain the concrete floors were giving me in other shoes. The outlets also usually have an ongoing buy one get one half off.
[dkvmwq2] (score 9, diepte 1) I used to wear "hip" sneakers in my first years of teaching.  Wrecked my feet.  I've since followed the lead of my more experienced colleagues and have exclusively been wearing running shoes... Nike Air Pegasuses have changed my life.
[dkvy9u4] (score 9, diepte 6) And they're always in running shoes.
[dkvycj6] (score 9, diepte 3) I can dress professionally and wear Nikes.  They aren't neon orange or anything.
[dkvs0zm] (score 9, diepte 0) If you're in England - Ecco. Usually £100, typically £50 in a sale. They look like formal brogues, but they're very comfortable and allow free movement.
[dkvj2ev] (score 8, diepte 0) I wear Birkenstocks. They are surprisingly comfy!
[dkvw55r] (score 7, diepte 1) Birkenstock an white socks is the way we teach in germany.
[dkw2ftb] (score 7, diepte 5) I'm not a lawyer going into a court room, or a police officer.  I got very simple, gray Nikes (gray is one of our school colors) and they are much nicer than the flip flops other teachers wear.  I certainly don't wear them on days I'm being observed or for parent teacher conferences.  This means that while I find them professional, they are on one end of the 'professional dress' spectrum.  I'm going to wear a nicer shirt/slacks/shoes on those days.  Other days, I'm going to wear what is comfortable, but still professional.
[dkwc0p1] (score 7, diepte 7) I don't think they are unprofessional, but there are more professional shoes.  I don't wear school teeshirts those days either, though they are encouraged.  Anything I wear to school is professional, but there are some things that are more dressy/formal and things that are more casual.  There's a pretty big spectrum of what is considered business casual these days.  Jeans can even look pretty professional and nice when dressed up with  a nice top and fancy shoes.
[dkvsvxp] (score 6, diepte 1) I've only ever had the clarks cloudsteppers. I love them, but the memory foam gets all gross and wears out after a few months of heavy use. Are their traditional shoes as comfy?
[dkviyux] (score 6, diepte 0) I have a friend who swears by the Tieks ballet flats. I've tried hers on before and holy cow, they are insanely comfortable. However I'm not exactly jumping at the chance to drop $170 on one pair of flats. However, I found some flats at- surprise- Walmart (faded glory brand, leather flats with elastic back) that I think are cute and they are super comfy and durable and to me, they feel comparable to Tieks. I have them in blue, black and brown and they are only like $19. Highly recommend.
[dkvs7d2] (score 6, diepte 3) Last year I once wore the same adidas track pants (you all know the kind...), same blue school t shirt and same fucking grey shoes as one of my most difficult students. 

It was glorious. I sent a photo to his parents informing them that he really wanted to be me that day.
[dkvkz8d] (score 6, diepte 0) Vans
[dkvs8ss] (score 6, diepte 0) Skechers Go Walks. My feet are functional, not ornamental. Don't like the look of sneakers on my elderly feet - don't bother to look. I've got teaching and moving to do, and I'm not at my best when my feet hurt.
[dkvj2p5] (score 5, diepte 1) In my opinion, Tieks are a bit overrated- and pretty overpriced. I wear VidaLeather flats I bought on Amazon for (I think) $60. Wore them nearly every day last year and I find them very comfortable and supportive. Tieks are nice, I just can't justify that price when these flats are essentially the same without the blue sole.
[dkvn3fs] (score 5, diepte 1) Totally have to agree with boost here. My principal luckily allows us to wear any shoe we like so we can be comfortable since we're standing majority of the day and for me it's boost all day every day.  Plus getting into the sneaker game helps start conversations between you and students (both males and females) which is a nice bonus.
[dkvom13] (score 5, diepte 0) Crocs actually has some really fashionable shoes now. When it's warm I wear these black Croc sandals that are super comfortable and you can't tell they're Crocs.
[dkvv5k9] (score 5, diepte 0) YES to dansko clogs. They are amazing. The only shoes I can wear and my back doesn't hurt at the end of the day. Worth every penny!
[dkvm93r] (score 4, diepte 2) As long as you dress "better than the students," you should be fine.  Our school staff dress policy is business casual, and you can find lots of great stuff that qualifies as such.
[dkw3flc] (score 4, diepte 6) If it's professional why wouldn't you wear it with your observations or conferences?  My observations are drop in, so even more support of the fact I need to be dressed well at all times.
[dkw36gs] (score 4, diepte 3) I get that, but on the other hand this is a job where we are on our feet constantly, for like 7 hours per day. If I had been wearing proper dress shoes for the past 8 years, I would be completely crippled by this point.

I tried it my first year. I went the entire first semester wearing dress shoes. I was in constant pain. So I switched to New Balance athletic shoes and now being on my feet isn't a big deal. I still dress very nicely, except for my shoes (which are very plain gray, so they don't really stick out at all). I just think of it as dressing appropriately for the work I'm doing (being on my feet all day).
[dkvujxs] (score 4, diepte 0) Sanita clogs (they are the company that originally designed Danskos). They make a huge difference for me compared to wearing dressy heels, flats, or wedges.
[dkvvhq5] (score 3, diepte 2) They are comfortable
[dkvhccm] (score 3, diepte 0) I got Merrell's they are cute flats but they have nice soles so I can run in them.
[dkviw73] (score 3, diepte 0 OP) Have any of y'all tried Tieks?
[dkvnq9d] (score 3, diepte 2) I know this is crazy but Walmart has memory foam padded leather flats in both Black and Tan for like $8 that are surprisingly comfy. I teach in mine quit a bit.
[dkvj305] (score 3, diepte 1) I've heard really great things about them! To be honest I really like target flats, it seems like they have added for padding which has been nice. I also wear a lot of ankle booties which are comfortable for me. I tend to pick cute over functional though, ha!
[dkvjj8k] (score 3, diepte 3) I totally get it, I had foot surgery right before I started teaching and my feet got wider so I have to be careful with flats. If you have a Nordstrom around you I would check it out for shoes, they are super knowledgeable, have a huge selection and there's a sale right now. Their shoes can be a bit spendy but they have great quality. I have comfy shoes from them that I still wear to work 5 years in.
[dkvvoby] (score 3, diepte 1) Tieks are amazing. I have one pair my Mom bought, didn't like and gave to me, but of course, they're in Navy and not in a daily wear color (for me, at least -- black, gray or a neutral light tan go with more of my stuff, Navy goes with a few things).
[dkvj5fo] (score 3, diepte 1 OP) Really? I love birks but not sure if they are appropriate for my school. By then again I'm still trying to figure out a suitable "teacher" wardrobe also
[dkwbxni] (score 3, diepte 7) I don't think that tennis shoes are unprofessional, but there are more professional shoes.  I wouldn't wear a school teeshirt on those days either, but they are acceptable in my workplace, even encouraged.
We don't have drop in days and if we did, I wouldn't be worried that my Nikes would even register to my administration.
[dkvsb33] (score 3, diepte 1) They're ok. No arch support or padding, but they don't rub my feet.
[dkvl5cf] (score 3, diepte 0) Professional: Cole Haan Lunargrands. They have Nike's lunarlon sole in the shoe so it's comfortable when you're standing or walking around the class and also professional/fancy/stylish. 

Casual: Adidas Ultra Boosts. They're on the expensive end, but I assure you that they're worth every penny and your teaching feet will thank you.

edit: typo
[dkvylok] (score 3, diepte 2) Sneakers are a *huge* deal for kids in my school. I have students from prior years tracking me down in the halls so they can show me their new kicks.

If a group of boys are huddled over a laptop in my classroom, they're most likely checking out shoes. Cracks me up.
[dkvmj2l] (score 3, diepte 0) Sketchers can be a life saver, I know they're not always attractive or flattering but I couldn't imagine a fill day without them
[dkw0pz8] (score 3, diepte 1) I got a pair of [blue mesh loafers from Skechers](https://www.skechers.com/en-us/style/68243/bayshore/nvy) and I get compliments every single time I wear them.  And what's better is that they are amazingly comfortable.
[dkvu2mt] (score 3, diepte 1) They sell them in the U.S. too.  I have two pair for work and second what you've said.  They're about $140 here.
[dkvt1o2] (score 3, diepte 0) Aerosoles!! AAANNNDDD they offer a teacher discount
[dkvzm64] (score 3, diepte 1) I've worn Dansko/Sanitas for 5 years and they have been mostly good to me, but when I went in to a specialty shoe shop, they said they don't recommend Danskos! And recommended Birkenstocks to me instead. Wearing a pair now and they feel like heaven!
[dkvwano] (score 3, diepte 0) Payless has a line of ballet flats with memory foam that are very flexible and get me through a day. I have several pairs. 

I also like Keens and Dansko, if I'm feeling spendy. Shoes are a good place to invest your wardrobe money for sure.
[dkvv71l] (score 2, diepte 2) I had no idea they ran a sale like this!  Game changer!  I'm still rocking my original 2 pair from my practicum 5 years ago but would like to replace in the next year or so.
[dkw7jwd] (score 2, diepte 1) I have worn clarks for the past 3 years and am about to buy a new pair for the school year.  They rule.
[dkvj7o2] (score 2, diepte 2 OP) True! I'm trying to find the nice middle ground. My feet are wide so I'm trying to find a nice shoe to accommodate that. Ballet flats look like to be the go to show but I've never found any that don't hurt haha
[dkvygj9] (score 2, diepte 2) I have a pair of purple ones.  I love them but I don't wear them everyday.  I'm a bit disappointed that the color has rubbed off some of the sides, but I've had them for almost 4 years now.
[dkvn9u0] (score 2, diepte 1) I second this. I wear my birks almost exclusively. I have a permanent tan on my feet from wearing them during recess lol.
[dkw2rth] (score 2, diepte 3) Sad to see this comment downvoted.  Fully agree with you, but we're in the minority.  

Edit:  I do understand that there may be a divide between Elementary and upper grades, and things such as the PE department, or art or drama, etc.  Would be odd to have K teachers in shirt and tie but by the same token it is odd for a male HS teacher to be without.
[dkvjqak] (score 2, diepte 0 OP) Have y'all tried the toms ballet flats? They look comfy but I'm not too sure!
[dkvu04l] (score 2, diepte 1) I've been wearing Toms classics since I student taught, so about 6 years now. Highly recommend, they're so comfortable.
[dkvz1um] (score 2, diepte 1) I have a pair of their ballet flats that I teach in sometimes, but I find their classics much more comfortable!

Unless it's sandal weather or snowing, I'm teaching in toms.
[dkvx0ty] (score 2, diepte 2) Good ol' Dr. schols
[dkvk68f] (score 2, diepte 0) Dr. Scholl's women's flats. Full stop. They are cute and have memory foam insoles. I wear them everyday and have them in many colors. I dress professionally when I teach and these are perfect.
[dkvslbf] (score 2, diepte 1) I have both a black and brown pair of the Cole Haan Original Grands - they are seriously comfortable.  I'm sort of a sneaker head and these shoes are as comfortable as any pair I've ever owned. You need to find them on sale though because the original price is $279.  It's tough to find black or brown on sale but I was able to get them for around $110 each.  They do often have a lot of funky colors on sale if you want to add some personality to your wardrobe but if you want more formal colors, you need to be lucky/persistent to find a good deal.
[dkwgz04] (score 2, diepte 1) Me, too. I wear the Kaedee flats almost every single day.
[dkvsbb4] (score 2, diepte 0) If your looking for men's shoes I have had great luck with my Rockport slip on black dress shoes. I can link it later if you wish. As a larger man I am a big fan of adidas shoes. I just bought a pair of Terrexx cross trainers that I think will be great for classroom as well.


Edit: probably should've look at your username... I'm guessing you don't need men's shoes.
[dkwd09r] (score 2, diepte 1) Yup, I have a pair that look like lacy flats (with better traction) that are so comfortable and go with pants or skirts! Skechers forever!!
[dkvvii8] (score 2, diepte 2) I wonder how many of us have usernames that start with Mr/Mrs/Ms/Miss
[dkvt9yc] (score 2, diepte 0) I am now swearing by Vionic brand shoes. I developed plantar fasciitis last year, and it took FOREVER for the swelling to go down. But these shoes kept me from having a flare up while I was walking miles and miles on my vacation this year. They are also super cute. I wore them to work a lot to help break them in, and I got a lot of compliments.

I also bought a set of their insoles for my converse I wear on Fridays. I love that they have shoes AND insoles, so you can get the same Vionic effect in any of your shoes.
[dkvtpeq] (score 2, diepte 0) I recently got a great pair of loafers that have become my new every day pair of teaching shoes. Basically, get something comfortable that is quality (yes it'll cost a bit more for good quality) because you are spending all damn day on your feet. If you get poor quality shoes you put yourself at risk of foot and leg pain (including shin splints). Plus good quality shoes last A LOT longer if properly taken care of.
[dkvzn1w] (score 2, diepte 2) I have two pairs that I switch between, and my kids are also fascinated by them. It was pretty hilarious when the "WHAT ARE THOSE?" Vine was a thing.
[dkvv9jt] (score 2, diepte 0) I bought a pair of Sketchers shoes before my internship and wore them almost exclusively for two years. This year I was in Florida and hit a Sketchers outlet store to buy another pair of shoes to wear to work.
[dkvva41] (score 2, diepte 0) to be honest- in the warmer months I wear nicer sandals and in the cooler months I wear nice boots.  I also like wearing Tom's wedge boots, which allow me to feel slightly more dressed up but are comfy AF.
[dkvvki0] (score 2, diepte 0) I do well with pretty much any kind of Aeresoles (if they have a very high wedge heel or something, they aren't magic, so that can feel less comfy as the day goes on, but I wear flat ones for teaching). I wear the slightly dressy flip flops and the ballet flat style ones on the regular. 

Toms are OK too. Not sure I find them "attractive" as they seem like the most neutral looking shoe on the planet, but at least I don't find them unattractive like some comfort shoes.
[dkw27si] (score 2, diepte 0) [Keen Citizen](http://www.keenfootwear.com/p/M-CITIZEN-KEEN-LOW-WP.html?dwvar_M-CITIZEN-KEEN-LOW-WP_color=1015131&cgid=mens) in Black. They look nice enough for business casual, and they provide my feet a fantastic cushion. Further, they're good for traction and waterproof. These have my vote.

For casual Fridays, I wear New Balance Minimus, and for days where I wear a shirt and tie, Dockers.
[dkw97dn] (score 2, diepte 0) Go find a store that sells farm supplies or lawnmowers or construction equipment... and also shoes. Find "Non-conductive soles." The only work that requires non-conductive shoes is factory work. Those are shoes meant to stand on concrete for 12 hours at a time. Right before I taught, I worked 12 hour shifts in a factory. 

Also, you can find some pretty bad-ass looking styles. Trust me, kids notice.
[dkwgp3m] (score 2, diepte 0) People don't believe be when I saw my shoes are Dr. Scholls, but they've got some incredibly comfy shoes that look great!! I can honestly wear them all day, go to dinner, grab drinks, come home, and never once think of foot pain.

These are my personal favorite: https://www.amazon.com/Dr-Scholls-Womens-Dillion-Stucco/dp/B01DF0A9HU/ref=sr_1_14?ie=UTF8&qid=1501365653&sr=8-14&keywords=dr+scholls+booties
(59 reacties met lagere score weggelaten)

=== THREAD 1f0wrfr ===
SUBREDDIT: r/Teachers
DATUM: 2024-08-25  SCORE: 138  REACTIES: 114
TITEL: First year kinder teacher.. I survived the first week. My feet are in so much pain. 
POST (source_id=post):
I survived my first eight days of teaching. With the kinders I'm constantly on my feet watching them/redirecting them. My feet are dying. I worked from home previously. I've worn my hokas and air force 1s but my feet/legs are still so sore this weekend. I'm not used to standing all day. My throat is also hoarse from raising my voice so much. I don't like yelling, but if I don't theyre off in la la land ignoring me. They've improved from day 1, but we are still working on staying in our seats, raising our hands and waiting to be called on, not yelling out, all the things… I knew their attention spans would be short, but I didn’t realize it would be this bad.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ljuy1h0] (score 159, diepte 0) Takes about a month for your feet and legs to adjust. We’ve all been there! After this you’ll be able to stand for houuurrrrssssss. Long line at the airport? You’re good! 1.5 hr wait for a Disney ride? Good to go. Broke down 3 miles from civilization? LFG!
[ljuv7mz] (score 72, diepte 0) Compression socks. They really do help
[ljv2v7y] (score 66, diepte 1) And sitting for long periods of time will begin to drive you crazy.
[ljuzv4z] (score 65, diepte 0) Welcome to kindergarten! Were you also in bed by 8 on Friday? That’s usually how it goes for me. 🤣

I’m 7 months pregnant and my feet and legs have been FEELING it after this first week. I’m not ready for another week!
[ljuvo18] (score 46, diepte 0) Try singing instead of yelling when they are in la la land - it sounds insane but it really does help.
[ljvg3uf] (score 45, diepte 2) I’m 37, and some days I have to manually unbend my legs from the car when I get home. 

We do yoga in the mornings and I tell them it’s to calm our bodies and minds for the day, but it’s really for me to get some good stretches in 😩
[ljv7ol6] (score 40, diepte 1) At least until you hit 35 and realize you've ruined your legs and feet for the rest of your life and your doctor just shrugs.
[ljv2jqm] (score 37, diepte 0) I teach loud high schoolers but I never have to raise my voice to get their attention.

Let me introduce you to my friend: the quiet coyote.

Raise your hand up, put your thumb against the top of your middle and ring finger, stretch your index and pinkie out.  
Every kid that sees the quiet coyote has to quiet down and do the quiet coyote until eventually all kids are doing quiet coyote. It's great at getting kids to shush each other and they pick up on the procedure very quickly.
[ljuxb4j] (score 25, diepte 2) They also don’t even have to be “songs” necessarily - just whatever you want to say, sing it instead! It can be totally random notes 😂

I also think it’s helpful to have a couple tunes that you can fill in any instructions you need to give. I use “the farmer in the dell” a lot:
It’s time to - - -
It’s time to - - -
So - - - - -
It’s time to - - -
(Like it’s time to go outside/so line up by the door, or it’s time to eat our snack/so find a seat at the table, or it’s time to read a book/so find a seat at the carpet)

I’m also not sure the name of the original tune but I like the one that goes
“This is the way we - - - - -
This is the way we - - - - -
This is the way we - - - - -
To get ready to learn”
(With fill ins like “clean up our things” “come to the carpet” “line up for specials” “sit right down” “fold our hands”)
[ljv66qk] (score 20, diepte 1) I wear black Brooks sneakers too.  Game changer for me!
[ljv477c] (score 20, diepte 2) My mentor teacher sings “time to sit on the rug” over and over to the tune of…the farmer in the dell? To her first graders and it fully gets stuck in my head. She also has one of those microphones with a small speaker around her neck to save her voice. I believe all the teachers in my district have them
[ljv7t05] (score 15, diepte 2) Brooks Ghost 15s changed my life, seriously.
[ljvhi01] (score 13, diepte 2) Brooks Adrenaline are my go tos. I have high arches and they’re very supportive. Brooks has an online thing (or at least used to) where you stand on your phone in scans your foot it asks you questions about your needs and it recommends you what shoes of theirs are best for your needs.
[ljuw4ps] (score 13, diepte 1 OP) Thank you.. I made a book of songs but I’ll have to learn some! I don’t have any of the little songs/chants already memorized. We did some call backs this week and they did get one call back thankfully.
[ljwra1q] (score 13, diepte 2) This! Get some compression socks and checked for orthotics early.
[ljv55qj] (score 13, diepte 0) This is why teachers should wear sneakers! If school administrators want us to be up and moving all day then comfortable shoes are a must!
[ljwo516] (score 12, diepte 3) That's alright, kill two birds with one stone.
[ljw7a4u] (score 10, diepte 1) I have very much "we can walk" stamina for someone who grew up in  one of the least walkable areas in the country.  My ex was confused when I parked in a different state and walked to the downtown area because there was free parking.  He asked if we should Uber back to the car.  Lol.
[ljv9wzj] (score 10, diepte 1) I’m 6 months pregnant.  It teaching KG but it’s crazy how much more sore my feet and joints are. 🥲
[ljvaru3] (score 10, diepte 2) I feel you! I decided I’m just going to scoot around on my rolling chair this week, I don’t even care lol. 😅😂
[ljv7flq] (score 10, diepte 0) Compression socks and tights are a game changer. Snag tights have some that I like
[ljvlb6o] (score 9, diepte 2) The beauty of elementary kids is that they don't care and don't judge you on your singing voice so you can sing anything and everything and it will work to get their attention without worrying about being embarrassed by your singing abilities. Also, movement with sound or even without sound can be a great attention getter -- if you can hear me clap, "freeze in place!" ... this sort of thing makes it a game. Praise and possibly reward the ones who are doing what you say -- Jaylen is doing a great job of freezing in place! Ellie what a great freeze and being so quiet too! Similarly, do a game of Simon says (Teacher says) to get their attention and interest. Ask your fellow kindergarten, 1st and 2nd grade teachers about what videos on YouTube that their kids love -- these are often songs that your kids will know and love too.
[ljv502y] (score 9, diepte 1) I saw that on Pixar’s Soul!
[ljvkvi4] (score 9, diepte 0) Get a harmonica or little flute.  You can use a tone to get their attention instead of their voice.
[ljvyd8c] (score 8, diepte 2) As someone else said- it doesn’t have to be an actually song. At all. You can literally sing “class… I would like you to sit cross cross on the rug. Pleaaaaaase” 

This works. 

Also - try giving them directions while moving your mouth and using wild hand gestures but not saying anything. They get really interested and all try to figure out what you want them to do. You’d be shocked at how NOT talking to them can get their attention.
[ljwae8m] (score 7, diepte 1) Aanndd, you will be able to go 10 hours without needing to use the restroom! Pretty nice on long trips.
[ljuzrty] (score 7, diepte 0) Stretching and leg strentging exercises really helped my feet. Good posture and mobility made a world of difference for me.
[ljv803h] (score 7, diepte 2) Which really helps because most of the students have too. I used it jokingly with my new 7th graders last week and tons instinctively joined in. It was great.
[ljvyz3t] (score 7, diepte 3) Yep it's funny how culturally pervasive it is, and it's so simple even those who have never seen it before catch on from body language of their peers.

I once brought an auditorium of circa 500 students to a complete silence in seconds using it after finding my microphone was not working
[ljv72it] (score 7, diepte 0) People don’t realize how physical this job can be. It’s a marathon, not a sprint.
[ljvko2k] (score 7, diepte 0) Learned from a Kinder teacher I was interning with and used while I was teaching. (This also serves to reinforce prepositions) 
Quietly say, “I you can hear me, put your hand over your head.”
Then continue with other similar phrases like a game. The kids closest to you will start doing it and the others will catch on. 
 “If you can hear me, put your hand next to your ear.”
“If you can hear me, put your hand in front of your tummy.” 
Keep going until they are all listening! 
Intermittently reward fastest kids that do it for reinforcement to be on the listening lookout for when the game starts.
[ljvrt76] (score 7, diepte 0) I bought a voice amplifier on Amazon.
The single best teacher thing I’ve bought in awhile.
[ljxd3bi] (score 6, diepte 2) omg work something out with your colleagues for coverage!  Trust me, you can give yourself UTI, constipation and incontinence not going enough and cutting your bathroom break too short.
[ljxdm3c] (score 6, diepte 3) 23 year veteran here. I am finally at a school where I am near a restroom. But at this point, I've mastered my bladder. Until 3 pm, at which point I will use the restroom about 10 times before bed 🙄.
[ljv7cqx] (score 6, diepte 0) I feel all of this! Crocs in sport mode? Also, I love attention grabbers. Here's a few I will use and my third graders know to get quiet and listen when I use these. Takes some training of course!

I say: surfs up
They say: shhhhhhh (and make a wave with their hands)

I say: hocus pocus
They say: everybody focus

I say: gingerbread, gingerbread
They say: ohhhh snap (and snap there fingers)

Anyway, you can find more cute ones online or just make up your own using your favorite song lyrics, poems, lines from a movie, etc!
[ljvtfft] (score 6, diepte 1) I mean, I still use most of these suggestions for middle school. But then again, most middle schoolers act like kindergartners...
[ljwrxet] (score 5, diepte 2) Getting a microphone helps a ton.  Even if you are doing call and response.  If you have windows in your classroom you can turn off the lights to grab their attention. Some kindergarten teachers like using bells or singing bowls.
[ljv5wy3] (score 5, diepte 0) I taught second grade, and I sang all the time. Sometimes,  an actual song and other times just the instructions sing to whatever tune was in my head. My other go-to was I'd switch to Spanish, and the kids(none of whom actually spoke Spanish)  would quiet down, trying to figure out what I was saying.
[ljv96kz] (score 5, diepte 0) Not to sound unkind, but your feet will get used to it. I average about 10k steps a day, and occasionally have to trade my shoes for slippers with memory foam as soon as I get home.
[ljwgrpt] (score 5, diepte 2) Yeah, In music, I taught K-8th
[ljwgw31] (score 4, diepte 1) Buy good walking shoes. The little ones can be a handful in the trimester, but they start to mature as the year progresses.

(i did my clinical practice in Kinder)
[ljvfczv] (score 4, diepte 0) Buy at least 2 pairs of the best shoes that you can afford. 4 pairs in slightly different styles are even better. Change shoes halfway through the day and  don't wear the same pair 2 days in a row.

And wear above the knee compression socks.

It really makes a difference.
[ljvik55] (score 4, diepte 0) Good shoes are a must. Start stretching and icing before it turns into plantar fasciitis.
[ljw7p5i] (score 4, diepte 1) If your room doesn’t have an amplify system, you can get relatively cheap “tour guide” microphone systems. They have a headband microphone connected by cord to a speaker on a long lanyard. 

I bought one during Covid to help with amplification over the mask, and it really helped. I think it was around $35 at the time.
[ljwb7k5] (score 4, diepte 0) WARM UP YOUR VOICE! I’m a choir teacher who had to go through some voice therapy last year because I didn’t take care of it in the mornings. Seriously. If you warm up your voice just 10-15 minutes each morning and cool it down at the end of the day, it will make such a difference. Some ideas on what to do:

- gentle humming (doesn’t even need to be to a tune)
- humming but using a straw and some water
- lip trills/buzzing, up and down your whole range
- looks up some videos on YouTube, there are tons, even specific to teachers

Like others have said, having an amplifying device in the classroom will help and try as much as possible not to raise your voice.
[ljweax0] (score 4, diepte 0) My wife lives in berkinstocks (however you spell that). We get her 2 new pairs every year. Find a fancy footwear store near you and try on different pairs till you find the right brand for your feet. And never wear anything that hurts your feet just to look nice. Most teachers will end up getting foot surgery, do everything in your power to avoid that.
[ljxgpa4] (score 4, diepte 0) I teach K and sometimes I whisper when they’re on the carpet or lower my voice when things are overstimulating. 

I also play the “if you can hear me, touch you head…if you can hear me touch your nose/clap/etc” game. And I also have a doorbell.
[lk05okr] (score 3, diepte 1) And practice, practice, practice with the doorbell. Tell them about the new doorbell. Demonstrate the sound.  Ask them to be noisy and listen for the doorbell and get quiet when they hear it.  Praise them but say they could do better at freezing and listening when they hear it. Always follow the doorbell sound with softly spoken instructions. For practice, it could be something as simple as “touch your ears.” Use a softer than normal speaking voice, so they really have to listen. When children really listen to a soft sound, they naturally quiet down themselves. 
You could try a series of softly spoken instructions: 
1. touch your ears (pause to see who is responding-some may want to continue to play)
2. Shrug your shoulders (pause again)
3. Touch you toes (will make it obvious who isn’t tuned in, and you can silently walk nearer that child)
4. Walk to your circle spot. (There will be noise now, but everyone will know what to do and be heading where you need them to be for the next activity)
[ljxh0ty] (score 3, diepte 1) This right here. I don't care if I'm not wearing the nicest or prettiest shoes. I already have knee and back problems so I will wear my tennis shoes. It takes some time to find a brand that works well for you, I personally rank Adidas as first and Nike as second, but some peoples opinions are different than mine. Plus both brands make good shoes that are also fashionable
[ljv974j] (score 3, diepte 0) Soak your feet at home; it helps with the recovery. Put honey and lemon in your hot tea during the day. Get a bell of some sort to use as an attention signal. Practice with the kids so that they learn to respond to it quickly. I have a doorbell in my desk. The kids stop and listen for transition instructions when they hear it.
[ljvyhdm] (score 3, diepte 2) Former K teacher. Current 6th grade teacher. I agree. 🤣
[ljvksju] (score 3, diepte 0) Wondering if your classroom might have a microphone / amplification system? Teaching changed a lot for me (and I was subbing at the time) when those became available. I could speak in a normal voice or even softly/whisper and it would get their attention (sometimes the softer I spoke the quieter they would get). I also learned a lot of nonverbal attention getters that worked wonders. Quiet coyote is one, I also learned one from a colleague. You start by putting one finger up; students that see you do this hold up a one, you keep counting with your fingers silently and students match the number on their fingers (so if they see you at three, they’re holding up three). You set a goal beforehand, like- I want everyone’s attention at five and practice practice practice. They will help their peers get there, just like with quiet coyote. My 4th graders loved it and it saved my voice and patience many a time.
[ljvm4jx] (score 3, diepte 0) I teach HS science and am constantly on my feet during work. After 8 years, I ended up developing plantar fasciitis in my left foot and got prescribed a calf stretch regiment to fix it… but the real long term fix was buying orthopedic shoes. A friend of mine recommended Kurus. They’re a bit pricy but I’ve been using them for a year now and my PF hasn’t come back yet! [https://www.kurufootwear.com/pages/p-home-page-1?g_acctid=339-858-5723&g_adgroupid=149595348867&g_adid=706195035587&g_adtype=search&g_campaign=Paid+-+Search+-+Brand_KURU+Efficient+%28US%29_G_AQ&g_campaignid=19684801116&g_keyword=kuru%20shoes&g_keywordid=kwd-15615908306&g_network=g&gad_source=1&gbraid=0AAAAAD7fsteH9-mAxkxZZt1jodkzXyWRE&gclid=Cj0KCQjwrKu2BhDkARIsAD7GBovJrd8twLTcMb1pTp4CAONh9jMVLcvV0m-X3rK7IS_o59f0pI5vLAQaAtSYEALw_wcB](https://www.kurufootwear.com/pages/p-home-page-1?g_acctid=339-858-5723&g_adgroupid=149595348867&g_adid=706195035587&g_adtype=search&g_campaign=Paid+-+Search+-+Brand_KURU+Efficient+%28US%29_G_AQ&g_campaignid=19684801116&g_keyword=kuru%20shoes&g_keywordid=kwd-15615908306&g_network=g&gad_source=1&gbraid=0AAAAAD7fsteH9-mAxkxZZt1jodkzXyWRE&gclid=Cj0KCQjwrKu2BhDkARIsAD7GBovJrd8twLTcMb1pTp4CAONh9jMVLcvV0m-X3rK7IS_o59f0pI5vLAQaAtSYEALw_wcB)
[ljwb93m] (score 2, diepte 2) Same.  I love my Brooks.  When I wear my Air Force 1s my feet hurt for several days.
[ljyrt7w] (score 2, diepte 4) I know, right?
[ljxcowo] (score 2, diepte 1) Really have to buy the best orthopedic stylish shies possible.  Compression socks in winter.
[ljvo0uz] (score 2, diepte 1) I wear crocs at home now, so comfy!
[ljvo30v] (score 2, diepte 2) I do dearfoams.
[ljv9unv] (score 2, diepte 0) Do the alphabet with your feet while doing roll. Take every opportunity to stretch with your toes. Compression socks to your knees if you can. Let me echo birkenstocks and arch supports if needed. If you have flat feet get brooks. A running store can tell you your arch situation.
[ljvnf1z] (score 2, diepte 0) Compression socks at night help me.
[ljvno2w] (score 2, diepte 0) Yeah. One of the quiet perks of early childhood education is the work out. Since starting teaching I consistently have lost weight without even changing my diet.
[ljvnuy6] (score 2, diepte 0) You have to learn to speak from your diaphragm and not your throat. It’ll reduce the strain on your vocal cords
[ljvxcm2] (score 2, diepte 0) Blundstone boots.  I have over pronated soles and wear mine every day.
[ljvxi0e] (score 2, diepte 0) To help your voice- try to look up vocal exercises on YouTube that help you project from your breath/abs and not just strain your throat. Theater and choir performers learn this to help them be loud without damaging their voice, and having done choir as a teen those techniques really help me project as a teacher.
[ljwboik] (score 2, diepte 0) SAS shoes. I swear by them. Expensive but last forever and feels like walking on clouds.
[ljwiwgh] (score 2, diepte 0) I second the voice amplification systems.  Get a solid one for everyday use.  I’m talking a wireless headset like aerobic instructors use, and a small amplifier in the back of the room.  Get a backup one that has its own speaker (tour guide style) if the first one breaks or you are in a different room one day.  

Even if you have to pay for it out-of-pocket, it is worth its weight in gold as far as saving your voice over the long run.

Try New Balance or Dansko shoes.
[ljwon8x] (score 2, diepte 0) I sit a lot during the day during lessons on the rug. Do your kids sit at their desks all day?
[ljwovvn] (score 2, diepte 0) You might want to try light compression socks for the sore legs on days you wear pants. I like Vionic shoes and sandals for standing all day.
[ljx49mc] (score 2, diepte 0) As a runner (15-20 miles/week) and a HS teacher, the best shoes I had this year were puma platform sneakers- super cushy on the bottom. And adidas grand court alphas. They helped me through a running injury and kept me walking around my classroom all day.
(43 reacties met lagere score weggelaten)

