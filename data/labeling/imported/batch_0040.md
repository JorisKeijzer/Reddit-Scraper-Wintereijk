# Label-batch batch_0040

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
Schrijf het resultaat naar `batch_0040.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 100g0so, 8pliaw, zly2y8).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 100g0so ===
SUBREDDIT: r/BuyItForLife
DATUM: 2023-01-01  SCORE: 163  REACTIES: 175
TITEL: Best Men’s House Slippers
POST (source_id=post):
Looking for something durable that will last, that’s made from genuine materials instead of all this faux and plastic made crap products.

I personally like the slip-ons with an open heel aka “Scuffs” [(EXAMPLE)](https://imgur.com/a/GqcneqQ), instead of a traditional moccasin slippers, due to my feet getting too hot and sweating. 

I’ve been buying new slippers just about once every year, mostly due to the fact that the interior soles wear down to the point were any cushion is nonexistent, and you can’t really insert new soles due to this type of slipper. 

My budget is anything within $150, if it’s on Amazon that’s a bonus, since I have gift card credits, but if not, it’s not a big deal. I’m size 13 and USA based too if that makes a difference too.

Any help is appreciated, thanks.


*EDIT: Thinking about a BIFL slipper, it makes sense that the brand should have replacement insoles for sale, since this it’s likely to be needing replacement at some point, especially for sheepskin.*

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j2hkla2] (score 82, diepte 0) Geisswein. Their merino wool slippers are somehow warm and cool at the same time. I've been WFH now for 3 years and have lived in one pair the whole time. Not cheap, but I think they're great.
[j2i9ywx] (score 50, diepte 0) Glerups. That is all.
[j2hxbsw] (score 47, diepte 0) LL Bean Wicked Good Moccasins. I was in the same boat with the yearly slippers, these have been a godsend.
[j2hsu8o] (score 40, diepte 0) Birkenstock: https://www.birkenstock.com/us/zermatt-wool-felt/zermatt-cozyhomeshearling-woolfelt-0-latex-u_4369.html?dwvar_zermatt-cozyhomeshearling-woolfelt-0-latex-u__4369_size=300&region=US
The footbed is modified around your foot - and I haven't had an issue with wear, yet.
[j2hx2ww] (score 36, diepte 0) ive had a pair of ugg slippers for a couple years now with no signs of stopping. favorite slippers ive ever had.
[j2ib0wi] (score 16, diepte 0) I've had Glenrups for years and they are fantastic
[j2hm43k] (score 13, diepte 2) Soles are flat in mine - but I've only got the one pair so don't know about the rest of the range. I have the mens Veitsch. Insoles were fine - lasted me about a year and a bit (wearing them all day, every day pretty much) and have had to subsequently find my own ones. Customer service is excellent too, for what it's worth.
[j2hn2l8] (score 13, diepte 0) Someone already commented Olukai but adding my own comment rather than adding to theirs so they get two votes. Have had my pair for 4 years and got my FIL a pair 3 years ago and they are our wfh shoe for the whole time. No complaints and have been happy the whole time. Not sure what more you can ask for now a days from a brand
[j2i5equ] (score 12, diepte 1) My dad owned these all his life. He was a blue collar man who had few luxuries. This was one of them. Any time he wasn’t in work boots, he was wearing these.
[j2i7l31] (score 12, diepte 1) I’ve owned 4 pair of these. They’re great but they do wear out after a year or two.
[j2hlyz7] (score 10, diepte 1 OP) These look pretty good. How are the insoles? Do they have an arch or flat? Is it soft or hard? Which one do you recommend?
[j2i2omv] (score 9, diepte 0) UGGs, I've had my slippers for 14 years and they're perfect
[j2ihx6x] (score 8, diepte 2 OP) I pulled the trigger on them, they look super comfy.
[j2i3fkw] (score 8, diepte 0) I literally thought you were showing a pair of saddleback leather slippers and thought you would say, these slippers are BIFL. 

https://saddlebackleather.com/sheepskin-slippers-men/

I bought a pair for my father and another for a friend.
[j2ihl52] (score 8, diepte 1) Glerups, had mine for a few years now and they are great imo.  Leather soles.
[jw2hd4m] (score 7, diepte 4) any update on the saddleback
[j2icku1] (score 7, diepte 1) The uggs are so comfortable and durable
[j2i8jel] (score 7, diepte 2) Weird, I’ve had mine for 5 years and the only sign of wear they show are stains from spilling hot oil on them
[j2hlojd] (score 6, diepte 0) Olukai

Edit: One of their bonus features is the heel is designed to be intentionally crushed to use the slipper as a mule, or to pop up the heel when you want full warmth and less risk of the slipper coming off.
[j2hjca0] (score 5, diepte 0) Been wearing a pair of gecko man house shoes for just over a year. I don’t believe any footwear is BIFL but they have a hard sole, soft insole and are super comfortable around the house and provide good support. They’ve held up great. I usually wear a pair of Darn Tough socks to reduce moisture in them. 10/10 would recommend and will buy again. The ones I’m wearing have an open heel as you described
[j2iprrk] (score 5, diepte 1) I came here to say Giesswein too. Very warm, thick sole.
[j2if6go] (score 5, diepte 1) My wife got me a pair of these for Xmas, I was opposed to giving up my LLBean slippers but haven't taken these things off my feet yet. They are warm and very comfortable.
[j2ii1ga] (score 5, diepte 3) I just did too lol I had to
[j2iijl3] (score 5, diepte 4 OP) Haha awesome. I snagged these [ones](https://olukai.com/products/mua-ili-mens-leather-mule-slippers-dark-wood-silt?variant=39885104742499) too as a backup just in case, although I’m starting to realllly want these [ones](https://saddlebackleather.com/sheepskin-slippers-men/) instead, except their stupid website won’t let me select size 13!
[j2i8t5s] (score 5, diepte 3) Hah. Yeah all my fur rubbed off at the higher friction spots and the leather ~collapsed
[j2imggr] (score 5, diepte 1) Do you clean the inside? I love Uggs but generally get a new pair every year because they get janky as hell. Or maybe my feet are just nasty.
[j2if8r9] (score 4, diepte 1) How long have you had your pair? I’m really considering buying a pair from the website right now
[j2iq0aj] (score 4, diepte 2) They definitely run small to start as the wool pile takes up a lot of space. As the wool packs down over time they get true to size.
[j2iqqqz] (score 4, diepte 1) Uggs do eventually wear down - mine went after two or three years - but they're decent
[j2iht3x] (score 4, diepte 1) I second this. I have some great slippers but will happily switch when the opportunity presents itself
[j2ib3lp] (score 4, diepte 0) Haflingers
https://haflingerusa.com/collections/men
[j2ib28h] (score 3, diepte 2) I’ve had the Moloa since 2020 and recently grabbed the Mahana. 

They’re very comfy, and personally I like the versatility of being able to fold the back down and use it as a slide or have it with a back for better foot holding.

I will say that if you’re interested in buy it for life on any kind of shoe you really want a replaceable insoles. Olukai sells them for like $15 and you probably should replace them every year or two depending on how often you wear them. 

I found them to be on the wider side, but I usually wear them without socks.

I did learn that the bent back will wear out of its wool or cloth so if you want longevity I would lean towards a leather upper or at least a leather back (they used to offer a wool pair with leather back for this very reason.
[j2jzt6d] (score 3, diepte 2) I had a misstep (as in, stepped off a stair and my foot slid forward), and tore the seams of two diff pairs of ll bean slippers. They (as a brand) have gone so far downhill I'm surprised they are still in business.
[j2ijf5s] (score 3, diepte 6 OP) Exactly! Definitely an issue with their site. They give a 100year warranty on their leather which is damn impressive to back up too
[j2i0s75] (score 3, diepte 0) The Mulo slippers are proper BIFL stuff, especially the leather ones. They are actually most on 50% sale right now

https://www.muloshoes.com/mens-slippers/
[j2ihqeg] (score 3, diepte 0) Glerups are great, my mom has had a pair for 5+ years and when a small hole wore into the side, they replaced them with brand new slippers. I use the Sorel mens falcon ridge 2, had them for over 10 years and they basically look brand new save for a comfy imprint the shape of my foot. They are a bit warm though.
[j2ir9vt] (score 3, diepte 0) Glerups, no question. Get the ones with the rubber soles not the leather. They are incredible and worth every penny.
[j2is8z0] (score 3, diepte 0) Minnetonka

https://www.minnetonkamoccasin.com/men
[j2hiv93] (score 2, diepte 0) Bedroom Athletics. Shearling lined; Harris Tweed. Superb. Some patterns half price in their sale. Really nice slippers.
[j2hmbin] (score 2, diepte 3 OP) I was looking at the ILSFELD looks more like my style unfortunately they are sold out in my size. But that’s good to know you can replace the insoles on these. Do they sell them separately? Any other places might have them for sale?
[j2qjai5] (score 2, diepte 2) Mine have rubber soles, so are absolutely fine. Haven't got them soaked though, so don't know how the wool holds up if wet / if it reshapes or whatever.
[j2hu4ci] (score 2, diepte 1 OP) Wait you can pop up the heel? I was looking at this one (Mua 'Ili) and have no clue how that would be possibly just looking at the pictures. I didn’t read anything in its description either. Are you referring to the sandals?
[j2huf3y] (score 2, diepte 2) You're looking at a standard slide model. No heel.

The Moloā or Kīpuka Hulu have the optional heel design.
[j2hvz1s] (score 2, diepte 5 OP) Thanks for the help and feedback, I just bought a pair of the Mua ‘Illi & the Birckenstocks someone else mentioned below that sounded interesting and look cozy. I’ll have to compare and see how I like them anyways, who knows maybe in the end I’ll keep ‘em both! Glad I didn’t just go and buy some Ugg’s instead, those types of slippers just get demolished too fast.
[j2iixhq] (score 2, diepte 5) I was looking at those Olukai wool slippers but once I looked through all the suggestions and saw those Birkenstock ones I couldn’t pass those up they look too nice. I’m glad you made this post because I was telling myself a week or two ago I need new house slippers and I guess I just forgot and never thought about it again until I saw this post
[j2ij9rs] (score 2, diepte 6 OP) I’m super happy too, never knew there was so many great choices, I’ve been an Amazon ordering Slavs for too long! Time level up and get some slippers that actually last! My feet are killing me my slippers are so worn down it’s like I’m literally walking on wood floors with zero cushion! I can’t wait for these to get delivered. The Glerups looks pretty nice too.
[j2izdoc] (score 2, diepte 2) I’ve had mine for about 2 years, they’re great. The wool will stretch a little and the inner sole (which is removable with mine) will compress a bit, so order down in size instead of up (they are full sizes only). Great slippers.
[j2is8vn] (score 2, diepte 1) Happy cake day!
[j2iulzg] (score 2, diepte 1) LOVE my uggs. They have withstood so much and as the wool packed down I was able to add an arch support insole.
[j2iwhxj] (score 2, diepte 1) UGGS slippers 🫠🫠🫠 the best
[j2kz92g] (score 2, diepte 1) Thought I’d get flamed here for mentioning them, 3 years on mine as well I basically live in them at home 4-5 months of the year. Definitely bifl
[j3pg5py] (score 2, diepte 1 OP) Gotta say, so far I’ve bought the okulai and Birkenstock slippers and the Ugg scuff, only the Ugg’s are comfortable and returned the other two. Although they are nice, they are still pretty thin.
[j2ldi4y] (score 2, diepte 2) Do you have sweaty feet like me? If so; the key is baby powder. Every day when you first get them(for about a week) sprinkle some in. It’ll absorb the excess sweat and keep the sheepskin from matting. Then one a week thereafter should do the trick.
[j2jovy4] (score 2, diepte 1) First pair lasted 15-20 years. Same for second pair. But over the last 7 years I'm now on my 4th pair. They look the same, feel the same, but fall apart or wear out quickly. 
Unless the current pair lasts at least 10 years, they'll be my last.
[j2kfgp0] (score 2, diepte 1) Just got a pair for Christmas from the wife based on multiple recommendations on this subreddit.  They have been fantastic so far. The cheap $20 ones she’s gotten me in the past would’ve fallen apart by now.
[j2kvleo] (score 2, diepte 1) Had some of these as well but in Georgia they were just too darn hot. So I got a pair of the [LL Bean Leather Double-Sole Leather Lined Slipper](https://www.llbean.com/llb/shop/23723?page=mens-leather-double-sole-slippers-leather-lined&bc=474-629-503380&feat=503380-GN3&csp=f&pos=13) and haven't looked back. I'm in my 4th or 5th season with them and they go on my feet immediately when I get in the door from a long day. When wfh they stay on from the moment I wake/out of shower until I go to bed. If I ever need a replacement which seems unlikely, I'll go with the Bison leather version.
[j2i5rqx] (score 2, diepte 1 OP) Those look pretty nice, a bit more than I’m looking to spend, especially with shipping to USA and currency conversion. Gets pretty pricey.
[j3pgmzg] (score 2, diepte 1 OP) Well after trying out 2 other suggestions from this thread (Okulai & Birckenstocks) and they didn’t work out. I said screw it and pulled the trigger on getting these. Hope they are good, they look like it at least!
[j2kve4a] (score 2, diepte 4) I just put a little clothes detergent in them and used a small plastic brush on the interiors under the spout in the bathtub. Rinsed them out a few times and then air dried them. I did it thinking I may damage them, but it worked well. This was about a year ago. I wear mine with socks. I think they are 3-4 years old now. I bought a second pair at the time so I do not wear them every day anymore.
[j2i7psa] (score 2, diepte 2) They’re lovely. I’d advise going up a size since they seemed a little too snug when I tried my dad’s.


FYI, they have a 100 year warranty. Their slogan is “they’ll fight over it when you’re dead”. As bifl as you’re going to get I think.
[j2i9n5v] (score 2, diepte 4) I suppose I would call them to find out. 

I have 3 of their bags (2 backpacks and 1 travel duffel bag) all of which are holding up super well. I have no doubt I will NOT need replacements for at least two decades. 

They’re absolutely gorgeous - especially my front pocket tobacco colored backpack.

Here’s my post about it. 
https://www.reddit.com/r/BestGear/comments/m6rjgk/favorite_backpack/?utm_source=share&utm_medium=ios_app&utm_name=iossmf
[j2ia6qh] (score 2, diepte 5 OP) Looks like normal wear and tear is not covered unfortunately after reading more into it.
[j2id0w0] (score 2, diepte 3 OP) Yup I know that’s what I did, select color, and then try to select size. You can’t select 13 or 14, but all other sizes can be selected. Tried on a different browser as well.
[j2i4tuh] (score 2, diepte 0) [https://footskins.com/](https://footskins.com/)

&#x200B;

I've had a pair of Footskins deer skin w/ sheep interior slippers for 3 years and they feel as good as new and have zero signs of wear. Handmade in Colorado. Great company.
[j2i73rz] (score 2, diepte 0) Not exactly “slippers”, but I’ve been on the same quest and arrived at the oofos slides + darn tough socks combination after a lot of digging and considerations. This offers me really good comfort, support, cleanliness, and flexibility for hot/cold weather. I work from home so much that this is basically what I wear 90% of the time. I like that I can wear with and without socks because it can get really hot where I live. I hate slippers with any kind of fluff in them because they smell after a bit and give almost zero support. Added bonus is I just like the color and look of these slides (I have the beige ones). https://www.oofos.com/products/mens-sandal-ooahh-slide-black?variant=19099993989

Hope ya find what you’re looking for. I would go a size up if ya go with this option - these are pretty snug if you buy them true to size. Plus you need some room for socks. Lmk if ya have any questions.
[j2ihr9j] (score 2, diepte 1) Agreed. I love coming home and slipping them on
[j2jyjkz] (score 2, diepte 1) Will never buy anything else, they are so good!
[j2ilzow] (score 2, diepte 2) I also love Haflingers but they sure aren’t BIFL.
[j2io1ac] (score 2, diepte 2) Really?  Wow I’ve had mine for years…
[j2itbn3] (score 2, diepte 1) Love these. Have had four pairs - but they get a hole by the big toe within 6 months every time
[j2ikgj9] (score 2, diepte 0) Acorn socks
[j2ilhpc] (score 2, diepte 0) Garneau slippers made in Quebec, washable
[j2lrj2h] (score 2, diepte 1) I'm still on my first pair of lazybones \~17 years of indoor use/ taking out the trash, and will likely get a full 20 years out of them. Shearling upper and insoles, leather outsole that actually withstands outside use due to a thick layer of patina.

I would recommend choosing a dark colour to make stains blend in better, my dad also has them but always chose the light colour and would end up replacing them earlier because of how dirty they looked.

They sell replacement insoles, but charge a bit for shipping within Canada (not sure how much internationally), so just order multiple when the time comes.

Edit: because nobody has really mentioned it, I have stupid wide feet (6E) and these things have generous spacing.
[j2iotwy] (score 2, diepte 0) I've been there a few months ago. The only BIFL slippers seen to cost a good amount. Ended up getting lined crocs and so far they are awesome! Pro tip: size up if you like to wear thick socks in them.
[j2iplwf] (score 2, diepte 0) Teva ReEmber slippers are like sleeping bags for your feet, got my husband a pair three years ago that only get better.
[j2ivwok] (score 2, diepte 1 OP) Not really my style for at home since they have a backing, and I really like being able to slip in and out of em, however these look great to take on camping trip! Think I’ll buy one of these thanks!
[j2j7zws] (score 2, diepte 0) Baabuk Yves - they’re awesome. 

https://us.baabuk.com/products/yves-2019-dark-grey
[j2kn2tx] (score 2, diepte 0) I’m on year three of my Saddleback Leather slippers still got the liner and comfort. Solid leather all around I love em
[j2ldtzx] (score 2, diepte 0) Any recommendations for wide feet?
[kew0483] (score 2, diepte 1 OP) Glerups sucked, I absolutely hated them. Saddlebacks were definitely the best of all of the 10 or so slippers I tried. However **they run small so definitely order at least 1 size up**, and they never ended up getting a size 14 back in stock for over 6 months, so I just went with Ugg and they are my 2nd favorite which are still holding up with a machine wash every 1-2 months, that cleans the wool back to near new and fluffed.
(154 reacties met lagere score weggelaten)

=== THREAD 8pliaw ===
SUBREDDIT: r/Frugal
DATUM: 2018-06-08  SCORE: 7818  REACTIES: 174
TITEL: A little effort can save a lot of money! Got this stool for free and used one can of spray paint, discounted remnant fabric, and new rubber feet!
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e0c9874] (score 233, diepte 0) So pretty!  You did a great job.
[e0cdu0w] (score 219, diepte 1 OP) I got them from Menards for $1-2!  They were near the wheels. I found them while I was hunting for something else. Im sure any home repair store will carry them!
[e0cdpow] (score 215, diepte 0) Where did you find the rubber feet??
[e0c9asd] (score 116, diepte 1 OP) Thank you! :D I am very proud of it. I love saving other people's trash! :)
[e0cdi9s] (score 103, diepte 2) And people’s old farts. 

*“I reused the foam inside.”*
[e0cbtip] (score 76, diepte 0) r/Frugal shades over into r/Upcycling ...
[e0cdyw7] (score 69, diepte 3 OP) ( ͡° ͜ʖ ͡°)
[e0c9hr9] (score 60, diepte 1 OP) It isn't time wasted if you enjoy the process. :) Doing projects like this is relaxing and stress relieving for me. And this probably took an hour. Plus now I have something unique that I am proud of!
[e0c5i0d] (score 51, diepte 0) I can't be the only one who saw this.. https://imgur.com/a/hiqBjpX
[e0cdpxm] (score 51, diepte 0) I love what you did with it. Two questions what type of spray paint did you use? And where did you find the rubber feet? I have an old step stool that looks terrible.
[e0can2d] (score 45, diepte 2) The redditor has a little fetish for inanimate objects
[e0cc4rb] (score 44, diepte 1 OP) Just hoping to inspire other frugal people to try their hand at fixing up stuff before buying new and more pricey items. :)
[e0ckrl6] (score 44, diepte 0) Some people are being real jerks in this thread! I love it and I wish I had an eye for this kind of thing! I have a Goodwill a few blocks away and love little projects, but I have to have something in mind first (like something I saw on Pinterest). It would be so much easier if I could just see something and know what to do with it instead of having an idea and having to find the right objects to complete it lol. Nice job!
[e0ce0fk] (score 42, diepte 3 OP) Haha i was wondering if I'd confuse you with Menards. Its pretty much the same as Lowes and Home Depot!
[e0cj8xj] (score 38, diepte 0) Stool story bro
[e0cfr1v] (score 35, diepte 5 OP) Haha I actually wasn't going to, but then I randomly stumbled upon them while shopping and it was a no brainer! I didn't even realize you could buy replacement feet to be honest. And they were so cheap!
[e0cdw4k] (score 35, diepte 1 OP) I used Rust-Oleum! And I got the rubber feet from Menards for $1-2!  They were near the wheels/nuts/bolts/screws. I found them while I was hunting for something else. Im sure any home repair store will carry them!
[e0cdy8y] (score 34, diepte 2) Ok! I've never heard of Menards except that girl Sydney loofe who worked there :( I'm definitely gonna do this!
[e0cfoqw] (score 33, diepte 4) I would have never thought of replacing the "feet." You have a good eye for decor.
[e0cw4nv] (score 29, diepte 5) Save big money at menarrrrrds.

-girl from the midwest
[e0cpa5o] (score 28, diepte 1 OP) Just because you’re frugal doesn’t mean you can’t have nice things. I like to have nice things without breaking the bank. Frugal isn’t the same as cheap.
[e0c9hl6] (score 27, diepte 1) I don't get it....
[e0cg9f0] (score 27, diepte 0) Which one is the before and which is the after?
[e0c9bvp] (score 25, diepte 1 OP) Haha! Maybe I should have painted the legs yellow???
[e0cvr1d] (score 24, diepte 7) Makes me happy you two are so excited about feet for a stool.
[e0caa53] (score 22, diepte 2) What was the process of replacing the fabric like? If you don't mind. Also how dare you spend your own time doing productive hobbies that contribute to society /s
[e0cnnaa] (score 21, diepte 1 OP) Just because you’re frugal doesn’t mean you spend every minute of your life trying to make money. Every frugal person has their own reasons and goals behind being frugal. Mine is that I have more time and money to do the things I want to do rather than constantly struggling and trying to get more money.
[e0ca9du] (score 21, diepte 1 OP) I only took the seat off. Sprayed everything else. I haven't had any issues with it getting into joints. I spray paint lots of hinges and wheels and stuff and have no problems really. Im sure some got into the joints and rubbed away once I moved the legs, but it isn't visible! Im still figuring out this spray paint thing though haha. Ask me in a year how my projects have held up!
[e0d54vr] (score 20, diepte 1) 90% sure before to after is left to right, but if my wife found the current stool at goodwill she 100% would have gone the other way around lol
[e0d4put] (score 19, diepte 1) I guarantee you are the only one.
[e0cfhon] (score 19, diepte 1 OP) Yes the fabric of the cushion is different lol. Same foam on the inside but the replacement fabric does not have the ring of stitching.
[e0cpo2l] (score 18, diepte 3 OP) How is fixing something up instead of spending way more to buy a new one not frugal?
[e0ct3fy] (score 18, diepte 0) It’s uglier than before
[e0d4glg] (score 18, diepte 0) I kind of liked it better before...
[e0cfchp] (score 17, diepte 1 OP) Probably $10. This isn't a plastic stool. Its a metal, bar height, folding, cushioned (and customized) stool. :) I hope to use it for many many years to come!
[e0cr6fp] (score 17, diepte 0) Teal?
[e0cytcd] (score 17, diepte 0) I must say I do prefer the before, but what you did looks awesome. So colourful!
[e0cae5k] (score 16, diepte 3 OP) haha! I just had to pull out the staples under the seat that held the old fabric in place. I reused the foam that was inside.  Then I just stretched the new fabric around the seat and stapled in place! Lots of trial and error to get it to the right tightness.
[e0ca2gw] (score 16, diepte 0) Did you have to take it apart to paint it or does the spray paint not stick in the joints?
[e0cjo67] (score 16, diepte 1 OP) That is a good option for people working on saving for other things!
[e0cu81u] (score 16, diepte 1) It really is. Where he fuck would that even go? House has to be terribly decorated for it to fit anywhere.
[e0cvksd] (score 15, diepte 3) If you live near a Menard's and you have the radio on for any span of time, you'll know. The jingle will live in your head forever.

*Forever*
[e0cfa1d] (score 15, diepte 0) Am I tweaking? Those are two different cushions. Where's the ring of stitching around the top?
[e0cjf8k] (score 15, diepte 0) Thank you for showing this. I have two of these types of stools laying unused. I think I will dress them up now.
[e0ccc5m] (score 13, diepte 2) I'm with ya.  Compulsive upcycler here.
[e0cqpwi] (score 12, diepte 1) I'm the same; with cooking, crafts, most creative endeavors, I'm a copier not an innovator. It's pretty frustrating.
[e0cvp3u] (score 12, diepte 1 OP) I am happy with my 40 hr work week. I’m not offered overtime. And I like doing these projects for fun.  If I wasn’t doing this I would have been watching Netflix. This project only took me an hour.
[e0d0sdu] (score 12, diepte 2) Man, the fact that you have to defend yourself for making a super cute stool to all these jerks makes me really sad. The stool rocks and I think you rock.
[e0cargx] (score 11, diepte 0) That is cute as hell, and it looks like it was fun to do. Great job!
[e0cgqjy] (score 11, diepte 0) the white tips at the end look kinda odd... like an old person's walking cane. I would paint them the same color as the legs to give it a much more contemporary feel
[e0cwulo] (score 11, diepte 2) Lol I love how positive you manage to stay when responding to all these salty, bitter people on here. I don’t think I’d be able to. And your stool is super cute!
[e0cm71j] (score 11, diepte 0) Nice work. Looks boss! I recently re-painted my daughter's old toddler push car (pink to green) so my son would like it better, restrung a kid's electric guitar, and repaired and added training wheels to a bike. The guitar and bike I found in the trash. My kids love the stuff and I spent under $20 total on everything I mentioned.
[e0cvmo7] (score 11, diepte 1 OP) Yes I needed a stool. This isn’t poverty finance. I wanted a nice stool and found a cheap way to do it!
[e0d2i4m] (score 11, diepte 0) I'm gonna be honest, I love the fabric you used but I really *really* hate the paint colour. Those legs are painful to look at. As long as you're happy with it, though, that's what matters.
[e0d0hfw] (score 10, diepte 4) I love when some one else knows what Menards is! I live with three of their employees haha
[e0d0mvk] (score 10, diepte 1) Yes, we should all forgo aesthetics and live like paupers to save money.  
  
You’re confusing frugal with cheap.
[e0crtcx] (score 9, diepte 1) Maybe OP wanted a stool that looks like this, but it was more expensive than they were willing to shell out for it.
[e0caunt] (score 9, diepte 2) Thanks!  I haven't spray painted anything with moving parts, so wasn't sure how it would work out.
[e0cg1tz] (score 9, diepte 6) I wouldn't have even known where to look. Haha. I guess I do now!
[e0damqd] (score 9, diepte 1 OP) This is a hobby of mine that I do for fun while also saving money. If I wasn’t doing this, I would have just been watching tv. And I don’t think you could find a folding bar height stool that is unique and matches my style for that price.
[e0conde] (score 8, diepte 3) > “I reused the foam inside.”

For my new pillow.....
[e0d8sla] (score 8, diepte 3 OP) My time outside of work is not valued at anything besides what I want to be spending it doing. I work 40 hrs a week and that’s enough. I do not want to work more. Doing projects like this is fun and relaxing for me. If I wasn’t doing this I would have been watching tv which is way less productive.
[e0d1krf] (score 8, diepte 3 OP) I’ve learned that there will always be someone on Reddit who finds something wrong with your post lol. Even when I think there’s nothing to pick on, someone finds something! It’s a skill. Haha.
[e0d0ttu] (score 8, diepte 1) How dare people have purely decorative items in their homes
[e0ck3nd] (score 7, diepte 2) Do you have to sand off the previous layer? 

How did you do the seat cushion?
[e0cuju1] (score 7, diepte 2) You would think if they came from your own nards they would be free...

Seriously though nice job, that stool looks nice, especially compared to the before.  The picture order confused me a bit though.
[e0czgg1] (score 7, diepte 1) No one has mentioned it and not sure where you are located but big box home improvement stores- located in the hardware department with felt pads, furniture sliders, and rubber bumpers. They have different types of feet that nail, screw, stick, or just use suction.
[e0cf8sq] (score 7, diepte 0) How much it was all that?

I remember I lived for a while with patio furniture at home and one plastic stool costed me like $2.70.
[e0ci9km] (score 7, diepte 0) Ha. My grandma had that same stool.
[e0d0h5k] (score 7, diepte 2) Teal is a trendy color right now. That’s why.
[e0dcy8r] (score 7, diepte 2) This. I make artisan bread (actually all types of bread) and I will nurse the fuck out of a starter for 24 hours over buying a $1 loaf because to me it's fun!
[e0cfbo2] (score 6, diepte 3) Don't ruin my childhood Pat
[e0da07t] (score 6, diepte 2) I like it, this is true frugality. A lot of the other frugal subs are full of people who bought like 10 pairs of new shoes because they were on sale.
[e0cvwtl] (score 6, diepte 4) Gonna YouTube it. I need to know
[e0cvvve] (score 6, diepte 1) OP said they enjoy doing this type of thing. It was free time.
[e0cybqd] (score 6, diepte 1) There's also the less tangible benifit of reusing something that would have otherwise gone to waste.
[e0cz8mr] (score 6, diepte 1 OP) The frugal part is that I needed a stool and got this one for free. Instead of buying a new stool I fixed this one up and basically have a new stool for a fraction of the price! :D  I’m not frugal enough to be happy with a dirty stained and rusty stool, so this is a good compromise that still saved me money.
[e0d1l0v] (score 6, diepte 0) Bitch this is stunning
[e0cyneo] (score 5, diepte 1) Also r/buyitforlife.
[e0d033u] (score 5, diepte 2) I am located in Rhode island :) we have Lowe's and home Depot!
(95 reacties met lagere score weggelaten)

=== THREAD zly2y8 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2022-12-14  SCORE: 2803  REACTIES: 173
TITEL: Redback boots outlasted another pair of insoles. Five years of near-daily wear, harsh environments, and countless steps. Leather maintenance works wonders on quality products.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j07vz7n] (score 172, diepte 0) I love mine, I just wish they were resoleable.
[j07wby2] (score 117, diepte 0) sitting here in mine right now. about 4 years on mine, last year i swapped the insoles out for some orthopedic ones. i’m not a boots person but as an automotive tech i was going through tennis shoes every couple months so i bought them and they’ve way more than paid for themselves!
[j089ght] (score 63, diepte 2) They basically heat the outsole until it gets almost melted and then smush it against the upper so it’s bonded together
[j080kdg] (score 53, diepte 1 OP) I'm not there yet, but I didn't realize they weren't. Is it because of the glue versus stitching? I'm not a boot expert so I don't know what to look for.
[j091avj] (score 52, diepte 3) I had a pair of boots like this resoled once. There's a few specialty places that can manage it. 

They were a pair of relatively light weight hiking boots, you know foam mid-soles, lightweight materials except on the wear surfaces. 

They did a really good job with them, but they came back with a thick vibram full rubber sole, they just weren't the same, hardly wore em after because I didn't like the weight. Wasn't worth the effort in my opinion.
[j080vnf] (score 40, diepte 1 OP) That sounds like a good choice! Plus I bet they offer better protection. 

Mine have been through a brewery job, construction, and lots of travel. Definitely paid for themselves compared to other footwear.
[j08duul] (score 39, diepte 0) I have had two pairs of Red Back boots in my life, and I love them. The Chelsea style is so easy to slip on, yet they feel secure.  The soles are remarkable, and seem to last and last. Regular leather maintenance helps them look good. I've had Blundstones, but these are much more robust.  

One caution with the soles is that they are not super heat resistant. I was using a weed burner (roofing torch) on gravel. I walked on the hot gravel too soon afterwards and the gravel melted into the soles. Beware if you are using them in environments that can put hot stuff on the floor.
[j08fdx2] (score 35, diepte 2) It really depends on what you want.   Boots like these and blundstones use far more synthetics which means they are comfortable immediately.  And since most people only wear big cushioned shoes they aren't used to a more traditional boot.  That being one with little to no synthetics and also little cushion.   So a redwing Iron Ranger has a solid leather footbed with no insole unless you add one.    But this also means that those boots aren't as repairable if you need to replace a heel or a full resole like you can easily do on an iron ranger.

Synthetics and big cushioned shoes are really a more modern invention.    So what people call problems breaking in those types of boots is usually their feet just not being used to standing on a solid leather footbed with no cushioned insole.
[j080iz2] (score 33, diepte 1) Me too. On both counts.
[j0855gg] (score 33, diepte 0) Nearly 3 years on mine, soles are great, unfortunately I’m through to the steel on one of the toes though, should’ve bought the reinforced rubber toe guards. Comfiest work boots I've owned (industrial maintenance).
[j08f7zm] (score 31, diepte 1 OP) I just cleaned and oiled them a few days before this shot, so they look especially good right now!

I do take good care of them, but I try not to make it a burden. Basically, I clean them if they get pretty dirty, usually just with a damp cloth. A couple times a year (or more as needed), I oil them with mink oil. I use mink oil only because I have had a big tin of it for a decade—another product might be better, but mink oil works.

Also, I recently used dark brown fabric dye to touch up some worn patches on the toes that were much lighter in color and made the boots look old. The leather was in fine shape though, so I dyed them with a little paintbrush, buffed them with a rag, then re-oiled them. I was shocked at how well they turned out.
[j08hagy] (score 19, diepte 2 OP) Oh, and I should mention that I live in a very dry environment (Wyoming), and I store the boots indoors, so they dry out thoroughly every night. I have found that oiled, well cared for leather lasts a long time in arid environments since it doesn't suffer much organic breakdown. I've lived in humid places where fabric and leather seem to break down a bit more quickly, but maybe that's just my perception.
[j08ikj0] (score 16, diepte 4) You can! I’ve got a pair myself. Though be careful as some will smoosh your feet into the bottom of the inside of your boots.
[j08177i] (score 16, diepte 2) yep! my phone says i average about 10k steps a day when i’m working, by my calculation i’ve put 6+ millions steps in these!
[j0868kz] (score 16, diepte 0) My oldest pair started life in auto shops in '09.

I still have them.
[j08cmfi] (score 16, diepte 0) What‘s your maintenance routine? Those shoes look like you bought them yesterday.
[j08r3a8] (score 14, diepte 3 OP) I didn't—I had never heard of Redbacks, but was super tired of shitty boots, did some research, and sprung for them through an online shop. Once I knew what they were, I saw them everywhere!

Funny enough though, my brother-in-law runs a Matco truck and carries Redbacks now. My boots have been around longer than him :D but hopefully he outlasts them in the end!
[j08b11r] (score 14, diepte 1) I'm not sure if you've seen them, but you can buy generic rubber caps to glue on.  Not as good as the leather still being intact in the first place, but an option
[j08m1eh] (score 13, diepte 2) Did you buy yours off the tool truck like I did?
[j08dvx6] (score 12, diepte 1 OP) After the original insoles wore out, I've gone with Spenco insoles, specifically the [Polysorb Heavy Duty Insoles](https://www.spenco.com/comfort-insoles/polysorb-heavy-duty-insole.html). They're comfortable and relatively cheap, but I'm not necessarily saying they are the best ever—they do wear out. I haven't been in the mood to try anything else since they work well with these boots.
[j08f1xn] (score 11, diepte 2) Theres even better than that. Tuff toe.
[j080mox] (score 10, diepte 0) Much more comfortable than Blundstones IMO. More had on the sole, too.
[j09g4ga] (score 9, diepte 4) Then you lose the benefit of not having one all.  I feel that foot strength is something that is ignored.   We cushion when we should have less.   I personally dislike shoes with any cushion.   Even my running shoes are minimal for example.    Cushion can mask issues and increase problems.   So for me I would just rather have just the leather in there and nothing else.    You can add an insole but that can be difficult in an IR that tend to run more narrow and fitted to begin with.    For example I don’t think I could put even a thin insole in my IRs and still have them fit.
[j085vga] (score 9, diepte 0) Got a pair at the house that are about 7 years old that I use just for yard work. The ones on my feet are probably 3 years old. Only got them just to have a nicer looking pair. I work in the automotive industry as well! Sizing really threw me off when I first started buying, didn’t realize they were Australian sizes.
[j08hs9b] (score 8, diepte 3) Can you just whack a nice thick insole into an IR for the best of both worlds?
[j09b10i] (score 8, diepte 1) Check out Solovair, they have Chelsea boot. Goodyear welted so rebuildable and have a very comfortable sole. Used to be part of/formerly connected to Dr. Martens. Made in the UK.
[j08rjm4] (score 8, diepte 4) I put so many miles on those boots. Gravel asphalt concrete dirt, you name it. Barely any wear on the soles. Had them well over 10 years. Bought around 2001.
[j08gfn5] (score 7, diepte 1 OP) Good to know. I've never had to expose them to truly high temperatures, but I will keep that in mind to make sure they last!
[j0a8mdh] (score 7, diepte 1) Did something similar.. Burned a massive brush pile on a gravel parking lot.. Doing some overhaul the soles melted and picked up a ton of gravel.. Tossed the boots.. Learned a lesson.. Bought some more.
[j0924dk] (score 7, diepte 0) Love my Redbacks. Only had them a year but they have made the rest of my boots obsolete
[j08hiy9] (score 6, diepte 1) Agreed, I replaced my first pair because the heel wore out. I drag my feet and it wore through the rubber after several years.
[j08d28m] (score 6, diepte 1) I had the opposite experience with Redbacks. There was a seam or something in the area of my heel/Achilles tendon that drove me fucking nuts. As a result, mine languished at the back of my closet for several years until I finally donated them. 

I've had much better luck with Canada West Romeos.
[j08ktky] (score 6, diepte 0) I worked in a transmission shop when I finished high school back in 2000.  I had these boots.  Best boots I ever owned.  Same exact pair.
[j08s2eq] (score 6, diepte 1 OP) Yeah, very little footwear is truly buy it for life, but it would help if you could re-sole them. Pretty sure a cobbler would replace the elastic if that was a deal-breaker for continuing to wear them, but my pants cover the elastic and they still fit snug.

I think they are super durable as far as boots go, especially for the price. Mine are five years old, and the sole still has a lot of life left, but some folks are certainly even harder on them than me.

In my opinion, boots fall under the part of the rules that says, "Products that are well-made and durable (even if they won't last an lifetime) are accepted."
[j08io7a] (score 5, diepte 5) Good stuff thanks! I’ll bear that in mind when my Blundstones wear out
[j08n6ch] (score 5, diepte 2) Yeah cemented sole. Simply wasnt designed to be replaced.
[j08iw1e] (score 5, diepte 1) There is a couple of places that offer a resole, but for the price you could add $40 to $50 and just get a new pair off ebay directly from Austrailia.

I'm sitting at work in my 4th pair.
[j0a4q56] (score 5, diepte 2) I think those are more dressy, not work boots. Check out Jim Green stockman model (stitchdown construction).
[j0a98cy] (score 5, diepte 2) I hate that seam.. Wore a bunch of holes in my socks until switched to darn tough socks for daily wear..
[j08biln] (score 5, diepte 0) What brand insole?
[j08f5fc] (score 5, diepte 1) This. Please answer
[j08uh4y] (score 4, diepte 1) Isn’t this why so many in this sub recommend redwing?
[j0915hm] (score 4, diepte 4) Got to get that sweet family discount on the next pair!
[j08thoq] (score 4, diepte 2) Shocked they lived through brewery chemicals, iv had "chemical rated" leather boots fail within a year. Even rubber boots were only good for about a year before they cracked. 

The best boots that I have ever owned were redwing steel toe chemical resistant boots.
[j08ei1x] (score 4, diepte 0) Replacing insoles adds years to my shoes’ life
[j08pkra] (score 4, diepte 0) Not at all Buy It For Life. Not only can you not get new soles on them, but the elastic gets blown out after some time. I use them as my work boots, they’re the most comfortable boot I’ve ever had, but in no way are they “for life”. Three years and the sole is done.
[j09hrrk] (score 4, diepte 1) Here is a video I think you may enjoy!

https://youtu.be/hqwbBpcElpE
[j0a6q9n] (score 3, diepte 6) If you're planning on using them with a big insole, make sure you take that into consideration when you're getting sized for your boots.
[j09d7hg] (score 3, diepte 1) Get some Georgia boot Romeo's. Very similar boot, but they have a Goodyear welt.
[j09oade] (score 3, diepte 5) yea i also recommend buying quality leather creams or oils or shines and regularly applying them to you valued leather shoes/boots. Does wonders. 10+ years is definitely possible on quality leathers.

yup for my office shoes, i regularly apply polish etc, and also get them reheeled regularly. saves a lot, since each new purchase is $300+.

anybody know if caterpillar workmen boots are worthwhile?
[j099sax] (score 3, diepte 5 OP) Better believe it!
[j08ww8w] (score 3, diepte 3 OP) Yeah, I was brewing at a really tiny brewery, so our processes weren't as industrial. These boots saw some splashes and chemicals, but nothing like a big production brewery. Like we just used PBW rather than sodium hydroxide, etc.
[j08qe0c] (score 3, diepte 2) Ah, yes. Mine rubbed a bit at first but they eventually wore in. The soles are more springy than Blundstones, though.
[j09w1zu] (score 3, diepte 1) I’d love to check these out, but my Blundstones are on year 5 and my in-laws gifted me another pair last year
[j081nsj] (score 3, diepte 0) Timberland makes really comfortable insoles. Sometimes they go on sale for under $20 on their site
[j087ph8] (score 3, diepte 0) I have a pair , are they suppose to be roomy in the feet area ?
[j08fteh] (score 3, diepte 1 OP) As in wide? I don't know, mine fit great and I don't have particularly wide feet. I wear medium-thick socks with them. I definitely wouldn't describe them as narrow, but for me that's a good thing—more comfortable. I use them for working, travel, and casual wear, but not anything aggressive or athletic like hiking. They might feel too loose or roomy for that.
[j088wv6] (score 3, diepte 0) I have worn mine daily for around seven years, and they still look fairly new. I'm on like the 5th set of insoles.
[j0a00z9] (score 3, diepte 2) Spenco insoles are the best I’ve ever used.
[j08li68] (score 3, diepte 0) How is the tread wear? I had mine for about 8 years and the heel wore down enough to cause me to have knee pain. I was unable to find a local cobbler that would resole them for me, but I figured I had definitely gotten my money’s worth from the boots, so I just got a new pair.
[j08qe63] (score 3, diepte 1 OP) The tread seems to be wearing really well for me, and definitely still life in them after five years. New insoles help a lot with the comfort and joint pain, or lack thereof!
[j08mr5x] (score 3, diepte 0) Wow.  Bought a pair of these off my Matco tool guy 20 years ago. Not sure I still have them or not. Haven’t been a service tech in 10 years. Now everybody wears these. I remember seeing young people wearing these several years ago and thinking it was odd they’d wear the same type boots I bought off my tool guy. Lol. I was a trend setter. My wife has some blundstones or whatever they’re called. Still seems funny.
[j09b7cr] (score 3, diepte 2) That’s why I asked!  They look very similar but look like they could also take a bit more of a rugged lifestyle.
[j090s8k] (score 3, diepte 0) I bought a pair of these in 1999 in Australia and bought them back with me to the US. Loved them. Cannot remember how many years I wore them. I hung onto them after I stopped wearing them. One day I was sad to discover the soles had perished and were crumbling. Probably should have looked into getting them resoled. Good to know they are still being made.
[j0954v7] (score 3, diepte 0) I vouch for this boot, I’ve repurchased them over and over because Nothing else comes close

For insoles I recommend Keen’s K20 insoles
[j098l4b] (score 3, diepte 0) Way better than blundstones
[j099ugn] (score 3, diepte 2) Ya, I do have weird feet. I almost feel like the pair I have is messed up or something. The seam on the inside where the leather meets feels just like a razorblade after wearing them for a couple months.
[j09th9a] (score 3, diepte 3) Hmm I have a similar situation. They are very comfortable when walking around all day but if sitting for a few hours I have pain in the exact same spot. Just kind of accepted it’s the angle of my foot sitting down and perhaps I have a high arch. Still love the boots and wear them all the time! Redback support were very nice though! 👍
[j09w9xt] (score 3, diepte 1) Same here - I have small feet (size 6.5)and these would pinch the nerves on top of my feet. Seems like they don't adjust the toe cap length to account for a shorter foot
[j09xm9j] (score 3, diepte 0) Every boot/sneaker/shoe I’ve ever had, the back wears out and starts digging into my Achilles and gives me blisters. Anyone know why this happens, or shoes/boots that don’t have that piece that’ll dig into me but aren’t floppy above the ankle? 

  I’m sick of wearing out a pair of timberland boots in less than a year, and buying sneakers all the time for the same issue. I don’t like the shoes that are a thin piece of fabric that gets soaked thru in the rain, but they don’t have the same issue since their flimsy above the ankle on high tops (which I don’t like). Are there any shoes/boots like I’m looking for that also have support around the ankle?
[j0a182r] (score 3, diepte 0) Wore these almost everyday this past year. Traveled to 22 countries walked through snow, mountains, beaches, cities.... They still look good and feel great 420/10
[j0a4v9z] (score 3, diepte 0) I grew up next door to the family who owns the Redback's US distribution operation. Been wearing them most of my life. These are awesome boots, especially for travel, but not really BIFL due to the heel not being replaceable. I usually wear through the very back edge of the heel long before any other visible wear on the boots. A few years of daily wear is still awesome for any boot
[j08xxaw] (score 2, diepte 4) That makes sense. I used to go through a pair of rubber boots every year. Until I got those redwings. 

I'm currently at a nano and I haven't put on the big ass boots since I got my grundie deck boots(basically like your redbacks, but all rubber).
[j0cjh03] (score 2, diepte 2) i think it depends on the place you work and what they require, but most guys don’t seem to care about personal safety from what i’ve seen in this industry. i’ve never had anything fall on my feet, i’ve only known one person that had something fall on their foot and they were wearing steel toes. i got these cuz they were better protecting than tennis shoes
[j083ug1] (score 2, diepte 1 OP) How's the durability? I like the Spenco ones pictured, especially for comfort and cost, but they aren't terribly long lasting.
[j0866xh] (score 2, diepte 2) Not sure, I’ll tell you in a few years lol
[j09iree] (score 2, diepte 2) Thank you for the reply
[j0bn6pj] (score 2, diepte 1) they should be snug across the instep and heel and roomy in the toe box
[j0cfpud] (score 2, diepte 1) I also know that Blundstone's soles are not heat resistant. A friend had their feet too close to a camp fire and the soles melted in the toe area.
[j097r1v] (score 2, diepte 2) That is awesome!
(106 reacties met lagere score weggelaten)

