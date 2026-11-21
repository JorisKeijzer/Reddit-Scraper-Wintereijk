# Label-batch batch_0106

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
Schrijf het resultaat naar `batch_0106.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1otbqi3, 1fy3sv5, 199uelt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1otbqi3 ===
SUBREDDIT: r/CampingandHiking
DATUM: 2025-11-10  SCORE: 33  REACTIES: 101
TITEL: It’s frustrating to be unable to hike or ruck because of plantar fasciitis, and it’s so hard and expensive to treat
POST (source_id=post):
I am 6 feet, male, 160 pounds, and 24 right now. I got plantar fasciitis six years ago from running, where I just ignored the feet pain and kept pushing until it became something that won’t go away. The pain is mainly in the arch area, and it’s a sharp feeling.

I been through so many doctors and tried physical therapy, steroid injections, icing, rolling foot on a ball, night splits, and basically everything short of surgery. Nothing helped. X rays and MRIs showed nothing, but all of the doctors I have been too are confident that it’s still plantar fasciitis. It hurts to walk and stand now, and I am worried I have to live with this forever. I don’t want to do surgery because it often can make things worse. I want to get back to being able to do physical activities with zero issues

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[no3fwsu] (score 43, diepte 0) Are you in firm-soled shoes or squishy-soled shoes?  

If you're in one, try the other, as at the point you're at it doesn't sound like it can hurt to try.  My wife got advice both ways on this one, and eventually found "always wear incredibly squishy sandals around the house/never go barefoot" to be what worked for her.  The squishy ones were Oofos, I think.
[no3jwc9] (score 28, diepte 1) I also wouldn't suggest going to a quack.
[no4bdv7] (score 22, diepte 1) That was the same for me. I switched to Crocs for house shoes instead of barefoot and it made a world of difference.
[no62z7m] (score 21, diepte 0) OK finally something I can meaningfully contribute. 

I struggled with this for years. I mean YEARS.  I tried everything.  Pushing through, resting until it feels better, new shoes, over the counter insoles, rolling, stretching, all of it. My soles were so tender just touching them would make me jump and they would tighten up at night and literally curl down when in bed.  

I was getting depressed about it.  What changed me completely was going to a podiatrist, a good one.  She told me so many things about my feet and then scanned me for custom inserts.  Yes they were expensive, like $500 but last years and you can move them between shoes.

I don’t run but I can do everything else pain free.  She also recommended a bunch of running and hiking shoes that are better for our feet.  Lastly she told me about Oofos to wear around the house.  I also were them around town/beach etc for more casual footwear when doing things outside. 

Definitely go to a podiatrist!  I resisted it for years as I thought they were low level docs for some reason but they can be amazing and extremely knowledgeable and effective.  This also cured my knee pain as well.
[no3gakn] (score 20, diepte 0) I personally would never suggest a chiropractor.  I just don't trust them as a whole.  My work at the time had free access to a sports medicine/chiropractor who treated my Achilles tendon.  The sessions were borderline excruciating the first few times.  

Ask around and see if you can find more people who have had the treatment.  It was explained to me that the tendon was acting more like bone where it met the bone. It completely fixed the problem at the time.  I rarely have issues with it now, and that was at least 6 years ago.  This was after having pain for many years prior. My doctors had been telling me to take ibuprofen. A few weeks of very painful treatments fixed it.
[no3e3mw] (score 14, diepte 0) Do you stretch and roll your calves every day?
[no4txf1] (score 12, diepte 2) My dad ended up with a boot he wore to bed for a few months to keep the ankle flexed back. That and daily stretching with toes up against the wall.
[no451n0] (score 9, diepte 1) Am I the only one confused by this comment?

You do NOT recommend what you say completely fixed the problem after years of pain?
[no3jfk5] (score 8, diepte 1) I don't want to claim that this universally, works for everyone but I second this suggestion - it worked for me.

 I had plantar fascitis of varying intensity for 3 years and it completely went away after a few weeks of barefoot shoes and never came back again (except when I dare to wear regular shoes again for a few days but even then it's gone quite fast). A flat sole (it can have a bit of padding but no "arch support" ) and wide toe box are key for me. For hiking I use exclusively Altra and I love them so much, no more problems with plantar fascitis at all even after 30+ km. You need to get used to it, don't push it too much in the beginning and gradually build distance, but your feet should slowly adapt. 

So I definitely recommend that you try it at least, it sounds like you have nothing to lose!
[no3gxh2] (score 8, diepte 0) I’m guessing you’ve already tried these, but they are about that only thing that’s worked for me.

https://www.amazon.com/Dr-Scholls®-Fasciitis-Cushioned-Compression/dp/B0CWVT8CTZ/ref=mp_s_a_1_23?adgrpid=54480336365&dib=eyJ2IjoiMSJ9.OU5zk53qM8FN2ALi1ad43iW3eiZdyib1OFpJ_And7YFEFkZgNOZoUtgBLSLvUOdv2WpMqQD0HMhd6mNblMOWOLQyfkxAgJDEfG2VHbbn-zpyU5oNfMyJYCKaMKCqixZ-IsKTrzJOjgSqTTx4AQIVpW8JO5Hz133MSRicnmXcSps1YhoCXowtd3U4_JjzxG4jqA3-F2sX4hyOLlf4CoJAeg.W776Snfu8z83QruB3Awxu0xUw-mdiBCzUt3oEDm0ZAg&dib_tag=se&hvadid=776666371086&hvdev=m&hvexpln=0&hvlocphy=9012430&hvnetw=g&hvocijid=12550633033985947661--&hvqmt=e&hvrand=12550633033985947661&hvtargid=aud-2443140925601%3Akwd-302094058258&hydadcr=7820_13829148&keywords=plantar+fasciitis+inserts&mcid=5530400c820a3fc889100bcc90ca795a&qid=1762777778&sr=8-23&xpid=F_3g3VpIoElq2
[no3jwx6] (score 8, diepte 0) Mine went away after as steep downhill that was nothing but rocks for several miles.  Something about the beating my arch took made it go away.
[no4qkm2] (score 8, diepte 0) I ripped my fascia during a backpacking trip and developed plantar fascitis from that. I had to switch to ultralight backpacking + doing specific foot stretches, religiously, every 20-30 minutes. I dont get the miles, but I still get the views and the solitude.

I hope you're able to work something out. Good luck!
[no40tgh] (score 6, diepte 2) Removing insoles won't make a standard shoe zero drop or barefoot- you should get a pair of shoes for purpose.
[no8bwl9] (score 6, diepte 3) I didn’t assume anything. I simply read what the person wrote.
[no3w2tr] (score 6, diepte 0) Compression socks help. They didn’t cure mine, but they helped significantly. If you’re using proper insoles, stretching, icing, and using the roller ball regularly, it can’t hurt to add compression and see if they help you.
[no6lr5i] (score 5, diepte 2) 100% - this was my cure years ago, long before Crocs became cool.
[no7rgq1] (score 5, diepte 3) They never became cool, but I am glad they helped :)
[no4jp0m] (score 5, diepte 1) "It completely fixed the problem at the time" 


What is "it"?
[no5yn2k] (score 5, diepte 0) Just went through something similar. My friend who teaches ballet taught me some great calf-ankle ballet movements and simple exercises that have been amazing, I would recommend googling ballet moves for plantar and try them out.

I would also say, everything is connected so if you have focused your treatment on your foot, maybe the problem is actually in your hips or lower back. Men don’t always stretch as much as they need in the hips, if you aren’t already start doing hip flexor stretches.
[no3dhcb] (score 4, diepte 0) Go barefoot and learn to walk properly. You need to get rid of arch support shoes and let your feet get stronger by themselves. This is something that takes time, so introduce it gradually and listen to your body. 

What shoes are you using that are not working? And what distance and terrain are you trying to hike on?
[no3i0ya] (score 4, diepte 1 OP) I do.
[no8svyj] (score 4, diepte 2) Birkenstocks work too. Wearing shoes with high arches or an insole like the Superfeet Green insoles can really help too.
[no71qlg] (score 4, diepte 2) There is no compelling evidence that Chiropractic is effective at treating anything and there is not enough  data to back up its safety. 

It's psuedoscientific quack medicine and you're making a very tenuous assumption that the Chiropractic treatment is what fixed the problem and not natural healing.
[no3yutp] (score 4, diepte 0) If your feet also fall asleep or stay cold while hiking, look into popliteal artery entrapment syndrome. After PF surgery, that turned out to be my solution
[no4htr0] (score 3, diepte 2) Flat terrain might be your problem too. Try a gradual uphill or even a treadmill with an uphill setting. Flat isn't doing anything to stretch your calves - it's just pure impact on your feet. An uphill climb will engage your calves and cause you to stretch and pull and work that muscle that connects from your calf to under the bottom of your foot.
[no57274] (score 3, diepte 1) My good friend, who is a massage therapist a sports medicine clinic also swears by this. I am a server/bartender and my plantar fasciitis/arch pain went away when I stopped wearing arch supports every day & prioritized shoes with a larger toe box. My feet were able to gradually get stronger on their own after that.
[no3opxs] (score 3, diepte 0) Are you wearing the plantar fasciitis boot every night when you sleep?
[no4gh64] (score 3, diepte 0) I know we're going into winter in the northern hemisphere, but wearing Chaco sandals with the toe loop, strengthened my feet and my issues with plantar fasciitis eventually went away after about a month and have stayed gone for the most part.
[no7b1d1] (score 3, diepte 0) You need to see a foot doctor.
[no3i41x] (score 2, diepte 1 OP) I already tried removing the insole, and it just made things worse. I am just trying to hike on flat terrain right now, which I am not successful at
[no639g5] (score 2, diepte 2) Find my parent comment.  People with what we have should never really be barefoot on hard ground.
[no3s4hj] (score 2, diepte 1) Yes. It may take a year or so.  But my pain is gone.  Calluses or they resolved.  Running is great cardio but very tough on the body feet to neck.  I gave it up so I could hike further into my age/life
[no3j7b9] (score 2, diepte 2) Dang. Maybe try a course of injectable peptides.
[no8at3u] (score 2, diepte 1) After a few years of pain and $1,500 in orthotics I now wear Chuck Taylor Converse All Stars and Sanuks or Dudes.  These shoes are flat with a little bit of sponge.  My feet are much happier.  I will wear Keen’s when hiking but my feet can handle it now.
[no7v7gf] (score 2, diepte 1) This has really helped me.
[no3rhao] (score 2, diepte 0) Sole high arch insoles worked for me. 

Cork bottom, cut to fit your shoe. Rei should carry them.
[no3u005] (score 2, diepte 0) I dont have the same exact issue, but I also have serious medical foot issues that have basically eliminated my ability to hike for now. I've picked up biking instead to stay in shape and get out still, but like you surgery is my last option. If you can afford the surgery I would say go for it, and then really take your time with the PT afterwards to rebuild that area and avoid complications. I just can't afford my surgery so im stuck this way for now. Beat of luck with whatever you decide to do friend, and be nice to your body.
[no41rka] (score 2, diepte 0) Get a Dorsi Flex and go slow.  I’ve saved myself and several others from pain with it.
[no41uea] (score 2, diepte 0) Do you have plantar fasciitis on both feet? This is generally due to a core stability issue. Do you also have back pain? If you’ve spent time and money treating the foot/feet directly, you likely need to look farther away from the problem. Gait is very complicated and involves many joints and muscles; is your hip mobile, can you stabilize your low back etc. 

What part of the world are you in? Maybe see if there is an AiM practitioner near you https://findingcentre.co.uk/find-help/ or someone trained in PDTR https://p-dtr.org/find-practitioner/

You may also need to strengthen the small muscles of your foot- these are great exercises to start with https://zhealtheducation.com/blog/strong-feet-strong-foundation-episode-338/.
[no4inxe] (score 2, diepte 0) The Walking Company Plantar Fasciitis orthotics changed my life. I went from barely able to walk to 12+ hours on my feet without a problem. Still use them in my walking/hiking shoes. I stopped being able to walk barefoot around the house. Aetrex flip flops were such a relief to my aching feet. They have some squish, but there is an orthotic inside. I will always own a pair.  

Between the orthotics and the flip flops, I have been pain free for years. Much better than the boot and keep your feet up advice I was given by my podiatrist.
[no4iq7q] (score 2, diepte 0) Yeah pain sucks I can agree with you there.
[no4o2sx] (score 2, diepte 0) Look up Squat University on YouTube and see what he has to say about PF.
[no4x0bh] (score 2, diepte 0) Cycling was a great therapy and recovery for me. I bikepacked the CT and AZT after ruining my foot on the CDT during a spring thru-hike attempt. 

The cycling mixed w occasional pushing was great therapy. 

Fortunately your body weight is good as that’s often an issue. 

Hoka’s for daily wear and PowerStep Pinnacle insoles worked for me. My PF has not returned when walking, running, Month long backpacking trips. 7 years in later.  

I’m a big fan of a whole food, nutrient rich, mostly plant diet now. Can only help…
[no6ztsm] (score 2, diepte 1) Power Step Pinnacles were the solution for me. Went to a podiatrist who suggested those first before considering custom orthotics. I used night splints until the morning pain got better and never stopped using the Power Steps.
[no5u4q7] (score 2, diepte 0) This may sound stupid, but have you tried prescription insoles from an orthopedist (you don‘t mention it)? I have plantar fasciitis too, two days after getting the insoles all symptoms vanished.
[no5zind] (score 2, diepte 0) Road runner sports has awesome custom insoles!  They’re like $100 or so but worth every penny.  Took all my arch pain away and helped my elderly parents too! Just a happy customer… also for heel pain oofos are amazing.
[no8g7kh] (score 2, diepte 1) Good way to test this is when you engage your glutes while standing up, your feet automatically align and lift up your arches. Glute activation is very important, especially nowadays where almost everyone sits all day
[no6bzjz] (score 2, diepte 0) This must be tough. Did you try to look into a specialist who focuses on movement analysis or biomechanics? Like a sports podiatrist or physical therapist who can do gait retraining or assess load distribution while walking.
[no73vpl] (score 2, diepte 0) You might be doing so much to try to heal it that you’re hurting it. I’ve dealt with it twice (about 10 years apart, same foot) and it didn’t start getting better until I started taking rest seriously. No shoes or anything constricting on it in the house, no rolling, minimal walking when I didn’t have to. Sucks to do but I was in the same position as you. 

Rolling my foot with a lacrosse ball was such intense pain that after a week or two of doing it, I came to the conclusion that it was doing more harm than good. 

Hope it helps, I am NOT a doctor. Just speaking from my personal experience.
[no7i2mz] (score 2, diepte 0) It’s so painful. I was told do the cortisone shots and go do PT. I bought HOKA Bondi’s for walking, HOKA Speedgoats for hiking and oofas for inside the house. I try not spending much time without shoes on. Do the stretches given by PT, especially standing on the edge of a step and dropping your heels down. Changing shoes totally solved my PF. Good luck!
[no8gcwo] (score 2, diepte 0) This dude is so weird! He posts this all over ultrarunning and even the LetsRun message board. He doesn’t really want help, he just wants…. I’m not sure? Anyway, it’s the dude! He’s here now
[no5h4mb] (score 1, diepte 2) You want the sole of the shoe to bend with the foot without resistance.  I can roll my boots up and stick them in my pockets if I wanted to. The soles of my boots are probably about as thick as the inside that you removed. I recommend shoes from a company called Magical Shoes.  Some of my friends like Vivo Barefoot shoes, but I haven't tried them.  Merrell's helped me for a bit, but the pain eventually came back even in those. Haven't had any issues in Barefoot shoes.  I didnt even have an adjustment period, but I have also primarily been Barefoot the majority of my life.  I hate shoes lol
[no6pxwo] (score 1, diepte 1) I was able to resolve knee and hip pain by switching to barefoot style shoes. Running up to six miles in flat 4mm hand cut sandals. Did barefoot hikes (no shoes) up to 11 miles in length. Spent almost all of my time in either barefoot shoes or going barefoot. I did this for over ten years, covering up to 15 miles a day with no problems. Just within the last year I have developed plantar fasciitis. My personal experience is that barefoot shoes are not a panacea for foot issues.
[no8ftq6] (score 1, diepte 1) Yup, this worked for me. The trick was to buy shoes with a bigger toe box and go barefoot as much as possible otherwise, relearning how to walk and listening to my body. PF gone for good
[no7x451] (score 1, diepte 3) They are good at doing manipulations that can help sometimes but everything else is complete BS. I have a back issue that gets fixed but I do not come back multiple times or do any of the adjunct things they offer.
[no99aw4] (score 1, diepte 3 OP) How long does it take to heal? It already has been 5 years for me
[no99er9] (score 1, diepte 4) Go to a real doctor.
[no9bcx2] (score 1, diepte 5 OP) I been through two podiatrists and one orthopedist. They didn’t help
[no6tsij] (score 1, diepte 1) What a strange condition. I have recurring plantar fasciitis, and this kind of hiking is absolutely guaranteed to bring it on for me. 

Downhill is the worst (for me) because my calves don't stretch out, and rocks make me go slower, so I'm doing the bad hiking for longer.
[no3oyud] (score 1, diepte 0) See if you have a Good Feet store near you. They can make a difference in how wearing a shoe feels. Helped cousins back pain after they went.
[no4028j] (score 1, diepte 0) I also suffer from PF and bone spurs. Got to the point of crawling to the bathroom in the morning and just suffering on my feet at work all day before finally seeing a podiatrist. 

Night and day. Doc suggested a set of insoles -PowerStep PULSE Performance Insoles | Running Shoe Pain Relief Orthotic - and for the first time ever the insoles helped. 

I get new ones every 3month, and replace my shoes at least annually now. I'm wearing good hiking boots, just with these insoles, and I can feel the insoles wear out by the end of month 3. Then the new ones show up and I feel great again. 

Doc also told me to stop going barefoot (which is my preferred state), so I eventually took that advice too and bought the recommended OluKai sandals for the house.

Hopefully you find something that works for you.
[no46qdg] (score 1, diepte 0) Coudl have written thid. I really think docs havent a clue  I wish they were honest bout this.
[no47p20] (score 1, diepte 0) Try those insoles with the dozens of little bumps all over it. They work wonders for me
[no48dfl] (score 1, diepte 0) Some of the best advice I got was to flex my feet upward in bed before I get up in the morning. It stretches out the plantar facial ligament so it doesn’t snap when I get up on my feet. It helped more than anything else. I tried. Good luck, I hope it gets better! Plantar fasciitis is a nightmare.
[no4ac6k] (score 1, diepte 0) I had it, and yeah it's miserable. Nothing I tried had much effect.  After about a year, one day it was just gone.
Just hoping I never get it again!
(35 reacties met lagere score weggelaten)

=== THREAD 1fy3sv5 ===
SUBREDDIT: r/CampingandHiking
DATUM: 2024-10-07  SCORE: 21  REACTIES: 86
TITEL: Plantar fasciitis sufferers how do you hike?
POST (source_id=post):
I missed out on a lot of hiking this summer and I'm trying to get back to it for the fall. My issue is that the plantars fasciitis in my right foot is more painful than ever. My doctor wants me to start getting cortisone injections. I know a lot of people successfully hike with this condition so just wondering what you all do to manage the pain during a hike? I'm hoping there's a magical non drug related solution I've missed.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lqrfv1m] (score 23, diepte 0) Go see Physio. Do exercise and stretches they tell me.  Stop going barefoot or wearing cheap sandals for a while.  By SOLE insoles for all of my shoes to support arch.  99% better.
[lqr6s90] (score 21, diepte 0) For me it’s the shoes. Altras have been a godsend for me. The zero drop has been the only thing to alleviate the pain after 12 hour shifts. Anything with a heel just exacerbates the problem. They’re expensive and they don’t seem to last as long as other brands but the trade off is worth it. They make a high top trail runner if you need the ankle stability but any of their trail runners have been great in my experience. 

And the stretches of course. There’s 3 or 4 different stretches you can do before and after a big day on your feet that really help.
[lqrrn7a] (score 15, diepte 0) For me, the magical non-drug related solution was losing weight. I started on keto, and dropped about 105 lbs. I haven't had PF symptoms in years. Also, keto is anti-inflammatory, so that also helped. I'm 53 and on zero meds.
[lqrf7y1] (score 11, diepte 0) I know a couple of people who battled PF and you really need to address it. Go to physio (see a physio instead of a doctor), do the stretches and exercises, actually let your body heal instead of trying to push through it.


Both friends are back to hiking now.
[lqryoxi] (score 10, diepte 1) Stretching can be incredible for PF. I suffered for *years* with knots on the bottom of my arch. My podiatrist's assistant taught me some simple stretches and mine completely went away. It was like magic and wish I hadn't suffered for so long without going to get it checked out. I seriously thought they would need to be cut out, but nope, stretching was a simple fix.
[lqrrlt6] (score 8, diepte 0) You need to see a good physical therapist and learn how to strengthen the foot. Plantar fascitis is not a life long permenent condition, it is just a result of weakness in some difficult to train muscles but it can be fixed over time. Take the time to fix it and you'll be set for life, there's no drug or surgery that can cure it just needs specific exercises
[lqr8kf8] (score 6, diepte 1) Altras work for me too for that specific issue on daily life. Normally i use barefoot shoes but sometimes that irritates my plantar fasciitis and i have to use Altras for a while again. It's like walking on cloud.
[lqra7vm] (score 6, diepte 0) I have P.F. Mine came from walking on concrete floors and boating without shoes. Mine had gotten so bad that it was becoming difficult to stand in the morning.  I discovered Hokas, and, honest to God, I've had zero foot pain for 7 years now. I am on my feet for the better part of 12 hrs a day and on concrete floors. I've not tried them, but Hoka does make a hiking boot.
[lqry9zz] (score 6, diepte 2) My podiatrist saw my inserts and asked me where I got them because he liked them so much he wanted to recommend them to other patients. They are very affordable and I swear by them. WalkHero on Amazon.
[lqrsa3c] (score 6, diepte 0) My podiatrist had me stand on a device that measured my arch.  Sent the results away for some custom made insoles. I wear them everyday and I’m 100% pain free.
[lqrtna0] (score 5, diepte 1 OP) It's funny you mention the zero drop because the foot and ankle specialist I'm seeing thinks my Altras are part the problem by not providing arch support. But I also don't trust she's not just trying to upsell me her orthotics lol.
[lqrsfpx] (score 4, diepte 1) +1 on the zero drop shoes, no particular brand though. I wear water shoes 90% of the time.
[lqs7ega] (score 4, diepte 1) Yes, walking pain immediately after getting out of bed. 
I now do ankle rotations, left circles then right circles. Both feet. 
Also, take a towel or the bedsheet and loop around sole of foot and stretch toward you. This horizontal calf stretch helps!!!
Then I can walk, not limp, to the kitchen and feed the impatient cat.
[lqsvct4] (score 3, diepte 2) Zero drop shoea cause PF for me.

The best thing I've found is Tibialis Anterior raises  (shin exercises).  Strengthen your Shins! To balance out the strength of your calf's
[lqryum0] (score 3, diepte 2 OP) Thanks. I do this every morning too. It helps
[lqs7nw9] (score 3, diepte 2) P.F. absolutely sucks. I cannot recommend Hokas enough even for just everyday work and life.
[lqrpfda] (score 3, diepte 0) I’m a letter carrier (mailman) and had plantar fasciitis for years. Every physio and doctor I went to gave me different treatment plans, exercises, equipment, socks. All of them, different. So inconsistent.. nothing really worked. 
I went to a chiropractor (a field I don’t acknowledge as legitimate) because a colleague really insisted it worked. Figured I would try, since nothing else works. He did one of those laser gun treatments. Also didn’t work… lol

HOWEVER he watched me walk, and observed that I was putting my weight on my arches. He said to practise walking by having my big toe make contact with the ground first. 

Somehow no physio therapist or doctor made this observation?? Really made me dubious of physio and athletic therapy.. how do half a dozen medical professionals miss this factor? Anyway.. 

So I did that, and it seemed to be doing something. I did it more and more, then practised with zero shoes - lo and behold, my feet are 90% improved. I can walk bare foot and in cute shoes without being crippled into my knees and hips for days. What a treat! 

Turns out, I walk like a flat footed Luddite and that was damaging my PF. Using the toes and spreading impact, while not letting my foot flatten, did the trick. This same chiro guy also suggested exercises where you’re tensing your foot, as if trying to grip the floor. Seemed effective. 

That being said, I wear hokas for daily use and work. Couldn’t recommend them more.
Clifton 9 are amazing for my feet. I tried 3 different models of Hoka, multiple ASICS, and keen shoes. Hoka are best for long use on pavement.
[lqrpgvw] (score 3, diepte 0) As others have said the pt is really Important. PF ruined a year of hiking for me, but doing the work, buying new boots and also making sure my casual and work footwear were correct is what brought my feet back to life.
[lqru6jb] (score 3, diepte 1 OP) Okay yeah this might be the way to go. I also did that- it recorded my gate and everything to see exactly how I step/walk.  My insurance doesn't cover them but might be worth it to pay out of pocket.  Do they jam up your hiking shoes?  Did you need to size up?
[lqs9cuw] (score 3, diepte 0) I have in both feet. 

Saw physio, did stretches, did strengthening exercises, and I'm massively better. It took three months and I have to maintain the stretching, but it's now gone, and I don't need some special shoe or anything extra. Highly recommend. Heal yourself
[lqvjefq] (score 2, diepte 2) I had precisely this situation in college. Arch support aggravated the problem. Getting into barefoot shoes (I have worn nothing but Innov8 F Lite 195’s for the last 20 years) is what fixed it. 

That and intentionally exercising my ankles, keeping the calves and hamstrings loose so they don’t pull on the plantar fascia. 

Twenty years PF free…until I went hiking last weekend in hiking boots. 

Sigh. I’ve been an office drone and haven’t been hiking/running in years. Time to get back in the saddle!
[lqvu8l8] (score 2, diepte 3 OP) Oh no!   Hopefully you get your feet back to normal soon
[lqruct1] (score 2, diepte 1) I 100% agree with the hokas. I no longer have PF also believe rolling your feet with a frozen bottle of water a couple times a day is key
[lqt8hvm] (score 2, diepte 2) Search Amazon for 'Night Sock', it really helped with my morning pain, since it basically lets you do your stretch all night while sleeping.  Also stepping right into a sandal  with arch support instead of barefoot or slippers with no support.
[lqrjdqg] (score 2, diepte 1 OP) Great points!  Appreciate it!
[lqrpmwa] (score 2, diepte 0) Hokas.
[lqrwk1x] (score 2, diepte 2) I hear you.  I have hiking friends in the same situation and Altras are the ticket.  I have a wide toe area and have to get Hokas 1.5x-2x sizes bigger, and Wide when available.
[lqsb7fn] (score 2, diepte 2) Right, it's not a single one it's multiple muscles. The vast majority of modern humans have extremely weak intrinsic foot muscles and that causes many of the issues we see with foot pain. Can be cured through specific exercises done consistently. I've cured mine and done the same for more people than I can count, I'm not some foot genius it's just basic rehab
[lqyxfpg] (score 2, diepte 5) A well designed clinical trial would support the narrative. But it's my understanding that there have been multiple studies that show evidence to the contrary. Things like massage, laser, ultrasound, stretching, kin tape, muscle imbalances, cupping, chiropractic, are no more effective than placebo. Even surgery is often not well supported by evidence in many instances. Pain is complex and multifactorial. There are psychosocial factors on top of the biological factors that contribute to it. We are not machines that can necessarily be "fixed" with just exercises, or just stretching, or just this one trick. To make things more complicated, we often can't really tell what made us feel better, because most people get better on their own anyways.
[lqtx74a] (score 2, diepte 2) It's really dependent on the soles and the shoes. They absolutely fill out your shoe/boot and if it's already a tight fit can force you to size up. Worth it though.
[lqrv962] (score 2, diepte 0) How long have you had it? I got 3 cort injections without improvement and then got the topaz surgery. My foot is perfect now. Very minor surgery (although they have to put you under anesthesia).
[lqs2d1o] (score 2, diepte 1 OP) 3 yrs now and it used to be manageable by avoiding heels and doing the stretches. Now I'm just always in pain. Sometimes even after wearing the boot thing when I go to stand up I fall if I put weight on it. It's that painful.  I'm not being a baby it's really impacting my life. I used crutches for a day last month after I walked my dog on the beach in Tevas sandals.  I'll never make that mistake again.  I just want to get out there and get hiking again.   Surgery is a last resort I guess.
[lqs49jd] (score 2, diepte 3 OP) And that is exactly how this most recent podiatrist has been heading. I keep resisting the orthotics due to the cost and I heard that once you go to a custom orthotic, you never can go back. But I guess that's a silly fear since I'm missing out on things I love in order to be stubborn
[lqs4tia] (score 2, diepte 4) Fwiw, after the surgery, I don’t use any orthotics or inserts. I can walk barefoot at home. I occasionally need to stretch my calf, that’s about it.
[lqrvvlq] (score 2, diepte 0) One thing that has helped me is . . . hiking! I treat it like physical therapy. The uneven ground is so much better than concrete and pavement and the varied terrain helps me stretch my tendons.  The first day or two hurts worse but by the end of a week, I’m floating! I concentrate on using my body fully - not babying the painful bits, but trying to take those steps strongly and equally for each foot. The  benefits last for several months, but slowly fade as I spend more time on flat hard surfaces.
[lqs3p17] (score 2, diepte 1 OP) I've seen a podiatrist (she says foot and ankle specialist) for 7 months now.  Shes been trying to push custom orthotics on me but I've been resisting. I might need to give in. I could stand to lose some lbs!
[lqs1shd] (score 2, diepte 0) HOKA hiking boots and lots of stretching.
[lqsk24q] (score 2, diepte 2) Yes, was painful and really hindered me from hiking any long distance and walking the dog. However physio has given me confidence back in my feet. It's worth the money and many appointments. Give it a go!
[lqt2hpt] (score 2, diepte 0) Physical therapy and better shoes.
[lqt5hry] (score 2, diepte 0) Stretching and exercising have completely cured my PF. I had tight calves that was causing mine however, yours might be from something else. In the meantime get some orthotics and good shoes like new balance, Hoka, Keens.
[lqtdbyd] (score 2, diepte 0) Superfeet
[lqvtwg0] (score 2, diepte 1 OP) I had not but looked it up just now. Interesting. Sounds a lot like the therapy my old podiatrist did.
[lqv2k33] (score 2, diepte 0) Most likely it's your hips being weak that's causing your plantar fasciitis. Please see a decent PT before you agree to the injections.
[lqv331y] (score 2, diepte 0) Buy KT tape and wrap your foot. I tried everything and this is the only thing that helped me heal. Plantar fasciitis is tricky cause your foot heals as you sleep and when you wake up, you step on the ground and it immediately tears again, that’s why it hurts first thing in the morning. 
Using KT tape and leaving it wrapped allows you to have support at ALL time.
Search up the proper way to wrap your foot with KT specifically for plantar fasciitis.
[lqvitl8] (score 2, diepte 0) Had this twenty years ago in college. Insoles and arch support for some reason made it worse. 

What helped was doing a lot of foot strengthening exercises. 

First thing in the morning I would walk 50 steps tiptoe, fifty steps on my heels, fifty steps toes out. Fifty steps toes in, fifty steps sideways right, fifty steps sideways left. 

Basically iterate variations of movement to work the ankle, calves and knees through all ranges of motion and warm/loosen them up.
[lqrde4r] (score 1, diepte 0) When hiking the best pre-emptive method for me has been to wear old-fashioned, rigid hiking boots by Meindl. Going for flexible soles is asking for trouble with my feet.

Once it's going, I haven't really found better ways than to roll my foot on a hard ball, and do calf stretches. It does take time to recover from.
[lqv73j8] (score 1, diepte 2) Seconding this! A friend of mine got cured by insoles, so because of her recommendation, I tried the same insoles she did and later two other models, but all of them made the problem worse. 

What helped me was a physiotherapist who made me do stretching exercises, massaged the foot and tugged and roled the ankle joint. Still, even after the physiotherapy, it wasn't completely gone. What helped me heal the rest of the way was taping the foot. There are different taping patterns that mostly seemed to work equally well, here's an [example](https://www.youtube.com/watch?v=jtvMwU-er98). Taping also helped a lot to reduce the pain when I went hiking.
[lqrj72h] (score 1, diepte 1 OP) Now the insoles I haven't tried yet. Thanks!
[lqyd1ep] (score 1, diepte 2) SOLE inserts are unique in that you warm them in the oven, then stand in them as they cool to conform to your feet. Be sure to read the instructions on the box.
[lqsslkb] (score 1, diepte 1) I go to PT and do exercises daily. My PT suggested barefoot while at home. So dome conflicting info. But the exercises really, really help.
[lqrp41g] (score 1, diepte 0) Too add and agree with what's been said, I never walk around my house barefooted and always wear the slip on slides. The cushion to my heals really seems to help. I reached a point where I almost couldn't walk, and now I only occasionally have issues.
TLDR: Never go barefooted
[lqrybg2] (score 1, diepte 1 OP) Ah thank you!  So years ago I saw this "holistic podiatrist" as he claimed to be and his thing was to wrap his patients feet to correct their individual issues and he did this by observing the way your foot made contact when you walked. Very similar to what you're saying. He claimed I would be walking - toes first instead of the inside of my flat foot hitting the ground first and that it would cure my pain. I never followed up with him because I was pregnant and the wrapping was dangerous on my 3rd trimester swollen feet lol.  Funny enough though I was there for ankle pain from a past sprain and hadn't developed plantar fasciitis yet. He told me I would if i didn't stop walking that way. I thought he was nuts. 
I used to wear keens and New Balance. I have bunion issues from an early "career" as a dancer but that same podiatrist told me I would have developed them no matter what shoes I stressed my feet out in because of how my feet are shaped and how I walk. He also said my unborn child would also have my foot problems guess what? she does.  I think I misjudged him. 
Anyway - how long did it take you to train your feet and would you say that hokas are somewhat wide at the top?  The toe box on Altras is what keeps me dedicated to them.
[lqtd789] (score 1, diepte 2) It only took a couple months of doing the “foot scrunching” exercise and time walking in “zero shoes” to notice progress. 
I wouldn’t say I’m cured, but it’s miles better than it used to be! 

Hoka are known to be reasonably wide to begin with, but also come in optional wide size 😊
[lqruqig] (score 1, diepte 1 OP) I've heard they're cushier than Altras. I need that wide toe box though.  My feet are very thin but wide at the top due to years of dancing I developed bunions. It sucks to wear anything that compresses that part of my foot. What type of hokas do you wear?
[lqxfe61] (score 1, diepte 2) Hoka are almost all thick. Altra vary from fairly thin to just as thick, the difference is Hoka are narrow & have typically 8mm drop (started running in Hoka years ago, now only Altra for me)
[lqwive3] (score 1, diepte 3) There is no evidence to support this narrative.
[lqyjp4i] (score 1, diepte 4) What type of evidence would change your mind?
[lqz3xi8] (score 1, diepte 6) I don't necessarily disagree with the majority of that, but if there's any chance simple exercise can "fix" something we should try it first since it's free and there's no side effects unlike more invasive procedures and surgeries. Modern people are very weak, and many soft tissue issues are directly caused by weakness and the cure for weakness is targeted exercise
[lr7ufhf] (score 1, diepte 7) Weakness doesn't cause soft tissue issues.
[lqszz5b] (score 1, diepte 2) Nah. I throw them in all my shoes. Never had an issue. Real thin metal. Your dr should determine the size.
[lqs3quu] (score 1, diepte 2) 3 years is a long time. The surgery has a short recovery time. It’s minimally invasive compared to the old style of surgery. A good doctor will start with a custom orthotic with cort injections. If that doesn’t work, topaz surgery is the next move, imo
[lqrvf1z] (score 1, diepte 0) Exercises/stretches for it.
[lqrziwl] (score 1, diepte 0) Schedule an appt with a podiatrist. I’ve got tailor’s bunions (basically wide feet) and my daughter has plantar fasciitis and does cross country. For both of us, the insoles/inserts (that they can measure your feet for) have made a world of difference. I totally did not want surgery. I’m on my feet a lot at work, and also enjoy hiking. Doing Keto and working out to become healthier and maintain my weight also helped.
[lqsjdg3] (score 1, diepte 1 OP) Both feet?  Yikes!
[lqsgbpy] (score 1, diepte 0) In contrast to some of the other commenters, what tends to help me is wearing heavier, chunky mid ankle boots. 

The podiatrist recommended footwear that is supportive and not flexible, and that seems to be working for me
(34 reacties met lagere score weggelaten)

=== THREAD 199uelt ===
SUBREDDIT: r/Disneyland
DATUM: 2024-01-18  SCORE: 12  REACTIES: 75
TITEL: Recommendation for comfy shoes to wear with plantar fasciitis, high arches, heel pain
POST (source_id=post):
I've been to Disneyland many times. The one downside to all the visits was foot pain after walking around. I have PF, high arches, and have tried different shoes and inserts, and inevitably, heel pain would put a big damper on my day. I tried Merrell Moab low hiking shoes, Asics so far, and a few others I can't remember.

A thread came up about Hokas being good, but they look pricey. Are there any budget to mid range $$ shoes that can do a good job at keeping me pain free for Disneyland? I just bought a Magic Key so I will be putting a lot of miles on my feet.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kigk2ym] (score 52, diepte 0) I would recommend going to a running specialty store and have them analyze your walking/running. They will suggest a perfect shoe for you! In my experience you are under no obligation to buy what they suggest so you can take that information and find that perfect shoe.

Even if you aren't a runner it's a nice thing to do. That being said I can also vouch for Hokas and Nike Trail Runners. After a LONG day my feet might hurt a little but in general I'm great.
[kigjfel] (score 26, diepte 0) Budget ain’t getting it done. Hokas aren’t magic but they work well for a lot of people. You can get them a bit cheaper at Nordstrom Rack and I’ve seen them at Ross once or twice. Usually discontinued models. Go for the Hoka Clifton with your high arches. The Bondi is also popular because it’s very cushioned but I find them a bit cloddish feeling.
[kigtbct] (score 21, diepte 0) Honestly, given your foot issues and your desire to making the most out of your parks experience with your new pass, I'd recommend going to see a podiatrist and get real inserts made. You can use inserts in any shoe. Inserts can be pricey yes, but so is buying a bunch of different shoes that don't work for you.
[kigg6wb] (score 19, diepte 0) Hokas are like walking on pillows. But the real reason I vouch for them is because of my wife, who is a nurse.  You want to know what the best shoes are?  Ask a nurse who’s on her feet for 12 hrs a day. Having said that, there’s many good options and everyone’s feet are different. But if you really want to help your feet, ya gotta be looking at the higher end, more expensive stuff
[kigmamd] (score 10, diepte 1) I was about to make this same comment about going to a running shoe store! This is by far the best recommendation for OP because while my Hokas are the only shoes I'll wear in the parks they might not work for someone else. Brooks are what work for my mom but Hokas don't.

I'll gladly pay the premium to not have my feet be in so much pain it ruins the trip for me.
[kii3b9r] (score 8, diepte 0) Friend I have three words for you:

Dedicated.

Disney.

Crocs.


I wear them with socks to avoid blisters, and they’re by far the most comfortable shoe I’ve worn at the park. And I also get the benefit of looking like a sexual tyrannosaurus.


Bonus points for embarrassing my family by wearing socks and crocs.
[kih0tgs] (score 6, diepte 1) This is how my wife deals with it. Good running shoes with appropriate arch support and nice thick padding.
[kighpt1] (score 5, diepte 0) I'm sorry to say Hokas are what work for me.  You might look into Skechers.  Those used to work well for me, but Hokas are expensive because they're just an entire other level of good.
[kigk4m1] (score 5, diepte 0) Quality shoes cost money unless you find them on sale.
[kigtg26] (score 4, diepte 1) Seconded on the Hokas. I have the same problems and have just been dealing with the pain and I wore my Hokas on my last visit and had zero pain.
[kihcgle] (score 4, diepte 1) This saved my life!  I have custom orthotics and they have held up for years over many long vacations.  It’s well worth the price.
[kigjrnc] (score 3, diepte 0) I would get a specific high arch shoe insert, that would be cheaper than a full shoe. Also look up exercises for plantar fasciitis and load up on them a few months before you go.
[kih40bi] (score 3, diepte 1) Excellent answer! I wear Hoka Cliftons for everything because they are amazing. 25k steps at Disney is fine in them as well. (For me!)
[kihbpnb] (score 3, diepte 1) Yes! I was embarrassed to even walk in to a running store, as I’m round and old 😄. But they were so helpful. They’re used to working with runners who have injuries, so at a good store they’ll be very knowledgeable. (If they’re not, try another store, or at least a different salesperson)
[kigo0nf] (score 3, diepte 0) I have been loving the ON Cloud 5.
[kigqodc] (score 3, diepte 0) Tevas. Seriously. I've done 40,000 step rope drop to "Main Street will remain open for your shopping convenience" days with PF in a pair of Tevas.
[kigvg7x] (score 3, diepte 0) I’m a high school teacher so I’m on my feet a lot. I’ve dealt with PF for ten years and there’s no cheap solution. The best way to deal with it is good quality shoes with plenty of support. I like Hokas (bondi for running, Clifton for everyday use) but also really like my Brooks Ghosts. That’s what the cross country coach at my school swears by and I’ve liked them a lot so far. As others have said, it’s good to have two pairs that you alternate between. One pair one day, another pair the next. I’ve come to grips with knowing I have to pay at least $100 for shoes, but it’s worth every penny rather than be in crippling pain. That said keep an eye on the inserts and replace them as needed. I usually grab a new pair every six months to a year and retire a pair.
[kigwrd3] (score 3, diepte 0) For me the answer is Dansko sandals. The support and comfort far exceeds sneakers.
[kih3tnz] (score 2, diepte 2) We did a week at DisneyWorld and Universal in Florida last June. I doubled up- took a pair of Hokas and a pair of Brooks Ghosts and rotated them. Worked out great. And I highly recommend epsom gel for feet and knees. That stuff is legit
[kigwmuk] (score 2, diepte 1) Totally agree, I can go so many more miles a day when I have my superfeet insoles in. They have a guide on their site which tells you what style would work best for you.
[kihjuf8] (score 2, diepte 1) I will add that if you go to the running shoe store, tell them the type of activity you’ll be using them for. HOA makes walking shoes as well as running shoes. Either would probably help you, but if you will mostly be walking, a walking shoe would be better. There are some differences in construction to support the foot best for each activity. Brooks also makes a good walking shoe.
[kiigg1b] (score 2, diepte 1) This is what my daughter and I did to get shoes for our upcoming trip. My husband has Hokas and he loves them. That’s what I planned on getting but we were able to try many different pairs and brands at the running shoe store. I ended up with Brooks and they feel like walking on a cloud! The salesman was very knowledgeable and never made us feel uncomfortable. He made sure we took our time and were happy with our decisions.
[kigmu4g] (score 2, diepte 0) Go to a specialty show store and let them find you the right show for your foot.
[kigvpxk] (score 2, diepte 1) My pair is coming tomorrow!! (specifically Cloud 5 Combo.) Can't wait to try them out.
[kigt254] (score 2, diepte 0) Hokas
[kihr42s] (score 2, diepte 1) This is the answer! If you have persistent plantar fasciitis a podiatrist can help you with custom inserts. You can also see if a cortisone shot is appropriate, as those can be very useful. 

Also, you will never wear cheap shoes again. I'm very sad to report that. FWIW, Brooks Ghosts work for me as the heel box on the Hokas is too big for my foot.
[kigtu0e] (score 2, diepte 0) My chiropractor recommends wearing New Balance shoes to me whenever I need to be on my feet for extended periods to mitigate my lower back strain. Not sure if that translates well to PF, but I wore them for a week at DLR and Universal Studios and it held up pretty well (shoes were between $45-75 at Big 5).
[kigumkv] (score 2, diepte 0) Hokas or Brooks
[kiguy09] (score 2, diepte 0) Oofos! I wear Hokas when I’m working out but my feet start to hurt in them after several hours. I have several pair of Oofos, I’ve done a million miles all over Disney and Europe. They are amazing.
[kihlbel] (score 2, diepte 0) My three must be packed shoes (after trips to Disneyland and WDW) are:

-Birkenstocks (I have a pair of two strap sandals and leather ankle boots)

-New Balances (my suggestion would be to go to a New Balance store and be fitted from there, I had this done and it really made a huge difference) 

-Crocs (my favs are the platform sandals and the regular clogs) 

I also cannot stress enough how great compression socks have been when at the parks! Congrats on being a Magic Key!
[kii91eq] (score 2, diepte 0) Respectfully, are you overweight? I’ve dealt with chronic plantar fasciitis for nearly a decade & my weight has yo-yo’d during that time (three pregnancies) and my husband and I have both noticed that my plantar fasciitis is considerably worse the more I weigh. I have custom orthopedic inserts & those are the absolute best thing I’ve ever done for my feet. So if you’re overweight, losing weight might hopefully also help your feet (less weight = less pressure on the foot structures) but investing in custom orthotics is amazingly worthwhile.
[kiibku5] (score 2, diepte 0) Sounds like you need to see a podiatrist and get custom orthotic insoles
[kihcuza] (score 1, diepte 1 OP) Good point. My SIL is a nurse and wears Hoka. She gave a pair to my wife and she loves them too. I guess we'll be a Hoka family. I'll try out the Clifton 8, they are on sale.
[kihf6pp] (score 1, diepte 2) I have the 9’s. Both are fantastic
[kigi3wt] (score 1, diepte 0) I have a few pair of nikes, and some saucony trail running shoes. The key is different shoes every day. Rotate 'em.

Beyond that. . . My feet just hurt at the end of a disney day. My PF lets me get away with it for a couple days but not longer than that so I hope to find new tips here.
[kigjaha] (score 1, diepte 0) I wear Reebok “forever floatride energy 2” shoes and they are so comfy.
[kih3jec] (score 1, diepte 1) This!! Especially finding them at the rack. Can find Hokas and On Clouds for under 100. Especially if you don’t mind obscure colors
[kigyj2f] (score 1, diepte 1) I see to get plantar fasciitis. I watched a few physical therapy videos on YouTube which were amazingly helpful. Anytime I get a small flare up, I quickly squash it with the PT exercises
[llm76pl] (score 1, diepte 2) you can purchas a new foot for the price of Hoka Cliftons
[kiglt1x] (score 1, diepte 0) Try Orthocomfoot brand.  I had pf for two years.  Started wearing these almost every day.  Can walk in them for hours.
[kign1lb] (score 1, diepte 0) Shoes are so individual so I don’t know if I would feel comfortable recommending something that works for my high arches and plantar fasciitis lol. But I kid you not, [these $35 tennies from Amazon](https://a.co/d/aa4dEry) are practically perfect for my feet and walking at Disneyland. I did 8 miles in them yesterday and my feet survived! Gonna do another 8 today, lol
[kixif6v] (score 1, diepte 1) I can also recommend the ON Cloud 5 or the ON Cloudsurfer. Both very comfortable for being on your feet all day.

They aren't cheap but they are stylish, high quality, and do their job well.
[kigpxcq] (score 1, diepte 0) Whatever you do buy walking shoes not running shoes.
[kigq3kl] (score 1, diepte 0) On Cloud 5-- I have them in 3 colors I have tried many pairs of hokas but always struggle with the sizes and how they pulled on my Achilles tendon. my on cloud 5s I took straight out of the box brand new wore them 2 whole days at Disneyland and were perfect. No break in time! The cloud 5 is a slip on that comes with laces to switch out. Super lightweight.
[kii64qe] (score 1, diepte 1) I love my Tevas, especially for water rides, but I finally caved and wore Crocs for a whole day and I had no issues. Tevas start rubbing the tops of my feet unless I put socks on. Either way I’m committing fashion crimes haha.
[kigr0wi] (score 1, diepte 0) I have PF, heel pain and flat feet. I use Sketchers Uno Shimmer Away sneakers or sketchers on the go sandals for hot days/water rides. Both give me good support and have cushioning and haven’t worn down (been about a year for both and we go once a month.) They’re also more affordable than Hokas and don’t look … like Hokas, in case that matters. 

Recover & Preparation are the main thing that helps more than the shoe for my PF pain. I use Epsom Salt foot gel on my feet in the morning and again at night. A quick foot massage (I use a mini Thera gun knock off) in the morning loosens the muscles and in the evening before bed it does the same but helps to relax. I also will use asbsorbine roll on at night, it has lidocaine in it and has helped make the middle of the night walk to pee easier and the next day I’m not whimpering with each step.
[kihvo5b] (score 1, diepte 1) This is the only answer. Lifesaver. Yes, pricey up front, but in the end it comes to pennies a day.
[kihrq9x] (score 1, diepte 1) I second Oofos, they have a sale going on right now as well.
[kigv10m] (score 1, diepte 0) Orthofeet.
[kigzyve] (score 1, diepte 0) Seconding the recommendation to visit a podiatrist—I know they can be pricy, but your feet & health are worth the investment! Problems you ignore now can creep up on you as you age if you don’t try to treat them early
[kih1x61] (score 1, diepte 0) go to your local running store + get your feet analyzed - it'll confirm your feet details (arches, width, + even feet swell) + the type of shoe support you should be wearing! i know everyone's budget is different, but investing in good walking/running shoes is worth the money + if you can, i would get custom in-soles for the shoes you buy!
[kih25wu] (score 1, diepte 0) Not everyone fits every shoe.  For me, with those issues, Hoka and New Balance are best.  For someone else, it might be Brooks or ASICS
[kih3f4x] (score 1, diepte 0) It’s just not gonna be a one size fits all. 

For some it’s sketchers, brooks, for others it’s Nike, Hokas, OnCloud, for some it’s tevas, chacos, for some it’s Birkenstocks, crocs. I think it would be worth discussing with a podiatrist if you can.
[kih4qhi] (score 1, diepte 0) I have similar issues and Hokas are what get me through (I have Clifton 8s, bondis and transports). 
 Before I discovered the Hokas a few years ago I wore Brooks Ghosts. I still like those a lot and they are a (slightly) less expensive option. 
I’ve never found a true budget shoe that gets me through and entire day without foot, knee and back pain after I hit my mid 30s.
[kihc80b] (score 1, diepte 1 OP) I was just looking at the Hoka website sale section, and saw the Clifton 8s were a pretty decent price. I may go that way. Thanks!
[kih534o] (score 1, diepte 0) You can find older styles /color way Hokas on Nordstrom Rack for <$100 
I’ve suffered from PF and they really do help. As do the night socks for Pfizer right after
[kih5eso] (score 1, diepte 0) I second Hoka. Do a Google search on which model of Hoka shoe is best for Planters Fasciitis, then go to some place like REI that has people trained to fit shoes properly. Then get yourself some quality socks to go with them, I like Bombas.  Then break them in before your trip. This is how I did it. I suffer terribly with planters, to the point where I take cortisone injections in the bottom of my foot. I went for 3 days last August, walked over 26 miles in that time and had no problems at all.
[kih5qod] (score 1, diepte 0) I've got high arches, heel spurs, deformed bones and nerve damage.  If I have to wear closed toe shoes, I wear my beat up RunDisney NB.  For non rainy weather, I wear my OluKai Ohana flip flops.

You know your feet so find your most comfy pair of shoes and use them as a starting point to find a new option.
[kih8h08] (score 1, diepte 0) Keds, I wear the slip-on ones. They arent too expensive but mine are so comfortable and I get so many compliments on the floral pattern by Rifle Paper & Co.
[kih93a5] (score 1, diepte 0) Please just spend the money on the Hoka's, go to a runners world or similar and have them measure your feet and get you into the right size and width.   

I had PF several years ago and went on vaca to Hawaii and was in pain the entire time, came back saw a podiatrist and purchased my first pair of Hoka's.   I have not had a problem since and actually had bought a new pair right before we went to Disneyland 2 weeks ago, well worth the investment.
[kihatwv] (score 1, diepte 0) ASICS Gel Cumulus are my holy grail for plantar fasciitis!
[kihbog7] (score 1, diepte 0) You can't discount all Asics because one didn't work, just like you can't say that any Hokas will work if you spend the money. Asics Kayano is a great stability shoe on it's 29th iteration, but it's not in the budget to mid range. And it doesn't many any Asics is going to work for someone who likes the Kayano.
[kihdyim] (score 1, diepte 0) Not a direct answer to your question, but I was able to solve my PF with one of those little spikey massage balls. I now keep them everywhere and use them whenever my feet start to hurt. It’s been a miracle! I’ve even started back up with my running after years of misery. Worth a try and $15 on Amazon…
[kihhutm] (score 1, diepte 0) Don't spend money on new shoes (unless you want to). Get a pair of Superfeet Green insoles and stick them in your favorite shoes. Worked wonders for my plantar fasciitis. Taking a couple aleve before you hit the park will also help, unless you're planning on drinking. Best of luck. Plantar fasciitis is a total bitch
[kihnz1x] (score 1, diepte 0) I have PF. I use asics with power steps insoles (got them on Amazon). No more issues! That main thing is to remember to stretch before the day and through out the day. Stretching healed my pf! I had it rough, every morning was the worst. Had injections for temporary comfort but as soon as I started stretching my calf’s everyday serval times a day I’ve had 0 pain since!
[kihoqva] (score 1, diepte 0) I don’t have specifics to recommend since I have different foot issues, but I would urge you to consider this an investment and pay a little more rather than try the more budget friendly options out there. 

Sadly, experience has shown me that while OK the overall experience and lifetime of more expensive shoes is well worth the money. 

I would suggest maybe going to a running store and getting fitted professionally. Even if you aren’t a runner they can help! I went after knee and hip replacement last year for some good walking/work out shoes because I have one fallen arch and have loved every step I’ve take in what they recommended even though I wasn’t thrilled at the cost.
[kihpwh7] (score 1, diepte 0) If getting prescription insoles from a podiatrist isn't an option these are fantastic. They are the only shoe I can walk more than 100 yards in without pain. It's a whole company dedicated to PF and high arches.

[https://www.kurufootwear.com](https://www.kurufootwear.com)
[kihtuua] (score 1, diepte 0) I don’t have a brand of shoe recommendation but I do have a shoe recommendation: bring a second pair. Switch in the afternoon.
[kiii9t3] (score 1, diepte 1) I recently wore some bright yellow Crocs to the park to look like Mickey :)
[kiikjud] (score 1, diepte 2) I should have gotten yellow ones!
(16 reacties met lagere score weggelaten)

