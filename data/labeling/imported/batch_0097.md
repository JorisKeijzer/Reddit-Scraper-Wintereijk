# Label-batch batch_0097

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
Schrijf het resultaat naar `batch_0097.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1el0d8d, 1gzxy8m, wflosm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1el0d8d ===
SUBREDDIT: r/TalesFromYourServer
DATUM: 2024-08-05  SCORE: 35  REACTIES: 76
TITEL: What have you found to be the best cure for feet pain?
POST (source_id=post):
I work on my feet all day and have some underlying issues with my feet already, just curious if anyone has a good hack to help ease the pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lgofglc] (score 57, diepte 0) Invest in some genuinely good shoes, don’t wear those shitty lil sneakers with no arch. Shoes for crews is the go to, although I’ve been rocking with Walmart non slips for a year or so and they work. Also Get a size larger and stuff those puppies with dr scholls inserts. Now.. the big one… wear compression socks. They actually help so much
[lgoflzn] (score 46, diepte 0) Compression socks and really good shoes. You will notice an immediate difference with the socks. Try a medium compression first. You'll blow through cheap shoes faster, while good shoes will last a while. It can also help if you can eventually have two pairs of shoes and let one pair rest between shifts.
[lgou5ud] (score 17, diepte 1) Alternating shoes is great.  Shoe trees really help extend the life of a pair of shoes.
[lgp9x50] (score 17, diepte 0) Work a side hustle as a dominatrix and have men pay you to give you a foot massage.
[lgow1p7] (score 12, diepte 0) If you're over 40, get your feet resized. I totally effed mine up by not knowing that your feet get bigger as you age. I'm 20 years in kitchens so I just assumed foot pain was normal. Turns out, I was wearing shoes almost a size too small. For YEARS.

 Sized up, got insoles for plantar fasciitis. 2 years later my foot and knee pain is gone.
[lgoooku] (score 11, diepte 0) Rye whiskey.
[lgph0bv] (score 10, diepte 2) Sadly you need the compression up to your knees. Not cute but a life saver.
[lgofpvi] (score 10, diepte 0) yep, you have to have good shoes. Ask some wait-people or nurses what brand they suggest.
[lgol4lh] (score 10, diepte 1) Nurse here and former waitress. I had the best luck with Dansko shoes, they are pricey but well worth it!
[lgovdue] (score 9, diepte 1 OP) I have been using tequila
[lgp3qwr] (score 8, diepte 1) Came here to say compression socks and elevate your feet with them on. I'm doing that right now.
[lgojr4o] (score 8, diepte 0) Epsom salt baths(even if it’s just your feet)  and 10 min of full body stretching before and after bed
[lgpbc52] (score 7, diepte 0) 1. Compression socks 

2. Shoes with good arch support - I recommend looking for ones that are geared towards nurses, since they need to stay on their feet all day. Try Dansko clogs. 

3. When you get done with your shift, lay on the floor on your back with your butt all the way up against the wall and your feet in the air. (Like this https://images.app.goo.gl/aWyh9SNPRDe9aqSS6 )

4. Get a racquetball and stand one foot on the ground and one foot on the racquetball and roll the sole of your foot around on it  (like this https://images.app.goo.gl/xMDiE1fgURT1kEkm6 )

Good luck!
[lgonmoy] (score 6, diepte 2) I now wear Comrad brand, but I started  with some I got from Dicks Sporting Goods. I have a friend who is a flight attendant who is happy with the ones from CVS.
[lgpkbhy] (score 6, diepte 1) A few weeks ago someone made a post after working in a restaurant for two days, complaining about the manager being rude. They only took the job while studying for the nursing board exams. Since I have done both I told them that they might be in the wrong field if they can’t handle stress. They thought nursing managers would be more professional! I finally had to block the delusional person! They were going to quit the restaurant job!
[lgou91i] (score 5, diepte 0) It's definitely worth it to get good shoes. If you have a local running store, go there. Explain what you do (on your feet all day). They will watch you walk & make suggestions. I like Brooks, but there's also hoka, vionic, kuru
[lgp6fnn] (score 5, diepte 0) If pain involves legs, I sometimes take some over the counter magnesium. Especially if have been sweating a lot recently.  

If you have things like kidney disease, then talk to your doctor first.
[lgphytk] (score 5, diepte 0) Mail carrier here. My podiatrist told me to get Superfeet (green) insoles off Amazon. Been using them about a year and it's been a huge difference.
[lgp3fdm] (score 4, diepte 1) Do they make a no-show or ankle compression sock?

As for shoes, I like Crocs Bistro.  Non/slip and very comfortable.
[lgojk79] (score 4, diepte 1 OP) So sugar and just unhealthy food? Or carbs?
[lgpquyd] (score 4, diepte 2) Nah, Tequila only works if you're in a Metric System country.  You need a Bourbon for your "feet"
[lgq4wxq] (score 3, diepte 1) The Walmart shoes made my feet so sore. Crocs are around the same price point & im only sore after doubles. A bonus is they’re all one piece of rubber so they don’t fall apart like the Walmart ones. When I had them they would maybe last 4-6 months
[lgog43n] (score 3, diepte 0) I stopped eating sugar and carbage. My back and feet pain disappeared within a week. 🤷🏾‍♂️
[lgp83cs] (score 3, diepte 0) Do you work for a chain? Sketchers has discounts for certain places and they're pretty great on the feet. 
I've gotten by with Walmart non slips, I had a really comfy pair that was about $60 from them and my current pair is Dr scholls brand with the inserts and so far so good. 
Shoes make such a difference. You can't skimp on them when you're on your feet as much as we are. 

Also soak your feet when you get home. Epsom salt foot bath or even get one of those massagers....
[lgpvdry] (score 3, diepte 0) Whatever you do don't wear the shoes that have the memory foam in them for all day use they will give you plantar fasciitis. I had terrible foot pain when I was wearing them and went to the podiatrist and that was the problem it took many exercises and stretches and about two years to fix the problem.
[lgqafm7] (score 3, diepte 0) Good shoes and a foot soak once a week in eucalyptus Epsom salt 


23 years in the biz. Life saver.
[lgojo25] (score 2, diepte 1 OP) I have two pairs i wear currently but was looking into the socks, any brand you like?
[lgr5zjb] (score 2, diepte 2) Comrad has no-show compression socks -- I've never looked for another brand -- but I've never tried them when I was on my feet all day.
[lgpf0lf] (score 2, diepte 2) Dansko!
[lgrf0b6] (score 2, diepte 2) You can get no-show compression socks. I wear them for my retail job. I bought them online.
[lgvq80c] (score 2, diepte 2) I’m not sure I never tried but I’d assume something would be better than nothing!
[lgpt2bw] (score 2, diepte 3) Muricah!
[lgoyi5y] (score 2, diepte 2) Works for plantar fasciitis.
[lgq5f4z] (score 2, diepte 1) I destroyed my feet wearing sperrys when my first place had a more lax dress code. Literally would walk out of work limping unable to put weight on my feet after a 6-7 hour shift.
[lgoy7sl] (score 2, diepte 0) I got prescription orthotics for my shoes. First thing I do is take the insoles out of my shoes and put in the orthotics. If you can't afford that, get some good hard arch supports from Walmart or CVS or something. Your feet will thank you.
[lgpdru9] (score 2, diepte 0) See a podiatrist. Mine put me in custom orthotics and it made a HUGE difference. If I stand in soft shoes, my ankles turn outwards, making me bow legged at times. It was the main reason I started wearing high top canvas shoes. High tops and the inserts are heaven. Ankle and arch support.
[lgpf2gz] (score 2, diepte 0) I found the dr scholls for 200lbs and over really help with making my legs less stiff after a long shift
[lgpfncq] (score 2, diepte 0) Put your feet up when you get home. Ideally, with your feet above your heart.
[lgqb6vr] (score 2, diepte 1) Super feet insoles are awesome I’ve been using them for years and I work on cement floors all day long
[lgvlgwp] (score 2, diepte 3) I had no idea you could take insoles out so easily. I'm dumb as hell and never tried, lol
[lgpj8jq] (score 2, diepte 0) Soak them in warm salt water
[lgpla2n] (score 2, diepte 0) Dr Scholl's insoles save me a majority of the foot pain
[lgpmq80] (score 2, diepte 0) Really good insoles, compression socks, and keeping them levitated when you get home
[lgprigt] (score 2, diepte 0) Epsome salt!!! Soak 'em!
[lgpwbpe] (score 2, diepte 0) I was told by a supervisor at Walmart to get Nike running shoes. Not walking, running shoes. Holy cheese was it a difference from the crap I was wearing. My legs felt better and my back wasn't in nearly as much pain after a shift.
[lgq54b6] (score 2, diepte 0) Freeze water bottles and roll em under your feet. Also take hot baths with epsom salt. I worked at Walmart as a stocker so I was on my feet all day and did miles of walking.
[lgq5wh3] (score 2, diepte 0) Supportive Gel insoles, helps my joints soooo much!
[lgr1dmi] (score 2, diepte 0) Magnesium supplements. I thought I was going to need foot surgery but this worked so well, even my coworkers ask me for it now. Most people are very depleted on this vital mineral, and it's a game changer. Most are sold "as oxide" which is not absorbable and makes you poo, so look for one that is "citrate, taurate, or glycinate" they have slightly different focuses so look into it if you like research,  or you can just take my word that this is the way. Also I don't do well with insoles so I took them all out of my shoes for a more "barefoot" experience. fwiw been in the business 25 years.
[lgq8vog] (score 1, diepte 1) New Balance makes a good pair of black leather slip resistant shoes as well. I would also say soaking my feet in a hot water bath after a long shifts does wonders too.
[lgomjcb] (score 1, diepte 2) Sugar and the junk. I ate more and more fatty meats (steaks, fish, etc), butter, eggs, and bacon. This helped me with my cravings for the sugar/junk. 

I’m a Physical Therapist (I help out my parents with their restaurant)  and I could not get rid of my body’s pain, R shoulder, back, and feet. It was all about my body’s inflammation, so none of my tricks and/or exercises worked. My inflammation was too high for too long. 

My suggestions:  •cook your own foods •DO NOT use vegetable/seed oils, they’re highly processed (pro inflammatory) ingredients •minimize breads, rice, oatmeal, pasta, cereals, bananas, grapes, apples; these are nothing but sugar once ingested •Increase ingredients from animals: fatty meats, eggs, cooking fats, whole milk dairy products with no flavors (mix in berries yourself in case you need some flavor in your yogurts, etc)

In summary:  don’t fear the fat, prioritize protein, and cut the carbs = inflammation/pain/moodiness/brain fog↘️ 

Keep in mind that this does not have to be forever. ☝🏾

But the more you stick with it the quicker and better you will feel. 

Good luck. 👊🏾
[lgr8q2v] (score 1, diepte 1) This is probably stupid but can I wear compression socks after my shift? I wear shorts that are just slightly above my knee and would look so stupid wearing compression socks.
[lgvrb0k] (score 1, diepte 3) I would really emphasize a solid stretching routine for long term relief. My chiropractor told me foot pain / planters fasciitis stems from tight hamstrings hips and lower back muscles. Some people like to write off chiropractors advice so Take that as you will but there’s literally nothing to lose by stretching. I like foam rolling and rolling my feet over frozen water bottles or lacrosse balls for short term relief. My bf got me a massage gun and goes to town on my feet and ankles for me bless him cuz that shit feels amazing as well.
[lgoy6lz] (score 1, diepte 1) Lol no
[lgp0u3v] (score 1, diepte 0) I hate to even say it, but good feet store insoles have worked, that said, they are salespeople, never buy shoes etc from them, you really only need one insole, but they sell 3, if you can buy only one tell me how you did it
[lgp6re6] (score 1, diepte 0) the insoles from birkenstocks + learning to lace my shoes correctly for my foot shape + elevating my feet whenever (and i mean WHENEVER) i can + plentiful stretches and self massages. it’s not perfect but when i’m diligent it helps.
[lgva6wx] (score 1, diepte 1) Ah yes, this is the way, my little chickadee.
[lgsyxdl] (score 1, diepte 1) How does the trimming work?
[lgukmvi] (score 1, diepte 2) Pretty easy, just the usual line up, mark and cut with scissors. I usually use the original insole from the shoe.
[lgvrszw] (score 1, diepte 4) Learn something new every day! Lol
[lgu3wur] (score 1, diepte 1) Especially Epsom salt
[lgqlani] (score 1, diepte 0) Hot soaks and black runners with support!.
[lgqlp3h] (score 1, diepte 0) Sounds counterintuitive but if you're physically able after shift, change into sneakers and walk around the block for 3-5 minutes.
[lgqtvbs] (score 1, diepte 1 OP) Really??? So like if it hurts keep walking??
[lgr7p0v] (score 1, diepte 0) Hoka Bondi SR non-slip shoes
[lgra334] (score 1, diepte 0) Inserts and a massage gun. Use the gun on the arch of your foot to help loosen. Don’t over do it build up a few mins each time. Heating cooling pads as well
[lgrduqc] (score 1, diepte 0) For me it was weight loss.  I always thought I had terrible feet because my mother did, and that was why my feet would be killing me after a 6 hour shift or 2 mile walk.

  
Turns out it was because I was fat and there was simply too much weight on my feet.

  
I lost a lot of weight, and now I walk more than any other job I've ever had, and I do it in dress shoes, and my feet are like, slightly uncomfortable at the end of a 14 hour day.  Not even uncomfortable enough to take a tylenol.
[lgres2h] (score 1, diepte 0) If you get pain in your heels/achilles tendon, stretching and massaging your calves helps a lot. I use a massager on mine before bed and it helps with that pain a lot.
[lgrn1mj] (score 1, diepte 0) Yoga toes after work.
[lgry2qg] (score 1, diepte 0) I bought protalus inserts on a whim. I even added them to my gardening boots now. Helped my feet as well as ankle, knee and hip pain. Buy the good shoes but add a good insert as well.
[lgsp4dk] (score 1, diepte 0) The restaurant style crocs on Amazon. They have been incredible. I last all day with no feet pain. I still feel the soreness of gravity on my legs but I past through my shifts with no issues
[lgsp9l6] (score 1, diepte 0) Nonslip skechers
[lgt2bwa] (score 1, diepte 0) Better shoes. Vime's theory of boots.

Also. End of day, hot pads under your feet for 20 mins, then after ice your feet for 10 mins.
[lgt7k26] (score 1, diepte 0) Good shoes is #1. Makes a huge difference. Buy new shoes when you need to. l
[lgtf3rm] (score 1, diepte 0) I had vionic non slips with those fancy $50 dr scholls insoles. Cost me about $200 overall but definitely made a difference in working doubles.
[lgu5691] (score 1, diepte 0) Insoles that A- you can mold your feet, and B- are made for each shoe size (unlike most drugstore ones, that are usually just small, medium, large).

The brand Sole saved me after over a year of problems. They have a variety of types, and you can heat mold them at home.
[lgv1y9a] (score 1, diepte 0) Compression socks. 
Really good foot wear. 
Customer orthotic insoles 
Heat and massage. 
And if you’re inclined… -a Kentucky mule and a few good rips of the devils lettuce. Always makes my feet feel friggin awesome after 16-18 hours stomping around with them.
[liumunf] (score 1, diepte 0) Good shoes, I use non-slip work shoes from Elten (only available in Europe I think), now my feet and legs still feel great after a 10 hour shift.
[lyvqlcu] (score 1, diepte 0) Been there done that. Insoles helped me (I’ve started using Akusoli). Also, compression socks as someone mentioned. It migth also be a good idea to check with a podiatrist.
[lgowgoj] (score 0, diepte 0) Moccasins.
[lgqcjua] (score 0, diepte 1) this is the way.

=== THREAD 1gzxy8m ===
SUBREDDIT: r/retailhell
DATUM: 2024-11-25  SCORE: 53  REACTIES: 76
TITEL: Any tips for standing 8 hours on your feet?
POST (source_id=post):
I already have knee problems and I have never worked for 8 hours before

If it were my old corporate job I wouldnt even mind working for 12 hours, but this job is a physical one, I have to lift heavy items and move the whole time and I can't sit

I know others do it, I've seen women much older than me that work for 7 hours everyday and i don't know how they do it, I guess I'm weak

Any tips on how to do it wothout feeling exhausted? How do you do it?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lyzqykl] (score 51, diepte 0) Good shoes. And take every chance you get to stretch your legs, put backs, facing up, whatever.
[lyzr9pp] (score 29, diepte 0) Get a great pair of shoes. Don’t skimp on them. Investing in your feet will keep your knees and back quite a bit happier.
[lyzvb5y] (score 24, diepte 0) Compression socks and good quality shoes make a huge difference for my foot & leg pain.   I alternate between pairs of Brooks, Hoka and Orthofoot.
[lyzsyk3] (score 19, diepte 0) Get comfy insoles
[lz0zvh3] (score 11, diepte 1) Very much this. Half my store wears Hokas, they're a bit pricey but worth it. Regardless of brand, get _non-skid_ shoes, don't wear anything too heavy (I wore Timberland Pros for three years, my first week after switching away from them felt like I was walking in Moon Shoes from the 90s), and only get steel-toe if your job requires them.
[lyzut8i] (score 10, diepte 0) Get medical insoles. I know they’re expensive, but worth it. Ask your older colleagues if they have a trick for lifting heavy objects. Stretch as much as you can and even your upper body. Relax on your days off, your body needs the break! The first weeks will be very hard, but you’ll get used to it.
[lz0g9n1] (score 9, diepte 1) This ! 

Dr. Scholls makes a few that run between
$15-20 and they're a game changer. Mine are Gel something's for runners.

I average between 9k - 15k steps per 8 hour shift, and now I don't wear any shoes without em', they're so comfy. 

xD
[lyzvrtn] (score 9, diepte 0) Compression socks and good shoes plus taking walking breaks when you can. My feet hurt worse when I had to stay in one spot cashiering. Now I get a wider space to move and my feet feel a little better.
[lyzutjp] (score 7, diepte 0) Like everyone else, I recommend good shoes. They don't need to be pretty - get something comfortable.

As far as I remember, I got used to it after about a month of working. Now I can stand all shift with no problem.
[lyzwc8j] (score 7, diepte 0) Get shoes in either a wide or about a half size bigger than you normally wear with good insoles.  If your knees are a problem,  have on hand some kind of knee support, like neoprene sleeves. If you're doing alot of lifting, also consider a back support belt. Try to remember to practice safe lifting and carrying. As you get used to it, it will get easier in some ways but don't destroy yourself by trying to do too much more than you can.
[lz00bfb] (score 7, diepte 0) Look up some basic yoga. Do it in the morning before work, focusing on your legs. Modified shoulder bridges saved my back. 

Get some good shoes. Hokas, asics, or Skechers. I personally wear Skechers Max Cushion Arch Fit 2.0 and D'lites. Definitely more than one pair. 

Get your steps in. Shift your weight around. Prop a foot up on something casually if you're allowed. Drink Gatorade or eat a banana for potassium. You've got this.
[lz08p1i] (score 7, diepte 0) People say "good shoes" but I'm gonna get specific. 

1) check the end of the shoe where your toes go. If they are pointy or pointed, they won't do. Look for a rounder toe box, this gives your toes more room to breathe and they will swell less. (I go for converse shoes for this reason, vans are also good. They work best with flat footed individuals - which I am)


2) check the arch. Most shows have a high arch, so if your arch is high this will be very easy and minimal work for you. If you have flat feet try to find a smaller arch. (My feet used to always hurt because I had high arch shoes and flat feet.)


3) do not tight lace your shoes. You want to open up the shoe as much as possible without it being too loose. This will help with blisters, toe pain, and make walking/moving easier throughout the way.
[lz0fjs6] (score 6, diepte 2) Because theyll swell after a few hours.
[lyzxq1t] (score 6, diepte 0) Great shoes, good insoles, compression socks.
[lz00sjg] (score 6, diepte 0) Compression socks and good shoes that support your body.
[lyzxkjs] (score 5, diepte 0) Medical compression socks or garment!
[lz1weor] (score 4, diepte 1) Also find some good insoles as well.  They help a lot. Have at least 2-3 shoes to rotate to they last longer
[lyzt0qc] (score 4, diepte 0) In addition to good shoes, if you have to stand for hours up front on the register, get one of those cushioned floor mats.
[lz1c6ej] (score 3, diepte 2) At my old job I used to stand at the register all day. At my current job I stock etc. when there are no lines at the registers. I got a pedometer app for my phone and was surprised to learn that I walk between 4 and 7 miles in a 5 hour shift. It's done wonders for my health, but my legs/feet do get tired. No horrible pain though.
[lyzypl4] (score 3, diepte 0) Good shoes.

Stretch in the morning and at night
[lz0489h] (score 3, diepte 0) It really is something you have to build up to. I know this probably isn’t an option for you at this point. 

I have arthritis in my knees, hips, and back. Honestly this has been the best job for my body. I haven’t had many flareups over the past year, primarily because movement is actually good for arthritis. That being said, make sure you wear the best shoes you can. Get knee braces if you got to.
[lz0elud] (score 3, diepte 0) Sleep with your feet higher than your chest. It helps my legs feel relaxed while laying down and refreshed when I wake up
[lz46hy3] (score 2, diepte 2) I absolutely love Hokas, they are the most comfortable shoe on the planet.  Pricey, but your feet are worth it!!
[lz3j22j] (score 2, diepte 1) Spenco Cross trainer Insoles 

Limited-time deal: Spenco Insoles Polysorb Cross Trainer - Lightweight, Full-Foot Inserts with Heel-to-Toe Cushioning, Support, & Odor Control, All-Day Comfort & Stability - Ideal for Runners, Walkers, Athletes https://a.co/d/gJUBziO
[lz01iat] (score 2, diepte 0) good, well cushioned shoes
[lz04riw] (score 2, diepte 0) As many have already probably suggested, good fitting shoes with adequate sole and arch support are paramount when having to be on your feet 8+ hours a day.  There's also some good knee/ankle braces/supports that you can wear that go under your work clothes which will help lessen the strain on those joints.
[lz0b6r3] (score 2, diepte 0) When you get home from your shift, lay on your back @ put your legs up the wall.
[lz0e988] (score 2, diepte 0) You’ll get used to it.
[lz0no9d] (score 2, diepte 0) Stay away from the energy drinks lol
[lz26gk3] (score 2, diepte 2) Currently I have the dockers comfort flex. They could be to squishy for you
Added a link so you can see what they look like. I purchased mine from my store (Marshalls) for $38 
 [shoes](https://search.app?link=https%3A%2F%2Fwww.ebay.com%2Fitm%2F355724444591%3Fchn%3Dps%26var%3D624814880179%26_trkparms%3Dispr%253D1%26amdata%3Denc%253A1x3TVAy-FQzGi-H6b7__4wg17%26norover%3D1%26mkevt%3D1%26mkrid%3D711-117182-37290-0%26mkcid%3D2%26mkscid%3D101%26itemid%3D624814880179_355724444591%26targetid%3D2321110924221%26device%3Dm%26mktype%3Dpla%26googleloc%3D9028019%26poi%3D%26campaignid%3D21410650550%26mkgroupid%3D173029508308%26rlsatarget%3Dpla-2321110924221%26abcId%3D9450104%26merchantid%3D101743202%26gad_source%3D1%26gclid%3DCj0KCQiAgJa6BhCOARIsAMiL7V9nLGNvaNPSFdTxaHZ119I5ADfgLU962O962tk_snW0OG_UytyoCEEaAlxlEALw_wcB&utm_campaign=aga&utm_source=agsadl2%2Csh%2Fx%2Fgs%2Fm2%2F4)
[lz5mpua] (score 2, diepte 3) Those look good, and I like that they're all black. I kind of dress up for work (dressing up for me is not jeans or track pants or my first preference, pajamas) and wearing shoes that actually go with my clothes is impossible, so solid black running shoes are good.

Anyway, thanks!
[lyzuwj3] (score 1, diepte 0) Good shoes which can be on the more pricy side. I got two pairs of Brooks, one pair brand new for about $150 and the second pair for $20 off of marketplace. They have been a life saver for my feet and knee, stretching and sitting down when I can also helps a lot.
[lz0dylc] (score 1, diepte 1) Might sound dumb, but why get shoes in a size bigger?
[lyzz2sy] (score 1, diepte 0) Get some nice support inserts for your shoes helped me .
[lz00jhb] (score 1, diepte 0) My doctor had me get the superfeet blue inserts and prescribed me an anti inflammatory and it’s been a night and day difference.
[lz1dhbv] (score 1, diepte 1) If the anti-inflammatory is an NSAID, be careful, my doctor had me on one for years and it damaged my kidneys.
[lz1l2oi] (score 1, diepte 1) I'm envious because I've had the opposite experience. I can be on my feet all day at home but the concrete floors at work are just a nightmare on my arthritic ankle and most days I get home and can barely walk.

Fortunately it doesn't hurt as much once it's warmed up, but even sitting for 15 minutes on my break means I'm limping for half an hour afterwards. I've started walking on my breaks and lunch just because I don't want to deal with the pain after resting.
[lz04h06] (score 1, diepte 0) Shoes,shoes shoes. I was cna, bartender or deli worker for my whole life. I am 60 still working.  Invest in either a great pair of food service( no slip, waterproof, padded) or nursing shoes. Probably have to replace at least once a year but your feet,legs,back will thank you. Remember- if your feet hurt, your whole body will ache and you will get tired faster.
[lz0677a] (score 1, diepte 0) Other than good shoes and insoles, find a rhythm so you can move a bit back and forth. Find a way to, occasionally, shift position (lean, kneel, etc) and stretch out. 

Yeah you're stuck at a register for 8+ straight hours but do the best you can to be a little mobile and it will at least make you a little more comfortable.
[lz071xb] (score 1, diepte 0) Hoka shoes if you can afford them. They are 100% worth the $150 in my opinion. I’m on my feet 8-12 hours a day and they last on average 3 months before needing replacement. However if you swap between 3 pairs of shoes per week, you’re typically set for a year.
[lz084s6] (score 1, diepte 0) Good insoles and a bottle of ibuprofen in my locker. I'd say good shoes but ever since discovering some nice insoles I can wear pretty much any shoe. But aches and pains are still an occasional part of the job.
[lz0ai3u] (score 1, diepte 0) I know lots of people have said this but genuinely, as long as your footwear is as comfy as you can possibly find/own coupled with a pair of extra insoles for the extra bit of comfort you'll be surprised how fast your body will adapt.

This bit sounds silly & no one ever told me this but Wearing a super cheap pair of socks over the top a better pair or even normal pair of comfortable socks always was the difference between having blisters and not having blisters for me too. 

Both things were the difference between me hobbling around home after work in agony, or taking my shoes off and feeling like i had just been for a walk for the afternoon :)
[lz0baz5] (score 1, diepte 0) Good shows, leg exercises etc,
My friend who does Thai boxing actually wishes he had my legs coz I walk everyday and I'm on my feet for maybe 12-17 hours a day, I also tend to stand on one leg at a time, challenging myself to stand like it as long as possible at work, so while on register especially if all day I'll be posing as my friend dubbed it, crane style lol
[lz0bzxg] (score 1, diepte 0) I found that buying a pair of shoes 1/2 size larger than what I wear really helped by giving my feet room to swell
[lz0cex8] (score 1, diepte 0) See if your company offers subsidies on non slip shoes. I go through shoes every 6 months or so. If you can get shoes through shoes for crews or srmax  (those are what my company uses) they offer great fitting shoes at any size
[lz0cz0p] (score 1, diepte 0) Definitely get good shoes. I prefer Nike air max as they have great support when standing on concrete floors for 8-12 hours a day. 

Also, like another comment stated grab yourself a knee brace for support. Be sure you're following safe lifting guidelines. 

Once you've found the right shoes for you. You'll know. Good luck!
[lz0fcfg] (score 1, diepte 0) Compression socks,  good shoes,  magnesium supplements, and whenever you can put your feet above your head to help the lymph drain.
[lz0fz2x] (score 1, diepte 0) My job requires kitchen safe non-slip shoes. I have been wearing Hoka’s for about a year now and they are fantastic. I have flat feet, so a majority of shoes are uncomfortable. These are fantastic.
[lz0ijxx] (score 1, diepte 0) Don’t. But seriously get a pair of converse
[lz0ja8p] (score 1, diepte 0) Good shoes and keep active. Walk around whenever you can and make sure to stretch
[lz0jjf1] (score 1, diepte 0) I figured out for me that if I go 5 days without a long shift - even if I walk around a normal amount during that time - my legs ache the first day back. 

So yes you definitely do get used to it, but it’s still always demanding. 

I went for the wide fit shoe for work. They feel like a clown shoe without my two layers of thick socks for regular wear, but I’m really glad for it at work. 

If your workplace provides anti fatigue mats…don’t underestimate them. They really do help. I rolled my eyes once at dragging it 2m to my till and went without for a few hours. Jeez I felt that.
[lz0mnuh] (score 1, diepte 0) When I was a Pharmacy Tech, I was on my feet all day. The only thing that helped was Futuro compression hose. It covers your whole leg and gives all day support!! I wore them through both my pregnancies!!
[lz0pt9y] (score 1, diepte 0) Good shoes, good socks, lots of stretching, and movement when you can. It may seem counterintuitive to move when you’re on your feet but it helps loosen up your joints.
[lz0sb18] (score 1, diepte 0) Dansko and compression socks. 

If you can score Dansko from a thrift store you’ll be able to make sure you like them.
[lz0t485] (score 1, diepte 0) Doc martens and if you’re over 48 and having back or knee pain, steroid injections.  Being tired over holiday will decrease as your body gets stronger thru the season. It’s real exercise.    I throw Wellbutrin on top of it all. And casual caffeine like iced tea.  Not big bump.  But sip thru day. 
V8 makes yummy fruit drinks with 80 grams of caffeine if you need a fast boost in semi healthy way.
[lz0v32x] (score 1, diepte 0) Besides what was already suggested, make sure you are drinking water at work.

I think you’re supposed to drink 1/2 gallon a day. I grew up on well water so tbh I didn’t regularly drink water until more recently.

My feet and knees used to hurt really bad, and most of that pain went away after I made a point to get water in me.
[lz0v55c] (score 1, diepte 0) Don’t lock your knees ,arch supports for high arches ,Epson salts and ice bath for your feet when they really hurt after work ,
A small frozen water bottle to help massage feet after work …Don’t skimp on shoes .
[lz0z6yp] (score 1, diepte 0) While everyone is saying good shoes, let me add in, I also have bad knees, I average 14-18k steps in an 8 hour shift. Find shoes that have a thick heel, cushion inside with an extra insert. Rounded toes! Do not do pointy shoes. Never over tighten your shoe strings. I also like to get wide width shoes, just in case my feet swell. Over the counter pain relief can help. 
Good luck!
[lz1ls3z] (score 1, diepte 1) What shoes have worked for you? I've tried several kinds of hokas but the toe box is too narrow for me. Tried several new balance, and the toe box works but then they're too wide in the back or too squishy overall. I have weird feet I guess. 

Currently wearing new balance non slip shoes. Not perfect but I'm tired of buying and returning $200 shoes. I think these have been the best so far because of a steeper heel drop which is easier on my ankles.
[lz11cwp] (score 1, diepte 0) Good pair of shoes and stretch your feet everyday.
[lz136li] (score 1, diepte 0) Think of it as training your calves.
[lz13hra] (score 1, diepte 0) I work in a shoe department in a retail store. The shoes you pick are incredibly important. 

1. Dont wear heels, it just doesnt work and causes damage in the form of foot, knee, and back pain, with the addition of shortening your calf muscles, making it painful to walk without them. I have seen older women whose toes literally point like a heel does from wearing them. 

2. Function over form. The comfort and build of the shoe is more important than the look because if you’re in pain you wont look good anyways. 

3. Here are some brands that I know that are good for work: 

Ecco is great because their shoes feature polyurethane soles which are very shock absorbent. I walk 10 miles a day in mine at my job. They are great for wider feet as well. 

Borns have a nice cushy sole, but do not have the best arch support. 

Aetrex has fantastic arch support while still remaining soft and cushioned. They feature flats and wedges. 

Dansko were originally nurse clogs, but with hospital dress codes easing up during COVID-19 most nurses wear sneakers. This has spurred them into making more fashionable shoes while still retaining comfort. 

4. Spend the money. Dont skimp on shoes, you really do get what you pay for, and your long term health isnt something to play with. 

5. Try not to stand still, I find that makes my feet hurt more than moving around because the pressure is constantly on my feet
[lz13yv5] (score 1, diepte 0) Get arch supports
  Compression socks too.
[lz14y2k] (score 1, diepte 0) Your not weak, it's bullshit that companies make you do that in the first place. I landed a cashier job where I get a chair and it changed the retail game for me forever and guess what? I'm JUST as good of a cashier without standing for 8 hours, forbidden from even leaning against a wall.

Good shoes do make a huge difference. Stretching when you can also helps. If its allowed and not already provided, a quality one of those cashier floor mats make a difference. You MIGHT be able to get a doctor's note for your knee but it's far fetched in this business that they'd do anything to give you support even with a doctor's note but if it's unionized maybe you can try.
[lz1bibk] (score 1, diepte 0) Everyone else mentioned the shoes, so I'll mention something else. Soak your feet in Epsom salts after work. If I have a longish day (10 hrs), I also use Arnica Pain Relieving Gel. It's a roll-on bottle and is also good for bruising and swelling. It's not sticky or smelly and absorbs fully, pretty quickly. No lotion feeling. I get mine from Walmart for under $10. Then, elevate your feet.
[lz1n1qi] (score 1, diepte 0) Make sure you're getting enough sleep eating the right foods and stay hydrated during your shift.
[lz1oc4b] (score 1, diepte 0) Good shoes + socks go a LONG way

Do not cheap out on these btw, trust
[lz1vs7i] (score 1, diepte 0) Fatigue mats
[lz26qes] (score 1, diepte 0) Everyone else hit the main points so here's my two cents. 

Look for simple quick exercises to strengthen your feet/ankles. Seriously. I had a week right ankle that lead to a nasty limp, that gave way to serious pain and issues. Took four months of physical therapy to work it back out. Knee workouts as well given your knee problems. You need to strengthen the muscles that move you around. 

My feet knees and back still hurt after eight hours but not nearly as bad as it used to, and im no longer horrifically injuring myself.
(7 reacties met lagere score weggelaten)

=== THREAD wflosm ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-08-03  SCORE: 63  REACTIES: 76
TITEL: Will Amazon help me get back on my feet
POST (source_id=post):
Hi everyone. I’m 20 years old I just got unexpectedly kicked out of my dads house and he’s not even letting me have the keys to my car. I don’t know what to do and I’m sort of still figuring it out right now. I only have a little over 100 dollars to my name. Will Amazon be able to excuse my shift? I’m going through a lot right now and don’t have the UPT to cover it trying to get a hotel just so I can not spend the night on the streets. and I also really need this job because I just turned homeless. 
I’m trying to get my keys back to my car and if I do so will Amazon let me sleep in their parking lot for like two weeks just so I can get a couple of paychecks in my account and look to be someone’s roommate no money, no credit is hard to get an apartment with. I’m not sure what to do any advice is welcomed sorry for this post again.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iiukutm] (score 108, diepte 0) Don’t tell them you’re sleeping in their parking lot but go ahead and do it (my sisters x did it for a month when she finally kicked the deadbeat out). Get a planet fitness membership for their showers. Talk to amazons benefits help line thing they will help you find a place to live, help you set a budget for your finances and everything.
[iiuzal5] (score 37, diepte 0) Get a wisely card too so you have $$ daily and you’re not waiting til Pay day.
[iiw4vmm] (score 32, diepte 4) Easier to ask for forgiveness than permission...
[iiuk19b] (score 29, diepte 0) Yes Amazon can help you get a handle on your life, but also file a charge of theft against your father. ༎ຶ‿༎ຶ
[iiupar5] (score 25, diepte 2) I don’t know about your site, but we had a guy with a trailer that stayed in the parking lot. Had a dog that lived out there too. I know a couple of camper force people(when that was a thing?) that would stay out there a few times. But… I don’t 100% know the policy for this stuff. On one hand, if you ask and they say yes, cool. If you ask and they say no, and they find you out there… that might be a weird conversation. You might look into campgrounds too. Again, I don’t know the policies with those and just cars, but it might be worth looking into. Probably cheaper than a hotel maybe. But, hotels have their own bathrooms. Maybe look into an air b&b for a weekly rate? In any case, good luck to you homie. This is just a minor bump in your road.
[iiv8tj1] (score 25, diepte 0) Better to ask for forgiveness than for permission
[iiuykcf] (score 22, diepte 0) Having a job at Amazon, is better than having no job at all. Sleep in your car, shower at a gas station shower like,  pilot J. You should be OK to sleep in the parking lot at amazon. Just don't let them find out, if they do, sleep in a hotel parking lot, maybe even on a residential street that doesn't require permit parking. 

Good luck, though
[iiuld3s] (score 20, diepte 3) Damn that’s really rough. Once whatever is going on passes over don’t ever go back to your dad for help ever. Burn that bridge and start a new life.
[iiwe2bm] (score 20, diepte 3) Talk to the police and explain your situation, ask them if they are willing to do a standby so you can gather your belongings because he's not letting you in.

If the cop isn't a lazy bastard he'll acknowledge that it was an illegal eviction and try to help. Technically you are a tenant and he can't just throw you out on the street without going through the eviction process.
[iiunla3] (score 18, diepte 1 OP) Will they really not let me stay there if I ask? I’m worried about being caught and fired for that. That would lead me in a much worse spot than I am right now if I become homeless and jobless.
[iiv1th8] (score 17, diepte 0) I am so sorry that you have to deal with such a difficult situation. i don’t have much but if you ever need a meal send me message i can cash app u a few dollars l.
[iiujw4d] (score 15, diepte 0) Everyone is going through some shit. Go to work. Get your keys to your car. Sleep in your car at the Amazon parking lot. Get a gym membership to shower. Build up paychecks and rent a room
[iiusbo5] (score 14, diepte 4) Right on. The dude parked way in the outer area. Our parking lot is never full so he wasn’t in the way at all. Anyway… I’m pulling for you random stranger!
[iiwa5gw] (score 14, diepte 1) Don't sleep in a hotel parking lot, they'll kick you out so fast
[iiuospu] (score 13, diepte 0) dont shit where you eat.  you can park at a gym or walmart to sleep.
[iiukg41] (score 12, diepte 1) Charging theft only if the car is actually in your name that is.
[iivx1eo] (score 12, diepte 3) Call the cops! If the car is in your name and not his he has to give u the key. He has to let u get your stuff too and oftentimes police can help facilitate all this for fifteen minutes or so. Also  Guess what call AAA and get a membership that includes a locksmith. Or if it's cheaper, call a car locksmith directly and they'll open your car and make you a new key. Tell them it's lost. If you mention dad they'll think it's his car. Easy peasy. Sleep in the car at any Walmart parking lot and first paycheck rent a room from Facebook marketplace. If you speak any Spanish, Latinos have the cheapest deals. But do call police first and tell them what's going on. Even if they refuse to help, you need evidence to sue him in small claims for the value of your property. But don't think Amazon gives a shit about your problems they don't
[iiul4xq] (score 10, diepte 2 OP) Yes but everything is inside the house which I’m sure he is hiding or shredding everything from me. I’m lucky enough to have my phone on me. So even if I do file a charge he can just deny it.
[iiwwqq4] (score 10, diepte 4) This! I wish I'd done this when my family kicked me out. Would had saved me a lot of grief and I'd feel better about my security months later. Do this please. P
[iiuz6g4] (score 10, diepte 1) Preferably park at a building that is open 24 hours.
[iiusuj5] (score 9, diepte 2) We have about 10 peeps who sleep in their car at mine, but I live in a city with a huge homeless problem. Get yourself a gym membership. EoS is popular in my area. You don’t even need to ask. They won’t bother you if you have a badge.
[iiuym9e] (score 9, diepte 0) I don't know what state your in but some states have laws that prevent your father from kicking you out. He would need to get a judge to kick you out. I'm not sure the laws in your state
[iiwa3cl] (score 9, diepte 0) Dude don't even fucking ask, just do it. Better off apologizing and feign ignorance if you're "caught" than bringing up you're sleeping there and having someone who couldn't care less about your life tell you no.
[iiwlw79] (score 7, diepte 2) If they ever have problems with it you can always sleep in a Walmart parking lot if one is nearby. Walmart doesn’t care and it is a well known location for stopping if you are traveling.
[iiur2wm] (score 6, diepte 3 OP) Thank you. 💜  I’ll ask them tommrow if they say no I’ll follow other peoples advice and park somewhere else since this job is most important right now.
[iix23vi] (score 6, diepte 4) I hope you haven't already but yeah it's illegal to sleep in public parking, unless the owners give permission but Amazon is a place that is a stickler for rules so I guarantee they'll say no
[iivchca] (score 6, diepte 0) If your site allows it, take as much OT as you can. Apartments look at how much you made in the previous months. 

Mine for example took a look in the previous 2 months of pay stubs to see if I made 2x minimum what the rent was going to be.

Also set aside a minimum of $2k to cover the first months rent as well as the security deposit. It's going to suck, I know all too well but it's definitely worth it to have your own place.
[iivg43x] (score 6, diepte 0) Talk to your manager and to HR.  Explain what the situation is - you would be surprised at what resources they have available and HR can take care of your UPT (as long as you don’t abuse it).  We’ve had managers bring clothes and food out of their own pockets to help employees. Also check your A-Z app under Benefits.  There is a section called Resources for Living.  Toll free and anonymous.  They offer guidance and help for a lot of different things going on in your life.  You get a couple of free sessions with a counselor and I think you get a free session with a lawyer that could give you advice on how to handle your situation your Dad.  Good Luck!
[iixwxw4] (score 5, diepte 2) They will say ‘no’ ESPECIALLY if you ask. It means that they will accept liability for you in their parking lot. So, while they may want to, they can’t. It’s more a don’t ask don’t tell. Good luck. You’ll get through this.
[iix9i1k] (score 5, diepte 1) Planet fitness membership is cheaper
[iiulju9] (score 4, diepte 3) Damn...
[iivxdhz] (score 4, diepte 1) True he can call police and say his father is illegally evicting him and they'll make dad let him stay she'd have to go through an eviction process. This is especially true of OP pays rent. Hell even if he doesn't, just SAY you help pay rent CASH end of story police will let you in the house
[iiv5g27] (score 4, diepte 1) It's hard find ppl like you 🙏🏽
[iiwl6pg] (score 4, diepte 0) If you call erc and tell them you're having an emergency and need a day off they can do a thing called "planned absence reporting" and will excuse your hours. I just did it for yesterday, make sure you say the planned absence reporting thing otherwise they'll just act all confused.
[iix61bg] (score 3, diepte 3) Call them anyway and file a report and also they will demand be let you in to get your property well should I'm not a lawyer but ya do it
[iivd5mi] (score 3, diepte 0) Call the cops to get your keys and stuff back
[iiw6h89] (score 3, diepte 0) Sleeping out at the end of a Walmart Super center, where some other 18 wheelers park and sleep is safer and less conspicuous. I did it all last summer thru November & never once had any issue nor any patrolling cop spotlight me sleeping in it. Get there early evening and lay TF back and stay down till morning. Our Amazon keeps at least 2-3 local pd units stationed in the parking lot. They'd notice if the same car was there - esp if they saw movement inside it. Too risky to me.
[iiwik1b] (score 3, diepte 0) If you can get your car back, and have a Walmart near you, the vast majority of Walmarts allow you to park overnight. They even allow RVs, so a car is no big deal to them
[iixbd8d] (score 3, diepte 3) Planet membership is only like $10 a month and you can cancel it whenever. They also have free food twice a month and massage chairs. The truck stops are way too expensive.
[iix87n1] (score 3, diepte 0) i would really ask the the non emergency police line if they will assist you in getting your stuff.. you are an adult and you can't just be illegally kicked out.
[iiweqw2] (score 2, diepte 3) It doesnt matter the car was registered in your name, if he shredded the title he won't be able to reproduce a new one, if I were you I'd hot wire the car and drive off, figure the rest out later, but I wouldnt leave it at your work
[iiwej4u] (score 2, diepte 4) They should only really care if they don't have enough parking happened in my building they paid for our lyft to reduce parking.
[iiw0lii] (score 2, diepte 2) Just sleep at a Walmart
[iiulo3i] (score 2, diepte 0) Idk bro not going to the one place that gives you money to make a living seems like a bad move. Get those hours in and maybe move out? Save up at least 3k if you seriously want to get your own place.
[iiwwx9y] (score 2, diepte 2) It's a legit saying. Basically means to keep boundaries betweem where you make your money and everything else.
[iiwolg7] (score 2, diepte 2) I've park at a hotel parking lot for 6 hours and my car was still there. You are right though, there are better options than a hotel parking lot.
[iixrueq] (score 2, diepte 1) If you're that bad off you gotta get that Anytime Pay.
[iiv3obn] (score 2, diepte 0) Do there CDL A train also while your there  to start being in hella cash and get a planet fitness membership to use da showers and there was a guy at my site dat slept in the parking lot and never told them dat he was there so depending on your site you should be Ight and at dis point you should try and take advantage of the benefits Amazon gives you
[iix9gb3] (score 2, diepte 2) Not everyone is a shitty human like you
[iix6651] (score 2, diepte 1) *Walmart is a safe*

*Overnight sleeping just so*

*Anybody knows*

\- Suitable-Ad4879

---

^(I detect haikus. And sometimes, successfully.) ^[Learn&#32;more&#32;about&#32;me.](https://www.reddit.com/r/haikusbot/)

^(Opt out of replies: "haikusbot opt out" | Delete my comment: "haikusbot delete")
[iix82he] (score 2, diepte 0) I worked with a few people at different jobs including Amazon who were sleeping in their car in the lot. My car didn’t start when my shift was over one time and my car was sitting in the lot for weeks but now 
 until I had the money for a tow truck. Amazon has anytime pay now so you don’t have to wait for money just be mindful. Just communicate and be up front with whoever you talk to.
This to shall pass. Hard times don’t last and you will be stronger when this is over.
[iiujj2y] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[iiypvyc] (score 1, diepte 2) You won't get fired the first time it's noticed for sure. Can do it until you get an ADAPT and then adjust.
[iix6es4] (score 1, diepte 4) Apologies. I got a different impression from your comment. 

If he can pull it off then yes I agree as well about the Amazon parking lot. Hell because of certain circumstances, even I feel safer at Amazon than in certain parts of our city. But it'll ultimately depend on the site and how much traffic they get and if security and HR care. At my site, definitely not. Not for an all day thing anyways. Others, they might care. They'll have to make the judgement call themselves.
[iivsa35] (score 1, diepte 0) If you're looking for a place, check out the roomster app. You can find reasonable stuff that's much more affordable than renting on your own.
[iivxogs] (score 1, diepte 0) POLICE POLICE POLICE call them yesterday. Say you help pay rent there even if you don't. That's illegal eviction. He also has your keys and property that must be turned over to you. At the very least the police call is evidence should you have to take him to court for your property. Also any car locksmith including AAA will let you in your car and cut you a new key. If you must sleep on your car go to Walmart. Rooms for rent are available on Facebook marketplace.
[iiwjvsm] (score 1, diepte 0) Don't tell Amazon you are sleeping in their lot, also you can go to truck stops like Pilot/ Flying J and use their showers. It çosts about $12 where I'm at. Talk to HR about what you are going through and see if they can help you with your shift. I am so sorry you are going through this OP. Also, even if you have work "friends" remember that's all they are and don't tell anyone anything. You don't want your problems spread around Amazon. Good luck!! You've got this!
[iiwzfcd] (score 1, diepte 1) Facts! A lot of people think associates are there friends..nothings wrong with saying hey and starting conversations but as soon as it gets personal I stop talking lol
[iix650y] (score 1, diepte 0) Walmart is a safe overnight sleeping just so anybody knows
[iiz57lv] (score 1, diepte 2) Good bot
[iix67k0] (score 1, diepte 0) It is highly doubtful they would "allow" you to sleep in the parking lot, but with that said, most every Walmart will allow you to stay overnight in your car on their premises. You can also try reaching out to your local city/county for any housing assistance, and if you happen to be a Veteran you can reach out to both local veteran outreach as well as the VA. Best of luck. "This too shall pass."
[iixi38f] (score 1, diepte 0) Get a Airbnb it’s cheaper. Tell them you’re experiencing homelessness. They will help
[iixoi7t] (score 1, diepte 0) I know a guy currently sleeping in his car for his 3 shifts, he's rt shift and lives 2 hours outside our fc, he sleeps in our lot for a couple nights then drives back home.
[iiy1ig3] (score 1, diepte 0) Just dont make it obvious. I was homeless for two months while working at amazon. I used to pretend i was a college student to use the gym showers. After my shift, i would simply sleep in the parking lot or nearby.
[iiy5nze] (score 1, diepte 0) Seems to me working would be you best bet. It might suck but you will be looking good on pay day. At least you will have a toilet and free water to drink at work. You might talk to police if your dad illegally evicting you and keeping your car. You ever look into military? If you "sleep" just say your eyes were closed but you were not sleeping and your shift will start in a little bit.
[iiyaoon] (score 1, diepte 0) sign up for anytime pay too if you need it
[iiycxnl] (score 1, diepte 0) If there is a Walmart close that is a great place to sleep the night.  Truckers do it all the time and there are usually alot of cameras and even security roaming the lot so you don't have to worry about anything weird happening.
[iiyhggm] (score 1, diepte 0) If you stay in California use your guaranteed paid hours so you don’t go negative ..or use bereavement 🫠
[iiynhop] (score 1, diepte 0) I don’t think they mind you sleeping in your car as long as you move it periodically like maybe once every other day or so just so they know the vehicle is being occupied and not abandoned . I don’t think they have a policy regarding how long an employee can be present in the parking lot, it be hard for them to make it fair to differentiate people who are just getting there or have been there. Plus you aren’t in the building which is the only means for them to consider you on the clock and you have your employee badge to show security you aren’t anyone sketch but I never done it so tread lightly, play the “I didn’t know that was a rule” card if you have to. Good luck stay safe
[iiz6dch] (score 1, diepte 0) To be honest I’d go in if I were you. Sounds like you need the money now and it’s at least a roof over your head until you get back your car. As far as sleep, sleep in the least populated break room off the clock for as long as you can until someone tells you to leave
[iizg4sw] (score 1, diepte 0) If I were in your situation I would get a planet fitness black card 22.06$ every month free shower bathroom wifi massage and you can stay and just sleep at the parking lot if they try to kick you out just say im here to workout I got my gym membership.
[iiuybs5] (score 0, diepte 1) Agree. Take some of that $100 and catch a bus or something to get there.
[iix2c10] (score 0, diepte 3) I am well aware of it being a saying but i disagree sleeping in your car in your in Amazons parking lot is "shitting" where he eats. Worst case scenario Amazon asks him to stop doing that and he agrees, worst case scenario him sleeping on a randomly parked street is he gets robbed or ticketed by cops
(2 reacties met lagere score weggelaten)

