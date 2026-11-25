# Label-batch batch_0140

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
Schrijf het resultaat naar `batch_0140.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 5ctakz, 15we1yf, 178w93w).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 5ctakz ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2016-11-14  SCORE: 9  REACTIES: 124
TITEL: Fellow people with EDS... How are your feet??
POST (source_id=post):
Pain? Arch? Flat? Bunion? Normal? Orthotics? Edit: 
We can compile useful information into another thread :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d9z8098] (score 11, diepte 0) Very high arch, very unstable ankles. They don't hurt, just give easily. I absolutely can't wear normal shoes for any long time period anymore. I worked in nikes for awhile and would always come home from work in so much pain I'd whine a lot to my ex, I'm sure that was't fun. My ankles KILLED, I'd lay in the tub with the drain open and let hot water run over my ankles.

Then I tried a pair of dansko clogs I bought on ebay for $30, they're normally super pricey. I knew my mom who has different physical problems loves them. Made such a huge difference! My ankles don't hurt, the pain in my feet and legs is manageable, not whine worthy lol. They don't do anything for ankle stability but holy fuck, better than any pain med. My mom gave me salomon shoes for working out, they have ankle stability that is wonderful for that, but dansko fits my foot shape best. Orthotics are the best thing and I worship them.

Edit: I don't worship orthotics since I haven't tried them, I got confused. I worship comfort shoes like danskos lol
[d9ziug7] (score 8, diepte 1) My ankles pop frequently, without warning and so loud that my coworkers down the hall will go "Oh my god, what was that?"

I work in a chiropractic clinic.
[d9z7uum] (score 6, diepte 0) The high arches I have been born with are now sadly flat. I wear orthopedic shoes and thankfully do not have bunions. Standing for any length of time is off the table for me.
[d9z8hbr] (score 5, diepte 0) Flat, have to pop my toes and ankles alot.
[da09djh] (score 5, diepte 2) Former massage therapist here. My hip sometimes sounded like a shotgun in that tiny, quiet room.

Most of my clients were seniors, though, and they really warmed up to me as a result. It helped them see that I actually did relate to their issues.
[d9zbpt2] (score 5, diepte 0) Super high arches and weak ankles. I can't wear my heels anymore, which is tragic because I loved my heels. Currently my feet feel like they're on fire. I can't stand on them for too long now. 

Insoles are my life saver.
[d9z936h] (score 3, diepte 0) I have plantar fasciitis, orthotics have helped though.
[d9zf74h] (score 3, diepte 0) Super high arches and I wear orthotics.  They are a lifesaver!  I also have hammer toes which I do stretches for, otherwise I end up walking on my metatarsal bone.  My ankles are bad like most everyone here, but are way better than they used to be.  I buikt up strength in them by balancing on mushy things as part of my PT.
[da01ize] (score 3, diepte 1) Lurker not diagnosed with EDS (just genetic joint hypermobility syndrome and tons of things that go with EDS, 7 months down and 5 to go til I see a geneticist) and have to say I **love** your description of your PT. Much of mine involved falling off of squishy/mushy things (my balance is crap, so I wasn't balanced on much of anything for long lol).  This made my (previously crappy) day.
[d9zirn9] (score 2, diepte 1) Exact same here, right down to the Danskos. But a word of advice: be careful if you're wearing socks in them/no ankle braces, especially on uneven terrain! Strolling down a cobblestone street will feel like walking a tightrope.

I stick to flats and ankle boots with prescribed orthotics. The only way I feel safe in any kind of lift is if it's a heel with no bevel and ankle braces.
[da02k8p] (score 2, diepte 2) Haha ohh man, you're right about that! I've had some spills, or trips. Or just having an ankle go when I'm shifting my weight around standing, and then people get wierded out. 

I don't know what a bevel is lol. I used to wear high heels all the time in high school, idk how I did it. I can barely stand them now. Prescribed orthotics would be great! What kind of dr does that? I was thinking of seeing if dansko made boots, maybe they'd have more ankle support. Basically I want the exact bottom of a dansko but in a more stable shoe. Plus I wish they looked nice, the clogs look wierd with leggings or dresses, my favorite stuff to wear.
[d9zqs0t] (score 2, diepte 1) I'm a nurse and until a few months ago when my pelvis fucked me up I was a faithful dansko wearer for 10 hour shifts.  Danskos along w orthotics were a dream for my feet except they're so damn heavy.  I do have very strong ankles however.
[da0h1xt] (score 2, diepte 3) I wear the danskos with Superfeet brand orthotics.  My prescription orthotics don't fit in them quite right. I wear the prescription orthotics in all my other shoes x flip flops or dress up shoes. 

My username is from Napoleon Dynamite.   I love how Uncle Rico pronounces "coccyx" it makes me laugh every time.  Yes I did once fracture my coccyx years ago but surprisingly it's not been a long time issue.
[da0cz1v] (score 2, diepte 2 OP) Same comment Lol I hope your user name isn't that bad. 

Another one for Danskos, I'll check it out.
[da0cvci] (score 2, diepte 1 OP) I'm assuming custom Orthotics? I'm stubborn and I think we can strengthen the feet and the body to counteract the effects of Ehler danlos. One day I'll either give in or I'll find a way.  My experience with Orthotics has been so so.. I've been wearing minimal shoes (just flexible pumas) and it's been pretty good for 2 years except the big toe.
[da0h7hw] (score 2, diepte 2) See my above response. 

I'm a strong believer and practitioner of strong muscles --> stable joints but it seems gravity and wear and tear are catching up with me.  I'm fucked from the waist down right now and now my relatively low-key chronic neck and shoulder issues are flaring up.  I'm assuming that's because I haven't been working out like usual for three months now.
[da50hpa] (score 2, diepte 3 OP) I meant foot orthotics 
Great!!! We need people who are proactive! I'm for that. There's a doctors thread on this page and next up I'd like to do a useful practises thread.. I'm compiling some info but it's hard to keep up with life and this. But anyways.. I'm sure at the very least the info would help!
[da0f1cw] (score 2, diepte 3 OP) My ankle popped so loud once in class that I heard it over my loud ear phones. It hasn't popped in a long time but now my right hop pops almost everyday.  What's the cause?
[da0i9st] (score 2, diepte 1) Every time I stand up I have to stand on my toes to let my ankles pop.
[d9z9efb] (score 2, diepte 0) Bunions.  Severe overpronation.  Despite faithfully wearing prescription orthotics have daily plantar fasciitis and achilles tendinitis pain.  Had to quit distance running in 2013 and now I'm sidelined in a major way thanks to constant foot pain and severe pelvic pain. My podiatrist doesn't know where to go from here, but my pelvic specialist recommended prolotherapy (sp)? And I've seen some soft tissue surgery for EDS people online.  My feet are fucked but it's my pelvis that's giving me the most misery these days.
[d9zqthw] (score 2, diepte 2) Sorry, man. *fist bump*
[da0eshd] (score 2, diepte 3 OP) I have done prolotherapy and I've gotten many family members to do it (none have EDS) 

I can tell you more info about it (I spent a good $1500) on this. I've had it done maybe 20 times

You need to do PT.
[da5053u] (score 2, diepte 5 OP) Great.. Your pelvic specialist should be your best friend haha. 
Hip and knee.. Multiple ligaments.. For me it wasn't so successful but for family members who are not hypermobile, it worked like magic. I recommend it to them and they were happy. All 3 of them. Go for it and let us know how you do!
[da85jgl] (score 2, diepte 6) The tears happened in a separate activity( I slid down a banister of my deck playing a game) but it was while I was actively playing sports- it was super sudden bc well- I snapped both ankle and knee- tinctures can be more expensive- it's actually VERY cheap to buy 'shake' weed (the shitty stuff no one wants to smoke but still has THC in it) and make cannabis coconut oil- and yes you can get high off of a tincture- find out the right dosage that won't get you high and you'll still feel the positive effects. There's something called CBD oil that reduces anxiety and is an anti inflammatory that I've tried and really does help- It was just harder to find for me at the time lol- and not noob questions! I didn't know any of these things a few years ago- the more you ask and research the more you know ❤️
[d9zgxfz] (score 2, diepte 0) Weak ankles, horrible bunions and I'm unable to keep them straight whenever laying down on my back they immediately fall inward. My feet are also super narrow.
[d9zu14a] (score 2, diepte 0) I have high arches... until I stand. Then they're completely flat. Weird toes, lots of pain and cramping, my ankles are a mess. Both of them. My right one I roll frequently as the tendons on the front/side are completely stretched out or have torn, but they're both unstable. My left ankle tends to go out towards the back, which causes a lot of heel pain. I'm getting custom orthotics soon, which will hopefully relieve some pain!
[da0dsfs] (score 2, diepte 1 OP) It sucks to hear this. I hope the Orthotics will help. How do you know they're torn? I can say go for prolotherapy but our muscles, symmetry, and general synergy has to be done first.
[da54nz2] (score 2, diepte 4) I'll try to think of some stuff and come back! Specific to feet, or just in general? I actually live in Portland OR. So, close! It's really hard to get diagnosed - there's one geneticist in the state who actually diagnoses people, everyone else refuses to diagnose hypermobile type or won't diagnose adults. Lots of people travel though, especially to California. We are really lucky that there is a physical therapist in Portland who started her own practice and has EDS herself. She's very dedicated to educating other practitioners, so hopefully soon there will be more young physical therapists who will know what they're doing! I think they are also starting to teach about EDS in the local hospital universities so there's a growing awareness.
[d9zz9ly] (score 2, diepte 0) High arches that flatten when I stand on them. I can't walk around my house barefoot anymore before the pain gets too much. I need to figure out orthotics and PT very soon 😥
[da06wgk] (score 2, diepte 0) High arches that have now collapsed; plantar fascitis; right foot has both a standard bunion and a tailor's bunion; various crunchy things have happened in the arch and I'd got ganglions that have been there forever on the top of both feet. Pain. Sometimes numbness.

I use orthotics and heels are a distant memory. I take cushioning as seriously as orthotics and support. If I want to really walk anywhere I wear hiking boots with solid ankle support. Summer is an effing nightmare...

I think the right foot is worse because my right leg is either longer or is misplaced in my hip somehow. It turns inward (if I lie flat on my back, both feet lean left). I couldn't get any doctors to take this seriously or even measure it properly but my groin pain improved a lot after I added one-centimeter rises to the shorter leg side.
[da0didv] (score 2, diepte 1 OP) This maybe caused by your pelvic positioning. Maybe muscle weakness, compensation patterns, etc. Let me know if you want me into, if you're gonna spend money on a doctor, you might as well go to a physiotherapist who actually works on people with Ehler danlos.
[da3iijk] (score 2, diepte 3 OP) The only one I know of is called Jan Dammerholt. Search up his lectures or Interview and listen while you clean or whatever. You may learn something. 
How expensive? $80?
[da1ccpw] (score 2, diepte 2) Yeah, minimalist shoes really did help with my knee pain. Unfortunately, since my foot broke the first time, I can't wear them for very long without consequences. And I'm discovering that functional feet are more important for me to be able to get on in the world than functional knees.

Never diagnosed with anything more specific than ligament laxity; this was in pre-ACA days and I was advised against searching deeper as it would leave me uninsurable.
[da0fv0m] (score 2, diepte 0) Suuuuper high arches but sometimes I feel like they are falling. I get plantar fasciitis but the "falling arch" feeling is quite different. When I was a teenager, I used to get these random intense episodes of pain across the tops of my feet that would last from days to months. Bone scans, MRIs, x-rays were all negative. As an adult aware of and diagnosed with EDS, I feel like the pain was likely due to bone subluxations. I often get pain at the base of my big toes that shoots through to the tip when I push off while walking. My ankles are assholes. If I try to run even just a little bit, like across the street, they very painfully give out on me. 

Adidas Energy Boost shoes have been amazing for my feet, knees, and pelvis. I used to have a really horrible gait and these fixed it completely. My physical therapist was amazed. I used to hit hard with my heel, over-supinate (hit with the outside of my foot instead of the inside (pronation) like most people do), then slap my foot down like a flat footer. I've got a mostly neutral gait now thanks to these. They also hold up incredibly well. I had my last pair for over a year before I had to call it quits. 

Also, for anyone who gets plantar fasciitis, check out [the X Brace](https://www.thexbrace.com). I used [Mueller PF Tape](https://www.muellersportsmed.com/pf-tape-system-for-plantar-fasciitis.html) for a while and loved it, but it's pretty expensive. The x brace has worked just as well for me and really does help. FWIW, I thought they were both a joke initially and didn't see how they could possibly help. I was very pleasantly surprised.
[da23fpz] (score 2, diepte 2) Peroneal tendon...it should be on the side towards the backish, not visibly pulled around to the front. It's kinda gross tbh!
[da3i2mw] (score 2, diepte 3 OP) I just saw some pictures on google... Logically speaking we should be ABLE to put that tendon back in place..
[da7j9s5] (score 2, diepte 3 OP) That's the first time I hear of this... I hope you will be OK!! It's hard enough having EDS
[da7l67q] (score 2, diepte 4) Thank you, I'm doing my best! Just so glad I'm finally diagnosed with SOMETHING. I hope you're doing well as well.
[dabqa1m] (score 2, diepte 1 OP) I've been destroying that tendon since I was a kid :)
Check out xbrace.. Another redditor posted this
Do you Lift? (Srs)
[d9zi0zv] (score 1, diepte 1) Ditto.
[da50mlt] (score 1, diepte 1 OP) Went away after wearing orthotics?
[da51pys] (score 1, diepte 2) Nope. It's a part of me now it seems.
[da5ftf8] (score 1, diepte 3 OP) The muscles you can do something about, ligaments not as much and maybe nothing. I kind of built a bigger yet still low arch from exercise
[da02nzj] (score 1, diepte 2) That's what my mom does too! Or did before her arthritis got out of control. I found out about danskos when I wore hers to work back when I lived at home. I had never thought of danskos with orthotics too, that sounds amazing! Do you get prescription ones or other ones? And I agree, they're annoyingly heavy. I think they just came out with a lighter kind though, I tried on my mom's. Hopefully they make their way to ebay soon lol. Also not a fan of how the clogs look with everything, I'd like something more stylish.
Edit: I love your username....and hope it's not true, ow!
[da3jr5l] (score 1, diepte 4) I had to look up that clip, pretty funny! And ow, sorry that happened! I'm glad it's at least resolved now :) 

It would be amazing to have those to wear in whatever shoes, esp dress and flip flops, which I love!
[da0hrdn] (score 1, diepte 2) Sorry, I got confused. I was thinking orthotics meant like shoes for joint problems n old people lol. Never had orthotics, from what I hear theyre pricey. Id so try them if I had access.

Im with you about strength. I dont think its stubborness, its determination and taking care of yourself :) Im doing the same. Ive done some pt stints but thats pricey. Splurged on a gym membership. I feel so much better the more I work out. You just have to learn your limits. With strength some stuff makes my joints give, like pushups. Just have to figure out targeting muscles without injury. I do think it mitigates a lot. Id recommend everyone eds or not to do what they can! 

It helps with a lot, I still have tons of problems but working out raises my baseline. I even got hand strengthening balls! My splint on my thumb is a bit off sized, Id prefer to not need any. 

Keep up the good work! We should make an eds fitness sub lol
[da5371z] (score 1, diepte 4) If I ever try to make it I'll mod you :p 

And ooh gotta check that out. I need a primary who doesn't google it in front of me but don't have the funds to experiment with drs. 

That's such a great idea! And I'm with you, sometimes it takes days to respond to people cuz I'm super busy and also super distractable and forgetful.. bad combo lol. I do think the info would help! I had to kinda do trial and error with excercise, learned the hard way that pushups will FUCK UP my wrists and shoulders, and that I can't do that tricep exercise over your head with free weights....my shoulder joints just gave before I could even add enough weight to feel in the correct muscle lol.

We could ask for other's input too cuz I know there is a huge range of how much this disables people!
[da5fvg1] (score 1, diepte 5 OP) For sure! I'm experimenting with something new and I'll post my results real soon. 
I'm broke too.. Still a student :/ 
When I worked I spent a lot of my money on this stuff. 
But yes.. If this sub reddit is now active it will be great
[da50627] (score 1, diepte 1 OP) How long did  have you been using them for?
[dd4h7zu] (score 1, diepte 2) Sorry I missed this comment, I've been wearing them for a few years
[d9zp62p] (score 1, diepte 1) I hear ya on the pelvis issues :(
[da0hmtu] (score 1, diepte 4) I've been a faithful PT patient for various joint issues these last 8 years (neck, shoulders, FEET, sciatica).  I am a compliant patient and I do my exercises and all that.  I am a believer.  Hey, I'm an RN I gotta practice what I preach.  And I tell all of my ortho and spine patients they gotta be compliant if they want good results. 

Prolotherapy is big in my area.  (My part of the country is known for being quite hippy-dippy crunchy-granola alternative medicine etc.)  I'm just trying to figure out a way to come up with some cash for it.  My pelvic specialist NP is hypermobile herself and couldn't say enough praise re how much prolotherapy helped her feet and ankles.  She also recommended it for my SI joints.

Which joints did you have prolotherapied?
[da55ub5] (score 1, diepte 6) Thanks. Again, money is an issue , but I'm super interested.
[dac66mo] (score 1, diepte 5) Prolo's not cheap, I'm also very interested. 

Dry needling might be cheaper, and some researchers have suggested that even just the needle aspect might be part of why prolo and other injection therapies have an effect. It makes sense to me, inflicting controlled damage to promote healing is what eccentric exercise is supposed to do, right? Also laser, for that matter (for different tissues). 

The costs of paying out of pocket for therapy for multiple injuries are really adding up for me, too. Where I live, you can claim money spent on healthcare costs if they're over around 20% of your income, and that is me. (And I'm in a single payer system, that's all just physio, braces, etc.)
(71 reacties met lagere score weggelaten)

=== THREAD 15we1yf ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2023-08-20  SCORE: 33  REACTIES: 79
TITEL: Recommendations for good brands/styles of sandals that won't hurt me while teaching?
POST (source_id=post):
I just got hired as a substitute teacher, and one of my things is I love wearing colorful hippy dresses and I love wearing sandals. Sandals, unfortunately, don't love me. I want to continue wearing these things (especially since I plan on focusing on elementary school and kids seem to like my outfits) but I know walking around in flip flops for 8 hours a day will make me wish I could chop off the lower half of my body.

Any good brands or styles I could try? I have the hypermobile type of EDS; along with all the other good stuff, I have bad hips and sciatica that goes down both legs.

If sandals in general are bad, any shoes that won't hurt me that would at least not look awful with dresses would work.

Thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jx0bfmg] (score 45, diepte 0) I love Birkenstocks! They are definitely on the dorkier end of stylish, but they provide nice support and are comfortable (they’re not soft like memory foam; they provide hard support which my EDS specialist said is good for our bodies). I have a close-toed pair of birks that I wear every other day to work (the other days I wear sneakers) and they’re great! They last a long time (I still have a pair of birk sandals from about 10 years ago) so the price is worth it. Most of their styles are adjustable so you can loosen them if your feet swell from standing a lot. And they have a variety of styles to choose from, so hopefully you can find something you like!
[jx12na4] (score 21, diepte 0) Teva brand is what works for me. I wear them all of the time!
[jx0ck9e] (score 18, diepte 0) Arch support and firm soles are my friend for sandals! I've had a decent time with Birkenstocks, a teacher friend with arch issues swears by the Dr. Martens sandals because they're so stiff. Another brand to look into might be vionic shoes, they look quite nice! 

As an elementary teacher (kindergarten and music) who has subbed as well, honestly I wouldn't recommend sandals if you value your feet. If you're used to sandals and love them then just ignore this, but my toes get so many nicks and bumps and sores even from a day of teaching! Kids are clumsy and I'm no better, but in a day I get so much stuff dropped on my feet, kids step on me, depending on the age you sub for do you really wanna wipe yogurt and snot off your toes? My answer was no lol. So I bought a bunch of different fun patterned slip on vans, ripped out the insoles, and put in my own supportive ones. Now I'm fun cause my shoes match the kids, they're easy to clean, and my hips hurt way less! I wear a lot of loose dresses and skirts and find it fun matching my printed shoes to them!
[jx1gns0] (score 9, diepte 2) coming in to second birkenstocks! So freakin comfy, I have the Bostons (original clogs) and they stay on fine!
[jx15ils] (score 8, diepte 0) Tevas. I have two of the flatform style sandals and they're incredibly comfortable, durable, and supportive. Don't get the elastic ones though, the Velcro straps are the way to go.
[jx102yw] (score 7, diepte 0) Love love love my Birkenstocks!! I also love wearing converse and vans (so many cute styles to wear with dresses too!!) but I switch out the insoles - superfeet makes great ones, I have custom orthotics now. I lived in my vans old skools and slip ons when I was on my feet all day working in elementary. 

For my hips I wear compression shorts under my street clothes and reinforce with an si belt as needed (serola brand from Amazon is the best one I’ve tried). 

Good luck!! I miss working with kiddos but my body just can’t rn, maybe someday!
[jx0rxay] (score 6, diepte 1 OP) Your closed toe Birks, are they the slipper style or do they have a strap on the back of the heel? Do they stay on your feet pretty well?
[jx14op4] (score 6, diepte 2) The closed toe birks I have are their London style: https://www.birkenstock.com/us/london-suede-leather/london-heritage-suedeleather-0-eva-u_27.html#sz=48. All of the styles of birks that I’ve had (even the sandals) stay on my feet well. They kind of mold to your foot after a while, if that makes sense.
[jx1n06h] (score 6, diepte 0) Chacos. They are more supportive than Tevas and there isn’t the annoying Velcro issue. They stay on your foot in the right place and feel like sneakers. They are also not as ugly as other sandals (personal opinion). They have versions with a really supported arch and ones that are not as structured. They last for years (unless your dog eats them).
[jx1lae4] (score 5, diepte 1) I also suggest birks. But get the original sole for the support and the nubuck leather for the hold - I find it molds to my foot and the leather not stretching helps keep my foot in place in the shoe.
[jx0ni3e] (score 5, diepte 0) Hoka Recovery Sandals have been the most amazing sandals for me! I highly recommend
[jx0vbh7] (score 5, diepte 0) Clarks are just about the only sandals I can wear! They’re super cushy but have enough support for my collapsing arches
[jx1mmwj] (score 5, diepte 0) I love my Tevas. They often use Vibram soles and can't go wrong. Clark's are also incredibly comfy and are starting to be more stylish.
[jx0g2m2] (score 4, diepte 0) I recommend going to a store that stocks a lot of the hiking sandal / supportive sandal brands and trying on a bunch. It’s definitely an individual process — what shoe brand works best depends on the size and shape of their shoes vs the size and shape of your feet, in 3 dimensions. 

My sister and I swear by Teva sandals. They definitely have a hiking / outdoor vibe, and I really wish they would make a dress sandal!
[jx14afh] (score 4, diepte 0) Oofos might help you. They didn't feel good on my feet, sadly, but a lot of people swear by them. There are lots of variations to choose from, too!
[jx0o1y3] (score 3, diepte 0) Vionic. These saved me.
[jx0sfns] (score 3, diepte 0) Orthofeet
[jx0wp5m] (score 3, diepte 0) Sorrel sandals. Built like a trainer but is a sandal. Check Amazon for lower price.
[jx0yhn6] (score 3, diepte 0) I have had success with www.orthofeet.com. Love how you can customize it inside for height and arch support if desired that comes in their shoes box and not extra.
[jx17as9] (score 3, diepte 0) 110% Clarks. I had a solid pair of loafers and two pairs of dress sandals when teaching. They’re amazing.
[jx1eq8l] (score 3, diepte 0) Dansko
[jx2ozsw] (score 3, diepte 0) I seem to have the opposite experience of most people. My knee and foot pain went away when I switched to minimalist shoes as my primary. I love softstars and wear them to work. They have an [open toe sandal style](https://www.softstarshoes.com/adult-solstice-sandal.html).
[jx0sa0s] (score 2, diepte 1 OP) I could try slip on shoes, but I've had mixed luck with those types of shoes. One of my feet is smaller than the other so it feels like that foot likes to slip out, especially if I try to wear ballet flat style shoes. I like the idea of putting in good insoles, they can make a HUGE difference.

I've worked plenty of jobs where I was on my feet all day, but not in a long time. My body hurts more than it did back then so I want to prepare.
[jx4ju8n] (score 2, diepte 2) I have these and they're phenomenal for all day wear: [https://www.amazon.com/Comfortable-Sandals-Lightweigh-Warerproof-Vacation/dp/B07L5N2KBD](https://www.amazon.com/Comfortable-Sandals-Lightweigh-Warerproof-Vacation/dp/B07L5N2KBD)

They're even machine washable!
[jx0kjvw] (score 2, diepte 0) I swear by Taos sandals, the ones with the cork footbed and low heel. Amazing comfort for my high collapsible arches.
[jx0ropo] (score 2, diepte 0) Others have said it but Birkenstocks, the proper ones not imitation ones or the ‘fashion’ version that Birkenstock make. Personally, I find mayar the best design as it stays well attached to my foot without needing me to curl my toes to grip the sole. I wear them constantly at work and I am a teacher too. 
If you can stand the weight of them Dr Martens sandals  are also fab (but I can only wear them when I’m going to not do much walking about so they aren’t great for the classroom)
[jx15jjs] (score 2, diepte 2) Birkenstocks are defined my recommendation then
[jxa31vp] (score 2, diepte 1) Love them! I can only buy sandals as I wear a 13 in closed shoes. They are very funky
[jx0x45z] (score 2, diepte 0) Earth origin
[jx11h32] (score 2, diepte 0) Keen! I have some I bought with the paracord Uneek sandals 

https://www.amazon.com/KEEN-Mens-UNEEK-Sandal-Black/dp/B00SYZ9N9C/ref=asc_df_B00SYZ9N9C?tag=bngsmtphsnus-20&linkCode=df0&hvadid=80264466501408&hvnetw=s&hvqmt=e&hvbmt=be&hvdev=m&hvlocint=&hvlocphy=&hvtargid=pla-4583863992946929&psc=1 


favorite summer footwear ever! Cool, easy to keep clean, they’ve been in the ocean, rivers hiking trails, summer business meetings, sales calls… they look great offer amazing support and come in all sorts of hippy colors (mine are black but they have a bunch.)
[jx12x8h] (score 2, diepte 0) Vionics, they tend to run narrow but I have good luck with the nicer looking flip flop versions. They are basically the only sandal I will go out in.
[jx14y3o] (score 2, diepte 0) Skechers. I used to love Birkenstocks, but when I found Skechers, I became enamoured. So many different types and styles, I can always find SOMETHING that works.
[jx16lh0] (score 2, diepte 0) The EVA Birkenstocks are the shoes I wear consistently, they’re comfortable and very durable too!
[jx18v43] (score 2, diepte 0) Look for orthopedic sandals. I just got myself a pair to wear inside my home. I could tell they were the real deal because i had to slowly accustom my feet to them: wear them for just a couple hours to begin with (i had to remove them because my feet got extremely fatigued), then a little longer the next day, and so on, until i could wear them all day.

Previously i was wearing a brand of sandal called Soft Moc, which is similar to Birkenstock but has a little more arch support. It was enough to prevent my hips from subluxing several times per day, but i still developed other leg problems while using them. Orthopedic sandals are definitely superior in this regard.

Also look into getting custom orthotics for shoes. I've had to wear them since i was 9 years old, but have been told by people who get them as adults that they are a game changer. The main thing to look for with shoes when you use orthotics is a deep enough heel to accommodate both the orthotic and your own heel.
[jx1ewdu] (score 2, diepte 0) Brand name Birkenstocks, the leather and cork sandals. None of the knockoffs or the foam material ones. I bought a pair in April and I've been walking around in them all summer. They're so great.
[jx1fgut] (score 2, diepte 0) There is one sandal that I’ve ever been comfortable in and that is Eürosoft’s Gianetta Sandal, so much so that I’ve ordered them again after they wear out. They are on the cheaper side so they usually only last me a year (I wear them almost every day though) and they go well with the hippy vibe that I also have. Though I must clarify, my feet are especially messed up and I have quite high arches opposed to the flat arches that most hEDS folk have, so your mileage may vary. 

I have heard good things about the Hoka Sandals though, I have yet to try them but I really want to. I have a set of Hoka’s tennis shoes and they are the only tennis shoes I can wear, although lately the pressure of laces tied on top of my feed has been too much so I haven’t been wearing them often. I currently rotate between the Eürosoft Sandals, some sketches slip-on shoes, and some random unbranded flip flops that I got a decade ago that are falling apart- I will be devastated when they finally give out lmao. I have no idea why they are more comfortable than just about anything else haha. 

I will definitely be trying some of the other suggestions in this thread though! I do love my sandals but variety is nice. And hey I might even find something more comfortable! Best of luck~

I wish you good luck!
[jx1fq4f] (score 2, diepte 0) I’ve worn Ecco Yucatan sandals for years. I can’t wear leather against my skin. So many sandals are leather. They come in lots of colors and I’ve walked miles in them without any issues. I pronate and have hypermobile ankles so they offer plenty of support.
[jx1j8sx] (score 2, diepte 0) Oofos!!!
[jx21ziv] (score 2, diepte 0) Love my Birks. Also bought some Teva sandals recently. I regret buying the basic model as I liked the design more. The hurricane model of Teva shoe was probably the most comfortable shoe I have ever worn. I plan on getting a pair soon.
[jx2760v] (score 2, diepte 0) Kork Ease are the comfiest I’ve found.
[jx29750] (score 2, diepte 0) I would get closed toe sandals if your wearing sandals to work! I personally love my open toe birks & second the closed toe ones. A lot of my coworkers used to wear them as well!!

I’ve not worked with kindergarteners but I used to work in a day program and we had to wear closed toe shoes but it made a lot of sense & a big difference to how my day went when I wore solid shoes. 

The day you don’t cover your feet is the day someone’s gonna accidentally step on your toes or otherwise injure you
[jx2f1ze] (score 2, diepte 1 OP) Last school year, I volunteered daily in my daughter's kindergarten class. Once it got warm enough, I wore flip flops daily. I don't recall any major incidents, and kids liked it when I painted my toes lol.

As far as I can tell, there isn't any formal dress code for the district besides "dress professional". Nothing specific. I have a teacher friend I can ask, though. Good call.
[jx2njtv] (score 2, diepte 2) Also congratulations on the job!! It’s worth asking your friend as well what they recommend! 

I’m just about to go back into the industry myself and I’m wondering if it’s worth grabbing fresh summer shoes as well.
[jx2uqch] (score 2, diepte 1) Same for me!  I decided to trial barefoot life with a cheap pair of water shoes that I wore for a couple of months (well before I knew I had hEDS) .  I bought a pair of Merrell zero drop shoes and wore them until they wore out.  😂 

All my previous foot/leg/lower back pain from falling and standing went away as my feet strengthened and did the work they are supposed to do.  I now wear Xero shoes (they do have sandals!) and now that's all I wear (I have eight different styles, from winter boots to sandals).  😊
[jx2qoou] (score 2, diepte 0) I have Merrill sandals I love! I also recommend compression shorts for the hip/sciatica issues. I'm usually in full waist high compression tights but if it's super hot out, I'll go with just high waist compression shorts (actual compression, not just bike shorts) and they help hold my wonky hips in pretty well.
[jx2swgy] (score 2, diepte 0) I got danskos this summer and my feet were much happier than in the past. 

Danskos are wildly popular with teachers because they are built ergonomically. They can get pricey but it's worth it to not be in pain.
[jx2th7g] (score 2, diepte 0) GDefy all the way. I get asked on the train how I’m able to keep my feet planted. I have hEDS and plantar fasciitis doesn’t help…. along with tendinitis and metatarsalgia. 

I’ve been wearing the same shoe for about 6 years. I’ve rebought the same pair maybe twice. They come with orthotics too!
[jx32idg] (score 2, diepte 0) Unexpectedly, I’ve found Adidas sliders sooooo comfortable! Size up one size. I feel like I’m floating and they’re great on my joints.
[jx354x9] (score 2, diepte 0) Someone recommended Pons Avarcas to me in this sub and they are my most favorite and comfortable sandal I have ever bought. They are also pricier than any other sandal (at $80), but now that I’ve worn them every day since I’ve bought them & they just keep getting comfier, well worth it.
[jx3dnku] (score 2, diepte 0) I recently bought a pair of Timberland “Adley Way” style sandals (they have 3 horizontal velcro straps w/ a mesh ankle support & are black, white, magenta, orange, yellow & teal) and theyre so comfy & supportive! I like the bold color & chunky look but they also have other sandals in the same color-way. I can run around all day w/ no foot pain/fatigue. So i recommend timberland for some if you have the spare ‎cash (i got mine on sale but their stuff is a bit pricey)
[jx3i8k7] (score 2, diepte 0) I really love Uggs that have the "SugarSole" or something like that. It's a sole made out of sugarcane, so it's good for the earth, and it's also the only thing that has never made my back hurt. Never. I've bought a really ridiculous number of pairs of expensive, furry "FluffSugar" Sandals because my back never hurts in them.
[jx3jsfn] (score 2, diepte 0) I really like Alegria shoes, they have several styles of sandals that are actually comfortable, as well as boots, clogs, nurse shoes, tennis shoes.
[jx3qjrv] (score 2, diepte 0) Bobs by Skechers do some fab sandals, I wear them all summer. Nice memory foam cushioning
[jx3rqae] (score 2, diepte 0) I just bought some cute sandals from Vionic and they have amazing arch support!
[jx3srus] (score 2, diepte 0) Can’t say enough good about danskos. I’ll never wear anything else working on my feet and occasionally wear them at home to give my feet a break.
[jx3vwzy] (score 2, diepte 0) Dr Scholls has some really nice looking shoes with great arch support!
[jx45agy] (score 2, diepte 0) Birkenstocks and Tevas, can't go wrong with either. And all the different styles are usually comfy. Don't buy the knockoffs though, they'll end up disintegrating quickly, but those two name brands will last.
[jx56bqe] (score 2, diepte 0) Born makes sandals that have a higher ankle for support.
[jx7r7to] (score 2, diepte 0) Crocs sandals!!! I promise they’re cute and super comfy
[jxhfdjv] (score 2, diepte 0) i have hsd and neuropathy and dr scholls shoes are my favourites and they also come in a lot of fun styles
[jxa2h2t] (score 1, diepte 1) Lol absolutely not for me. My feet are completely flat always have been. I used to get Birkensticks cuz they were cute and hammer out the arch as it was too painful. I called them Blackenstocks cuz I'm black.
[jx0tpvf] (score 1, diepte 1 OP) Good call, hiking sandals! I can't believe I used to hike/climb cliffs in flip flops back when I was 18-19 years old. Obviously this was before my body truly started falling apart lol.
[jx2u8qk] (score 1, diepte 1) Oofos sandals are AMAZING!
Chaco sandals & Birks are my other go-to's.
Good luck!!
[jxa2w3i] (score 1, diepte 1) Those are good I have some. You know this pillow soft spa slippers in every color you see for $10-$20? I have many colors and they're softer and more comfortable as well as cheaper. But don't werlar them on ground or they will melt lol
[jx0tjyv] (score 1, diepte 1 OP) I need something light, heavy shoes/sandals just kill my hip/butt region, I've found.

I'm willing to shell out good money for good shoes. Invest in what keeps you off the ground, a good bit of wisdom!
[jx1tbes] (score 1, diepte 1) Can confirm! I’ve been wearing Teva (spider model) sandals since they introduced them and they really help my foot/ankle/knee pain.
[jx4eify] (score 1, diepte 1) I was going to say I love my Oofos, just like a lot of other sandals they might take some getting use to.

I also love Merrel shoes and their sandals have an equally great sole
[jx18zib] (score 1, diepte 0) https://www.birkenstock.com/us/milano-birko-flor-nubuck/milano-core-birkoflornubuck-0-eva-u_650.html 
I also second Birkenstock... These give support and comfort at the same time!
(11 reacties met lagere score weggelaten)

=== THREAD 178w93w ===
SUBREDDIT: r/ehlersdanlos
DATUM: 2023-10-16  SCORE: 142  REACTIES: 77
TITEL: Sister claiming I don't have EDS because of some heels I wore
POST (source_id=post):
I have this pair of platform heels, they are roughly 5 inches tall, with a 2 inch difference between toe and heel. I don't normally wear heels because my balance is bad, and it's hard on my legs. These are my wedding shoes because I didn't want to pay to hem my dress.

They are actually really easy to walk in. It's very secure and not wobbly on my feet. The bottoms are kind of rounded to walk easy, and are super nice on my planters.

My sister who also has eds said she could never wear them with her knees. She recently wore 4in heels to a concert and ran around the place. I told her these are basically low wedges due to the platform, and they are actually helping my knees because they force an arch.

She's like "well I have Ehlers Danlos"

I was like "uh huh, so do I"

She said "sure you do" rolled her eyes and left the room.

She is currently mad because my wedding ruins her Halloween plans. She is in college and wants to party, but we have a rehearsal dinner, and then brunch and the wedding the 27th into the 28th.

I'm a big fan of a 2 to 3 inch heel, it helps with planters and sore feet. 

Just ranting because I am annoyed. I didn't judge her in her concert get up while I needed to be wheeled out because I was in so much pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k52jyvm] (score 189, diepte 0) I’m a shoe girlie. Some days, I run around in platforms & my knees don’t care. Some days I hobble around in Toms because it hurts too much to tie shoes. EDS is inconsistent like that.
[k52lh22] (score 133, diepte 0) I've worn 7 inch stripper boots and I have EDS. Tell your **genetic** sibling to stop gatekeeping a **genetic** disorder, it's harmful and inconsiderate. My EDS and my twin's EDS are very different in severity and symptoms but we both still have it.
[k52kao0] (score 77, diepte 1) I too, am a shoe girly. I am an avid collector of Doc Martens and Converse. I second this, I’m not much a heel wearer, but if they look cute. You bet your arse EDS can suck my balls so I can look hot as fuck
[k52mbvp] (score 43, diepte 1 OP) Ours are quite different too, I was not flexible growing up, and that held my joints together into my twenties, while her and our other sister struggled with major hip issues as kids. I have fibromyalgia worst out of the three of us, the other besides her hips has much fewer issues altogether. I also have more skin issues, while youngest is shrinking because her spine is compressing. We are all quite different but very hypermobile, of which I am the least due to tight muscles… but still more than a normal person.
[k52ib4e] (score 38, diepte 0) Is she a doctor? Is she a geneticist? Wait I know maybe she's rheumatologist? No, none of those? Then she can fuck right off.
[k534v32] (score 28, diepte 2) I am the same. My BIL got married and I forced myself wear my Valentino rock stud stilettos all night - at least until I couldn’t anymore. Luckily my husband was a doll and packed flats for me. Sometimes looking hot is worth the pain afterwards and I have a huge collection of expensive shoes I’m wearing if it’s a special enough occasion, every other day I’m in slip-on vans or converse.
[k52nxh9] (score 27, diepte 2) >while youngest is shrinking because her spine is compressing

Oh my God I just realized that's happening to me. I didn't know what it was. I went from being 5'5¾ to 5'2½ over a couple of years and my mom accused me of lying about my height and that I was actually still 5'5¾ and just wanted to "seem cuter to men". Is there anything that your sister is doing to help with it or is it a "it is what it is" type of symptom
[k52zz7y] (score 23, diepte 6) Feel free to ignore this as it is completely unsolicited & not the point of your post, but I can’t wondering if your sister has issues with executive functioning? I find it really difficult to book appointments (and do many other life admin tasks) and always thought I was just lazy. Now I know I have ADHD & ASD, and it turns out those difficulties are symptomatic!
[k52loui] (score 20, diepte 1 OP) I wear a lot of orthopedic sandals, and then boots in the winter, uggs when my feet just hurt. I have insoles with arches I wear in most shoes. I never wear heals that aren’t blocky, normally heeled boots with a thick tread, not like real heels. I can’t bear the pain in stilettos or pumps.
[k52sjen] (score 20, diepte 3 OP) No, she is currently ignoring it pretending to not have a chronic illness, she was taller than me 8 months ago by about and inch, she is now probably about an inch shorter than me.
[k52l7js] (score 19, diepte 1 OP) She is a freshman that plans on being a doctor… with a rather large ego, listening to her she could just go to med school now
[k52vaec] (score 19, diepte 2) She shouldn’t actually go to med school, her attitude and arrogance insure she will be a terrible care provider and even worse diagnostician—save everyone from her, please, tell her to go into research
[k52uwu9] (score 18, diepte 5 OP) She hasn't seen a doctor since she turned 18 because she won't schedule any appointments. Maddening, as she is literally shrinking, and SHE wants to be a doctor.
[k52v3mo] (score 17, diepte 6) Ironically medical professionals are sometimes the worst when it comes to taking care of themselves medically. I have bad social anxiety so I get struggling to schedule but not getting treatment will make her get worse faster and might ruin her chances at being a successful doctor. I hope everything turns out well for her.
[k52pryb] (score 16, diepte 0) I can and have worn a variety of shoes in my lifetime. On a good day, I know I could wear 6inch heals and run in them...on a bad day, I am starting to use a cane while in my go too Ariat slip ons. This syndrome is so varied from person to person and day to day. You wear what you like and what you can tolerate (or what you are willing to suffer for). 

Don't let your sister make you feel bad. Sounds like she may need to practice "bedside manners" if she is planning to be a doctor.

And have a wonderful wedding!
[k52w2ei] (score 13, diepte 3 OP) I don't think she will make it to med school. She is too easily distracted by boys, kinda expecting her to get pregnant, and no one will raise her child to help her go to med school.
[k5358uu] (score 12, diepte 3) Oooh I love the shoe collectors in this thread 🫶🏻 I have about 20 pairs of docs and around 30 pairs of converse and i’m absolutely in love with all of them. The pain is so worth it!!
[k52u80q] (score 12, diepte 4) Oh dear, I hope everything with your sisters improve <3 coming to terms with having a chronic illness is hard.
[k52msgl] (score 9, diepte 0) Everyone's body is different. Everyone's experience with this syndrome is different. Honestly, it sounds like she is a bit immature and/or jealous of the attention you're receiving.
[k57b9w2] (score 8, diepte 7) To add to your comment, EDS is also more common in ADHD/ASD populations
[k57ihyc] (score 8, diepte 9) Totally, I keep discovering more co-occurring commonalities like Hashimoto’s (thyroid), MCAS, POTS, low iron, vit D, b12. I feel like there’s a gene set that links all these!
[k52sszm] (score 8, diepte 1 OP) My new neighbor is mean, but when I collapsed taking my dog to the fenced yard he helped me back into my house. His girlfriend asked if I have MS, she often sees me with a cane, and notices I am always home and somewhat unkempt.
[k539udo] (score 7, diepte 4) Future unethical OBGYN telling all her patients not to use BC or condoms in order to build clientele 😂
[k57dc6v] (score 7, diepte 8) YES - totally worth mentioning, thanks!! It’s been kinda funny (anecdotally) how many friends I’ve met who end up having both. 

And don’t even get me *started* on gender dysphoria, body dysmorphia, proprioception issues, disordered eating etc… 😅🤓
[k52vn0s] (score 6, diepte 0) lol i know a stripper who has EDS... her heels are insane and she walked around in them quite a bit. 

ask your sister where she got her medical degree.
[k53hv5t] (score 6, diepte 0) Well.. that’s a fantastically stupid new low on the “you don’t have EDS” dismissive arguments list! 

I don’t wear heels much and I think I only have 1 pair left, but that’s mostly due to preference and working from home. I also have particularly floppy ankles that always roll, never sprain, but cause me to lose my dignity more often than I’d like by making me hug the ground, generally in public. 

On a different, but related note, you’ve mentioned that you don’t wear skinny heels because they make your feet hurt. If that something you’d like to wear, I’d suggest looking into dance/salsa shoes (at a specialized dance store). They’re made differently to ensure better weight distribution, they’re arched in a way that supports the arch and the sole is cushioned for comfort and longer wear. I’ve never tried them personally, but I have a friend who loves heels and swore by them.
[k52ow0a] (score 5, diepte 0) My next door neighbor said I’m obviously not as sick as I claim because I wore heels to my nieces wedding.
[k52t0x4] (score 5, diepte 1 OP) No kidding, her personality… let’s just say her psychiatrist diagnosed her with narcissism as a child. That pretty much sums her up.
[k52s1h5] (score 5, diepte 0) EDS traits are a spectrum and are dynamic and I wish more people understood that! My mom who I inherited it from has always been able to do more than me because she was athletic as a kid and had much more muscle to stabilize her joints for a long time. My issues are getting worse as I am aging but my little brother, who is 9, has it somewhat worse than me in the joint department. But he doesn’t have the same GI issues that I have — his problems are more stomach-based while mine are gut-based. And our mom hasn’t had any gut problems since she first gave birth to me for some reason! Oh yeah and my mom and brother both have terrible eczema while my skin problems are totally different (my skin is super sensitive and super fragile but very little eczema; I deal with fungal issues more). So your experience is totally normal and I feel like your sister is just being immature about all of it. Also I’ve known people who wear heels regularly because it helps their foot pain so that’s also not totally unheard of!
[k535oe1] (score 4, diepte 4) I JUST got a new pair of Oxford docs for 50% off at a Tilly’s warehouse sale the other day and I was so excited. I had been eyeing them for months but couldn’t do it, then I found one of them in a box and spent the next 30 minutes rummaging through more boxes to find the other shoe. It was meant to be. 

I blame my husband for my shoe addiction now, I have at least 6 pairs of Saint Laurent boots, multiple Louboutin heels and flats, and way more tennis shoes than I probably would have bought myself before we got together. I have found that my knees don’t hurt as badly in a heeled boot, so I buy far too many of them.
[k52tc3f] (score 4, diepte 1 OP) Yeah the heels help with planters because it stretches the foot.. I think? I can’t wear skinny heels though, or heels without a platform, thin shoes hurt my feet 😅 no cute ballet flats or sandals for me, all Birkenstocks knock offs, and foam shoes.
[k5461f0] (score 4, diepte 0) There’s been whole chunks of my life where I could only wear heels. The position it put my pelvis in kept muscles activated enough that my pelvis stayed where it was supposed to. Then there’s been chunks where anything that’s not bare feet is painful and/or annoying because knees and feet both wanna do the Hokey Pokey
[k53gjqs] (score 3, diepte 2) Do you find insoles work with uggs? PF has been kicking my ass for a year and I need new shoes (and to replace my old Uggs…). I was eyeing up the MTE vans because I know their insoles are removable.
[k539zz1] (score 3, diepte 0) If your sister has watched Drag Race Eevie Oddly has EDS and wore incredible heels on that show - you should look up a clip because she does these amazing contortionist like dance routines, showing how flexible she is and making her EDS work for her
[k54s4g3] (score 3, diepte 1) I just watched a tiktok breaking down the difference between regular heals and dance heals, and I was amazed. If I wore heels more, I would be getting myself a pair of dance heals. They have more cushion, they have more flexibility in the toes, the incline is built differently, and they actually have a ledge for the heel of your foot to take some of the force off the balls of your feet.
[k5468tx] (score 3, diepte 0) Eds affects everybody differently, and also can change over the years. When I was younger I used to rock stilettos like it was nobody's business. I worked at bars that required sexy heels as part of our uniform and didn't bat an eye being in them for 6 - 8 hours at a time. Now I have ankle instability likely aggrevated from walking constantly on an uneven floor at a really old pub that flooded every couple years, and I need to make sure my ankle isn't feeling weak if I'm going to wear heels. 

Don't take what your sister is saying to heart, live your life, reject drama. As I'm sure you know, sibling rivalry is a thing, and if it wasn't this, she would probably pick a fight about something else lol.
[k547ky6] (score 3, diepte 0) Love all the shoe talk. I wear heels a lot, i also pay for it, but i pay for it when i wear flats too. My feet hurt less in heels, and i have better posture in them.
[k54djmq] (score 3, diepte 0) I used to wear stillettos like I was paid for it. The moment I got off of work (in a bar), klogs were off, and my tootsies were strapped into sky-high babies. I could run, dance, kickbox damn near. 

A few years of raising babies and having nowhere to wear heels, and I lost all the strength in my ankles (both from not walking all day and not wearing heels). I can only do wedges or a sturdy block heel now. 

Not only are my muscles weaker, but my prioproception (sp?) is garbage. 

Your sister is being a bratty teen. She'll realize what's up when she gets a few years older.
[k54khrg] (score 3, diepte 0) I have loved high heels since childhood, and wear them as often as I can. Nowadays, that’s a couple times a year, but back “in the day,” it was at least a couple times a week.

I asked my PT why I found it easier to walk in heels than other shoes. She said the heel helps the foot mimic an arch, which I really don’t have—my feet are flippers/puddles. Heels make the difference between whether my low back is killing me or not. The pain for the foot? Well, not too much different from the pain I normally get, regardless of what shoe I wear.
[k54v452] (score 3, diepte 0) Shoe girl here.  Orthotic inserts, shoes with built in arch support, and no stilettos or pointed toes are my basic parameters.  Platforms rock!
[k54zhwu] (score 3, diepte 0) Does she not realize EDS presents differently in everyone with it? Just because she can't wear a heeled shoe like that doesn't mean you're not allowed either. Sounds like she's projecting her envy onto you tbh.
[k566ef8] (score 3, diepte 0) I can't wear heels at all 😭😭😭 I wish I could, I have fat feet and heels are for skinny feet,  I would need a foot lift rather than a face lift. Bwahahaha. But I can do platforms that makes me go from 4' 10 1/2 to 5' 4" to give me nose bleeds from the heights (not real nose bleeds) lol.  What you can wear on your feet  or body even has nothing to do weather you have EDS. Or not Some days I am so much worse as far as balance, pain, dislocating joints than other day. Nothing says you have EDS just by looking at what you can or can not do on any given day.

I am so sorry you have to deal with a sibling like that. I hope you can choose to limit your contact with her. I choose very minimal contact with my whole family because they think I am faking all my medical issues.Even after my baby half-sister tried telling them what EDS is, and she doesn't even have it in her family.
[k56vjrx] (score 3, diepte 0) Your sister sounds insufferable. My apologies
[k57o0f9] (score 2, diepte 4) Lol I love the Mick
[k5a12ih] (score 2, diepte 11) Ah yes MTHFR! Haven’t been tested for that one yet but I suspect it
[k52v7fa] (score 2, diepte 0) I love my high heels. I have legit 6 inch heels that I’ve worn for years whenever I’m able to because I love them. My ankles hate me while I wear them and my hips hate me when I’m done wearing them. I do have hEDS. It doesn’t mean anything
[k53t47s] (score 2, diepte 0) Fun fact, my chiro actually recommended I continue to wear at least a low heel. He said I'm the only person he had recommended it to. He said when I started wearing these low-heel booties, my knees stopped hyperextending when standing. 

Since wearing heels regularly, my frequency of knee and ankle subluxations are way down. I don't pronate in heels either, so my podiatrist has come to agree with my chiro's recommendation. Especially considering that the custom arch-support insoles just beat up my arch and don't help the pronation at all. 

It sounds like you are right in that your sister is acting out. There is no bearing to what she said.
[k54553c] (score 2, diepte 0) Diagnostic criteria for EDS: Patient is automatically evaluated no because they are wearing heels. 

I must have missed that part of the checklist?? Teenagers are the worst.
[k5ay7oq] (score 2, diepte 1) Did you know you can only buy heels if you have correct collagen? Yep, they give everyone a full EDS and connective tissue exam when you go to buy heels and tell you that you can't buy heels if you fail

Jokes aside, it's stupid. Chronically ill people do stuff that worsens symptoms for reasons they find important like fun, looking good, etc. all the time

If I avoided anything that worsened my symptoms, I'd have to die because everything worsens my symptoms. Being chronically ill involves weighing the pros vs. cons all the time, OP should wear those heels to her hearts content and her sister can shush up about it
[k545gz5] (score 2, diepte 0) This just seems silly. And most of us could probably manage weird shoes for just a day if it's for something like a wedding or photoshoot. I used to have a pair of copies of the Vivienne Westwood ballerina platforms. I've never been able to wear heels so I was surprised to discover how easy I found them to walk in. But it's basically because they are the ultimate stability platforms, the base is a solid block of wood so my ankles didn't wobble at all, and my arches didn't hurt. I still could only manage them for a few hours at a time but I'm just commenting because not all heels are made equal, and gatekeeping illnesses is just silly.
[k550kgb] (score 2, diepte 0) Well… my knees have been subluxating since I was 12. Did that stop me from wearing giant platform heels from age 18-27? Nope. If it happened, I would fall down, my friends would call me a baby giraffe and we’d move on with our night. 😅 30+ me does make more conscientious show choices though.
[k55808e] (score 2, diepte 0) lmao when i had hip bursitis the only relief i had was w a 2.5" heeled boot bc it took the pressure off my hips.

also. hEDS, like, as part of the diagnostic criteria can and does co-occur in families. why does your sister feel the need to be special ??
[k558ci3] (score 2, diepte 0) I used to wear heels all the time when I was younger, like college age and up to about 35-ish. They were my favorite shoes to wear. I stuck to 2-3”, but I loved them. Then I started having chronic pain and my back and hips couldn’t take it anymore, and now no way can my knees do it. I miss heels. But wearing them in no way means you don’t have EDS. It just means you can still wear them on your good days. Enjoy that if it’s what you like and want to do! And congratulations on your upcoming wedding!!
(23 reacties met lagere score weggelaten)

