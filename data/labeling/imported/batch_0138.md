# Label-batch batch_0138

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
Schrijf het resultaat naar `batch_0138.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: tz2o15, 1tcftsk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD tz2o15 ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2022-04-08  SCORE: 15  REACTIES: 63
TITEL: Kitchen workers, we are on our feet all day! What do you do to take care of your feet?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i3wi9f0] (score 67, diepte 0) When I get home, I drink until they don't hurt anymore.
[i3w74nf] (score 44, diepte 0) Literally nothing.
[i3w6sqt] (score 19, diepte 0) Invest in high quality shoes and socks, have a couple pair/styles and alternate wearing them, also work mats help a lot if you are stationary
[i3wn0xa] (score 10, diepte 0) Percocet
[i3wnte2] (score 9, diepte 0) Water and oil-resistans shoes with dampening/cushioning, like SFC or Keuka.

Dont skimp on the stuff between you and the ground. Good shoes, good mattress, and good tires (if you got a car)
[i3wz3it] (score 9, diepte 0) Compression socks! I even have extra wide new balance non slips with insoles but getting compressions socks really changed the game for me
[i3w7nzn] (score 7, diepte 0) I put toxins in my body that manifest into smells from my feet. It keeps my feet happy and my aspirations low. Love my job
[i3wv1uq] (score 7, diepte 0) Quality shoes and socks.  Go to a reputable footwear shop and get something specifically designed for your needs and your feet.  

It’s an investment that pays dividends in about a week.
[i3x0309] (score 6, diepte 0) Caffeine and cigarettes.
[i3wa72u] (score 5, diepte 0) Epson Salt soak, lotion + sock before bed. I wear alternating pairs bistro + birks + vans for makers?
[i3wx654] (score 5, diepte 0) Orthotics. Not only fixed my foot pain, but over time my knee and hip pain
[i3xf9sd] (score 4, diepte 1) Came to say exactly the same thing 🤣
But some times if it's been a particularly feet and soul destroying day, I don't make it all the way home and have to find a dive bar to drink in first before attempting the trip home 🍻🍻🍻🍻🍻🍻🍻🍻🍻🍻🍻🍻
[i3x36u3] (score 4, diepte 0) Change your shoes and socks half way through your shift. 2 different pairs that support your feet differently.
[i3xc9uu] (score 4, diepte 0) Use a ball between the bottom of your feet and the floor to give them a good massage. Something firm, but with a little give. Lacrosse balls are the best in my experience, but I've used golf balls (tend to be too hard) and tennis balls (tend to be too soft).
[i3wpban] (score 3, diepte 1) Vans for Makers fucked up my feet pretty bad. Podiatrist I went told me they were bad without even knowing that's what I'd been wearing.
[i3wcji0] (score 3, diepte 0) Try a Thai foot massage if there's any places near you.
[i3xbewl] (score 3, diepte 0) wear good quality socks and shoes. 

take all that off as soon as i get home.
[i3xpudg] (score 3, diepte 0) Ideally, stretches. I had crippling plantar fasciitis and nothing worked to cure it but regular stretching, before and after work.
[i3xqcyy] (score 3, diepte 0) Worry about rent
[i4r7bj6] (score 2, diepte 1 OP) Yes, the alternating shoes has helped a lot. Each shoe hurts a little different and in a different place so I spread the damage. It has helped overall.
My pedi egg is my friend also.
[i3y3za2] (score 2, diepte 1) That def works.. until it doesnt. Then your whole life will be pain not just in your feets.
[i40t5cl] (score 2, diepte 1) I started wearing them along with ankle socks and my feet feel so much better.
[i3x8jl8] (score 2, diepte 0) Go home and sit in one place smoking my pipe till it's time to take the dog out and go to bed. The upside is the dog lays on me as I sit. The downside is I'm fat and do myself no favors not staying active.
[i3xbptk] (score 2, diepte 0) Go for a run because my brain needs it
[i3xdbna] (score 2, diepte 0) I stretch my toes every day and lacrosse ball massage for the arches while I’m sitting on the couch
[i3xe18e] (score 2, diepte 0) Submerge them in a bucket or bowl of ice water. It's unnerving the first couple of seconds but it takes the aches, pain, and swelling away every time.
[i3xn6jc] (score 2, diepte 0) Smoke weed and drink!
[i4owyy9] (score 2, diepte 1 OP) Hmmmm......BBQ......(Homer Simpson voice)
[i3wqcst] (score 1, diepte 2) Crocs selling point is its podiatrist trusted yet some don’t recommend it. There are some who also try to peddle their customs. It boils down to your own feet comfort.
[i3xkm0u] (score 1, diepte 1) I either start my day with Epson salts or finish my day with them.. sometimes both.
[i3x33jq] (score 1, diepte 0) Nothing besides a squishy mat at work and then a recliner at home.
[i3x4g1h] (score 1, diepte 0) Hiking. Shoes.
[i4r6sjp] (score 1, diepte 1 OP) Sounds like my routine.
[i3xanvs] (score 1, diepte 0) I paint my toenails with my daughter to cover up the bad toenails, then hope I can walk when I’m 50.
[i3xdppo] (score 1, diepte 0) my place doesn’t require no slips cuz they have rubber mats over the floors. i wear trail runners cuz they have wider base with the thick foam and very breathable
[i4r65uj] (score 1, diepte 1 OP) I wish. Black pants, white jacket, white toque, apron, non slip shoes, black.
[i4r5p1w] (score 1, diepte 1 OP) You are a better man than me. Lol!
[i4r65i5] (score 1, diepte 2) I'm a big dude, 235ish pounds so the feet pains are always a real problem. This may suck real bad but it makes my feet feel fantastic afterwards.
[i4r6gx5] (score 1, diepte 3 OP) I'm 250. Still not doing the ice bucket challenge. Lol
Had a sprained ankle years ago. I tried the ice bucket and .....no.
[i3xipa3] (score 1, diepte 0) I spent 5 years in the army.  I was taught to change your socks often, make sure your shoes fit properly and don't fuck with your calluses.  I haven't had any problems since i started doing these things.
[i4r5hpi] (score 1, diepte 1 OP) I keep my feet clean and nails trim but I absolutely fuck with my calluses. Under calluses is where I hurt the most. Taking them down with a pedi egg keeps me pain free.
Of course you can take it too far and have tender feet. Got to wait for skin to toughen up then. Balancing act.
[i4tluvj] (score 1, diepte 2) Well, you gotta do what works for you.  I know guys who started taking down their calluses and it made their problems worse, but if it helps you do it. Personally, I never touch mine. My feet look gross but I never have foot pain.  Different strokes for different folks.
[i3xpi3u] (score 1, diepte 0) I had a sore foot for over a year when I was a line cook.  Thought it was just normal everyday being on my feet pain.  My gf at the time took a closer look and ended up pulling out a 1/2 " piece of steel wool that had been embedded into my foot that long.  Guess it fell off into my shoe one time while cleaning.  Seriously, don't buy Wal-Mart shoes, invest in something comfortable and durable.  I paid almost 150 for Birkenstocks back in my day and would last me 2-3 years.  Bring backup socks/shoes to work to change into after shift if you go out.  Don't want your feet being soggy all night.
[i3xrr8u] (score 1, diepte 0) Mucho Mota before bed
[i3xs5wb] (score 1, diepte 0) Form fitted inserts for my work shoes, sturdy non slip boots cause they have the best support for me, good cotton socks, peroxide after a shower to cut down on any infections
[i3xsdxm] (score 1, diepte 0) Doc martins and a good pair of insoles.  Well maintained that can give you at least 5 years of painless standing.
[i4ox4pn] (score 1, diepte 1 OP) I've been that route. Happy it has worked for you.
Me, not so much.
[i3xtu8z] (score 1, diepte 0) Pedicures and soaking in Epsom salt when my feet ache really bad.
[i4owubv] (score 1, diepte 1 OP) Really should get myself a pedicure. I keep threatening.....
[i4pora3] (score 1, diepte 2) You should. It's so relaxing!
[i3y1opu] (score 1, diepte 0) Danskos….although, my feet have been hurting lately…maybe I need a better pair of shoes? That and yoga after work! Stretching and lacrosse ball on the feet.
[i4owq9e] (score 1, diepte 1 OP) In the quest for the perfect kitchen shoe I have wound up with several different pair. All seem to hurt in different ways. So I have been rotating them almost daily. It has helped. Also my pedi egg.
[i3y54w1] (score 1, diepte 0) The feet never get to me but, my upper back starts killing me so bad after a week.  I don’t know what to do about it
[i4owapt] (score 1, diepte 1 OP) Are you stuck at one station or can you move around? I am a prep cook and can move around a big kitchen for my primary job (5 day a week) and then a tiny kitchen at my 2nd job.
At my second job there is no room to move. My back starts to ache then.
Peeling shrimp seems to be what hurts my back the most.
[i4pzh9j] (score 1, diepte 2) We have a small kitchen and I move between the line, the prep station and the dish pit.  Everywhere is just kind of under my height threshold.  I am not super tall or anything, only around 6’2, but, everything in this place is built for short folk it seems.  So, I have to spend too much of my time hunched over to reach everything
[i3y5rpf] (score 1, diepte 0) I go to Jones' Good Ass BBQ and foot massage of course
[i3y9vs3] (score 1, diepte 0) I don't.
[i3yj57q] (score 1, diepte 0) Get them massaged once a week by a foot massager.
[i3ykdsb] (score 1, diepte 0) Burkenstock crocs, i moisturize my feet and I run to help build the muscles for stanging
[i3yw7bc] (score 1, diepte 0) Shoes are the key for me, Birkenstocks or crocs bistro(no holes) are comfortable for me. I asked my doctor about swelling and she recommended compression socks I use them on long days where I’m going to be running around a lot. They do help.
[jx2loct] (score 1, diepte 1) What kind of birkenstocks
[jx36ufb] (score 1, diepte 2) I had the Tokyo and the super birki, I liked the Tokyo better. I have a wide foot they fit me better. I like the Croc bistro better than both of them.
[i3z5wmd] (score 1, diepte 0) Red wing boots and a little plug in foot hot tub
[i4r7h0f] (score 1, diepte 0 OP) There is an Asian Spa....

=== THREAD 1tcftsk ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2026-05-13  SCORE: 26  REACTIES: 63
TITEL: Got any tips for dealing with plantar Fasciitis on while on the job?
POST (source_id=post):
In the last 5ish years I’ve been managing pain with the holy trinity of aleve Tylenol and rest but I was wondering if yall had any tips on what shoes to wear or any remedies that work for you. I do have an appointment to see a specialist in a few months. Thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[olnxgr7] (score 27, diepte 0) Stretch, Massage, and search this sub for that topic. And of course, hydrate.
[olntizd] (score 22, diepte 0) I limped around for a couple years coping w advil, aleve, & booze.   I knew I had to give my liver a break so I stopped the pills & bought some damn crocs.  They helped but the problem wasn’t solved until I bought proper all leather boots with proper arch support.  Some cushioned merino wool socks too.  16-18 hour days weren’t a problem after that.  Search for Pacific Northwest boots.  It’s a big investment that’s only getting more ridiculously expensive nowadays — but it really worked for me.  There’s plenty of stuff available secondhand that’s lightly worn if you don’t mind going used.  Theres also nice Father’s Day sales around the corner as well.  Good luck & hope you get it sorted, pain sucks!
[olo5gyi] (score 14, diepte 0) https://preview.redd.it/j374x4x7yz0h1.jpeg?width=724&format=pjpg&auto=webp&s=b7548c52d528b99dae334fab3beffab17944b8c0

Buy these at CVS and learn how to wear them. Wear them daily and it will eventually heal.

Then get some shoes like Hoka Bondi SR.

I’ve had bad plantar fasciitis twice. Both times from bad shoes. Both times cured by the sleeves. I’ve never had it in the 7 years since I switched to the Hoka shoes.
[olnxioc] (score 11, diepte 1) Merino wool is good, helps regulate temp…wool doesn’t make you warm, heavy wool makes you warm. Natural wicking material…the catch is finding the one like smart wool that bands it in the arch area, they make it tighter under your arch and wraps over the foot iykyk
[olnwytt] (score 9, diepte 0) Always wear shoes, stretch in the morning…golf ball under the feet either before or after bed. Arch support. Super feet (plastic not cushion, you need support not quick sand). Halflingers at home, cork based slipper, Birkenstocks, Naot, hell, even Ariat with a proper shank. The more you can fold a shoe the less structure it has (bad). Get a hoka or SAS freedom and throw a green superfeet in. Cork won’t work in restaurants, wet cork breaks down.

Cook/chef/operator/manager also certified shoe fitter by the American pedorthic association
[olo1yv7] (score 7, diepte 0) I have extremely flat feet and need ankle boots to help stabilize my ankles otherwise plantar fasciitis seeps in very quickly. I wear red wing boots and use their insoles because the price tag has been worth it every time for the last 15 years for me. Aside from that, I have a massage thing that sits on the ground and has heavy metal balls facing upwards which I grind my feet on to break up the fascia. You can also use a golf ball like others have mentioned. Painful, but effective. Ultimately for me it’s always been about buying new insoles routinely (every 6 months or so) which I’m terrible about.
[olo4iu6] (score 7, diepte 0) Stretch, stretch, stretch. Then stretch some more. 

I like to put my foot against the wall and lean in
[olnytck] (score 6, diepte 1) Hokas with Superfeet for the win!  This combo has saved my LIFE. 🙌🏻🙌🏻
[olp6s0h] (score 6, diepte 1) This. I had pain for years and after stretching for a month it went away,
[olom79d] (score 6, diepte 1) https://preview.redd.it/65kltylqe01h1.jpeg?width=300&format=pjpg&auto=webp&s=75a6fcdd82be9335b1753044ac0ef695b2bca6b1

This “cross legged IT band stretch” - had plantar fasciitis for years and somebody showed me this, I did it every twenty minutes at work, it was gone within the week. Couldn’t believe it. Helps if you roll the ankle of the back leg so the big toe is up and pinky toe down. Should feel it from your heel to your hip along the outside of the rear leg.
[olnrf2v] (score 5, diepte 0) How you walk and how you stand may be some of the problem. Over use and bag shoes didn't help. A lot of it probably comes down to how many hours you are on your feet also.
[olo2us3] (score 5, diepte 0) You really have to do a lot of work at home, in terms of stretching, massages, toe pulls, and different exercises. 

Lots of great info online if you Google it, including YouTube videos. 

Footwear will help to prevent it, but they won't solve it.

Magnesium glycinate helps as well.

I hope this helps, good luck.
[olns0re] (score 4, diepte 0) Using [**Leukotape**](https://a.co/d/09NOuWr5) on my heel has been really helpful
[olojb7r] (score 4, diepte 3) Socks are wet, but your feet aren’t…that’s wicking…that’s wool. Also, Duluth is the Carhartt of Minnesota. I fux w/ them.
[olo8f5a] (score 4, diepte 0) Jumping jacks. I am not kidding. I had horrible plantar fasciitis for years and almost had to give up my career because of it. None of the stretches or massages helped. I started doing jumping jacks and got up to like a 100 a day. My goal was fitness, but it also fixed my feet. I think it strengthened my arch muscles a shit ton so my tendons weren’t under strain.
[olnsqbn] (score 3, diepte 0) Im flat(ish) footed, so I tape my arches up.
[olohss1] (score 3, diepte 2) I've been rocking some Duluth wool socks for a minute now, they add a little extra padding and when they get damp the socks are wet but not my toes if that makes sense. They are like 20 bucks a pair but have sales all the time.
[olo6i0q] (score 3, diepte 1) I can guarantee you that PF CAN be fixed very quickly.  I was a marathon runner with it and after ditching all my custom orthotics and simply switching my neutral running shoes fixed mine. I felt no more pain in less than a week.  It won’t work on everyone but it can happen quickly.
[oloig71] (score 3, diepte 2) 100%. You can also buy those green balls with knobs that break up your feet. Cold bottle is cost effective cause it’s reusable, achieves the method of rolling under your arch, and the coldness has muscle recovery features.
[olnx9ji] (score 3, diepte 0) I fucked off crocs, birkenstocks, all the kitchen shoe regular suspects and went for non slip toe capped builders boots which allow the perfect space for custom made insoles from a podiatry specialist. The generic flat foot/plantar insoles are generally crap and can even damage your situation further as everyone's feet are different.
[olr5bag] (score 3, diepte 1) And lots of calf raises with declination on a curb.  I nearly wanted to cut my feet off.  Now I do probably 100 a day and really try to stretch my calves and it’s really helped
[olo7zui] (score 3, diepte 0) I have to rotate shoes more often. If I wear the same pair of shoes every day, I’m busted. Make sure your shoes actually fit in length and width and arch support. Even the $15 Dr. Scholls inserts can make a big difference, but you have to replace them more often.
[olo7zrv] (score 3, diepte 0) I went to PT for one foot being fucked and he showed me several different exercises most of them were raising my toes up and rotating my ankle in a circle 10x in both directions then repeat while making a fist with my foot. 

Calf stretches

Using a resistance band to push my foot down 

I started uphill hiking as well to strengthening my ankles as well. 

It just came back on my other foot after 5 years and I just got the axis board 2.0 in the mail today to see if I can strengthen my ankle quicker at home without the hiking.
[olo9dzt] (score 3, diepte 0) I got rid of plantar completely by switching to zero drop barefoot shoes when not on the clock (vivos). Now rocking the Birkenstock tokios on the clock. I retrained my feet how to properly walk and strengthened muscles and that's after losing 200ish lbs. It's something you have to ease into, but it's completely changed my life.
[oloaslx] (score 3, diepte 0) Hoka and physical therapy helped me.
[olof06s] (score 2, diepte 1) Rather than the golf ball I use a frozen water bottle. Roll your arch over it, the cold helps if you have any swelling.
[olnzgtk] (score 2, diepte 0) the rubz massage ball saved me. i run too, but it made my symptoms disappear entirely. feels pretty good after 12 hours on your feet, too.
[olo8wjs] (score 2, diepte 0) Kuru is good for plantar fasciitis and they have a good kitchen shoe
[olob4dz] (score 2, diepte 0) Superfeet insoles saved my life. 
Go get fit for the green ones
[olodt4x] (score 2, diepte 0) I’ve dealt with it on and off for a couple decades. I have to have good, supportive shoes and I can basically never walk around barefoot. If my insoles get old and I don’t buy new shoes soon enough it flares up like clockwork. It’s worth experimenting to see what shoes you like best. I tried a pair of Hokas a year or two ago and I’m a convert.
[olodzy8] (score 2, diepte 0) Get "wide" shoes
[oloe2i7] (score 2, diepte 0) Proper footwear and changing my insoles at least every 6 months.  I prefer Blundstones, my feet get pissed when I need to wear anything else
[oloem0o] (score 2, diepte 0) Go to the American Podiatrist Association (or whatever it’s called). They have shoe recommendations with different price points, etc. This helped me so much (plus some weight loss) that I don’t have PF anymore
[olof3ld] (score 2, diepte 0) Expensive prescription orthotics.  Costs about $800 and they last a year with heavy use. Worth every penny to me. Helps alieviate my back pain as well.
[olof7p6] (score 2, diepte 0) Stretch your calves.  Completely fixed my PF.
[olofo5c] (score 2, diepte 0) I had it in both feet. I also used to work for a podiatrist. Stretch the tendon before you get out of bed and while you're sitting for long periods. Get custom orthotics from the podiatrist. You can get over the counter ones for now if you want. You'll need shoes with a deep foot well. I used New Balance because I could take out the insoles and replace them with the orthotics. Wear them religiously. The DPM can give you a cortisone shot that can help if you want one. I wore my orthotics for about 4 years. I've been fine without them for about 10 years now. In the meantime, forget about flip flops, heels (if you wear them), and sandals. Although the Ecco sandals were supportive enough to wear. Basically you need shoes with good arch support.
[ologabz] (score 2, diepte 0) Arch support all the way!  Vionic shoes have been a godsend!  But also that seated-bent-knee-toes-pulled-back stretch!
[olognk3] (score 2, diepte 0) Frozen water bottles, compression socks, and my personal fave, the plastic dryer balls with dimples on them from the grocery store. You want to break up all that built up tissue. Footbeds are very important. Superfeet makes one called Powersteps. Red Wing shoes sell them, and they have a 30 day customer satisfaction policy.
[oloh5r2] (score 2, diepte 0) Arch support - look into physical therapists
[oloi2p5] (score 2, diepte 0) Do you sleep on your stomach? I do, and I've noticed a drastic reduction in heel pain by sleeping with a small pillow under my ankle, so that the leg and foot aren't hyperextended fully straight all night and so the tendon going up the leg isn't fully slack.
[olojosx] (score 2, diepte 0) I'd switch to ibuprofen... especially if you drink. Look up plantar fascists stretches. For when you get home, put a water bottle in the freezer. Take it out when you get home and roll your feet over it. You're welcome.
[olon2ey] (score 2, diepte 0) In terms of work shoes the hoka bondi sr have been a life saver. For 2 years in my regular life I exclusively wore brooks ghost 16s, and asics gel kayano 30s. The hokas and brooks I wear with a regular drug store plantar fasciitis insole.
[olootbv] (score 2, diepte 0) 1) arch support inserts


2) figured that my feet tilt outwards (supination) so I have a wedge under my insert.


3) youtube stretches for pf

4) pf sleeve for my foot
[olosgbl] (score 2, diepte 0) When I have it bad, I rub Voltaren Arthritis Pain Gel on the bottom of my feet before bed and in the morning.  Strange but works for me.
[olouwlp] (score 2, diepte 0) Birkenstock super Birki clogs and a good foot rolling session after work solved it for me. They take a bit to get used to, as they are very supportive and have little squish, but once you get used to it they’re unparalleled for long days on your feet.
[olov1s4] (score 2, diepte 0) i think walking around on tiptoe at home helps me. it is easier to integrate into my routine than static stretches.
[oloxr2i] (score 2, diepte 0) Get a lacrosse or tennis ball and roll it back and forth on the floor with each foot to massage and stretch the arches. I do this when I'm watching tv or reading on my days off.
[oloz5gy] (score 2, diepte 0) Compression socks were like putting on new legs.
[olp01nf] (score 2, diepte 0) Merrell shoes and a tennis ball to roll your arch on
[olp8axq] (score 2, diepte 0) You need better shoes bro. That's the cure. Better shoes. It's literally just swollen scar tissue because you won't wear good shoes
[olpdbhb] (score 2, diepte 0) When I got PF (not in kitchens), it was literally cured overnight with Danskos. Ymmv, but they were nothing shy of a godsend for me.
[olpmq6g] (score 2, diepte 0) This is a great post to make because I’ve searched the same thing before and we are far from the only ones dealing with it. 

One of the biggest things that have helped me is staying on top of stretching, like others have said. It all started for me with tight calves which led to inflamed plantar fascia. A foot roller worked great when I was first learning on how to deal with it. I now also rotate my shoes so I don’t wear the same pair two days in a row. Compression socks has been my latest addition, I even bought ankle length compression socks that have a tight band around the bottom of my foot for when I wear shorts. I am considering trying out a cheaper massage gun next for extra help when it comes to my calves still feeling tight.

I appreciate all the other comments and tips here as well, good luck!
[olpsect] (score 2, diepte 0) Look up calf stretches that you can do against a wall. 

Apart from that, i personally recommend you get a good non slip sneaker with good arch support. I would recommend just regular sneakers, but if you slip and fall, they will say it's your fault because you werent taking proper precautions by wearing non-slips. So look online for non-slip sneakers.

The important thing is that they have good arch support built in and they lace up. If they don't lace, then you can't get them tight to your foot. That means your foot moves around too much inside of them and moves into bad positions where the arch isn't supported.

If you can't find sneakers, non-slip, low top work boots are a good option too. They're made for people to be on their feet. They will probably be steel toe, but you don't need steel toe in this industry and if you can forgo it, you should. I hate steel toes. 

Shoes are probably equally important as stretching. Those calf stretches are huge because they also stretch the plantar ligaments or tendons or whatever they are.
[olq9z8e] (score 2, diepte 0) I just found a shoe company called KURU last year that makes a line for people with orthopedic problems. The shoes are expensive but amazing. But stretching and exercises are the way to go. I did physical therapy for a year to stop the worst of the pain and still continue my stretching.
[olqy8av] (score 2, diepte 0) Run around the block barefoot. Sounds weird, but it will solve all of your problems...
[om5edps] (score 2, diepte 0) Two pairs of socks!  My bf has been in restaurants for 40 years and that's his favorite tip.  Also, for pf look up foot strapping (taping) videos, really helps.  Also, if you can find a massage therapist to do cupping on the soles it can help.
[olnszzj] (score 1, diepte 0) Warrior pose
[olpb31q] (score 1, diepte 2) Smartwool and Darn Tough and Icebreaker make excellent merino socks for running and hiking with bands for arch support. They are hideously expensive, but they have the advantage of needing to be washed less frequently, as wool has antimicrobial properties (just air them out between wearings . I’m a knitter, and it is a known issue that Chinese companies lie about the fiber content in yarn and in clothing, so look for socks made in the US, Canada, Peru, Australia, New Zealand, or Europe (but ugh, tariffs). Look for a wool content of 40% or better. 

(In case anyone is wondering about what “merino” means, it is the name of a breed of sheep that produce wool that is both soft and durable.)
[oloblby] (score 1, diepte 1) Yep, I got some good insoles and mine went away.

My boyfriend is a chef and I am a delivery driver and we both wear redback boots with insoles. I use Currex. I cant remember what he gets, but I remember he gets them at Footwear, etc.
[olohssi] (score 1, diepte 0) What kind of shoes are you wearing at work? Do \*NOT\* wear work boots with a raised heel, even if they're non-slip and look cool.
[olrfcci] (score 1, diepte 0) /r/goodyearwelt, custom fit boots, SuperFeet insoles.
[olvcxe6] (score 1, diepte 0) I had this 2x, each time took about a year to recover. 2nd time, I finally saw a podiatrist who made custom orthotics for about $500. I can move them into any shoe. That was 2012. Still on my feet all day and hiking on the weekends. Never had another episode.
[on1uixw] (score 1, diepte 0) My boyfriend's mother has the same problem. But She found Sketchers shoes and now she's ok.
[olo6tv1] (score -1, diepte 2) Can’t wait till you tell me about your no seed oils and veganism.

