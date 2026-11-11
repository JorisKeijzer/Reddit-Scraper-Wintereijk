# Label-batch batch_0015

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
Schrijf het resultaat naar `batch_0015.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: a4dto3, 185vmt9, rtoh0j, 1baizsl).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD a4dto3 ===
SUBREDDIT: r/ChronicPain
DATUM: 2018-12-08  SCORE: 2  REACTIES: 36
TITEL: need some support - months glute/hip/back/shin/foot pain
POST (source_id=post):
Hi everyone,  
I am writing here mainly to get some support and see if anyone has a similar experience / advise.

I am 37 years old, female, not thin but not overweight (just few kg too much on my belly, grrr).  
I work in IT, I am doing university after work for the last few years, so that means a lot of sitting and unfortunately bad posture (on foot under the other leg, cross legged on sofa, etc)

I have been sporty person when younger, a bit inactive in my 20s and started again running in my 30s.  
Two years I started having plantar fasciitis on and off when running on my left foot. Nothing too bad.

Then last March, after being stuck at home working from home cause snow, sitting for hours cross legged on the sofa until my legs went to sleep, I started to have a very bad pain under my left glute radiating down.  
It didn't pass for few days and it kept getting worse. It was like something clenching my butt muscle strongly, and was worse sitting and laying down. To make it short, I went to like 4 different GP, I went to ER, they just prescribed antiinflamatories or paracetamol with codein and nothing was having effect.  
I went to a physiotherapist and did massages for MONTHS.  
The crazy pain went away, but left a very annoying feeling of sitting on the bone on my right side of the butt (sorry).  
That led me to tighten the muscles because of the discomfort and created chronic pain in my lower back, stiff back leg, outer hip muscles and tibia.. and lately the foot.

I went to a neurologist and a physiatrist in April and they both said I didn't need MRI because no signs of hernia, it will go away.

It never went away.  
Now I moved country. I went to the GP, he sent me to a neurologist, which did EMG in my tibia (where I have this constant tightness tension feeling), all good. He says unlikely to be hernia and prescribed physiotherapy.

I have seen two physiotherapists so far and they agreed (as I was saying for months), that my pelvis is kind of rotated on the right. That's why I feel the bone sitting -> discomfort -> bad posture -> tension -> more pain.

I have to say that my right foot has always had a slight overpronation, and now with this problems, I have pain in the foot as well, at the allux.

The only relief I have is using heating pads, they mask the pain for a while.

It is since March that I can't sit as a normal person.

I bought all sort of cushions and built a bench with holes :P  
I am using a standing desk (alternating sitting on the cushion and standing).  
I started cycling to alleviate my foot pain.

In a way it looks like they are dismissing me because I don't scream in pain.  
Everyone who checks me says I don't have signs of hernia or anything bad, just stiffness, that will go.

But.. I am in constant pain 24 hours of my life since last March. Every single day. Some days worse some days bit better, but pain always present.

I don't remember life without pain.

I have still 4 physio appointment and then back to the neurologist/physiatrist that might do MRI.

I am kind of loosing hope, I do my best to cope with this, I started going to the gym as prescribed, I try to be active and act as a normal person.. but I am not, I am constantly coping and finding ways to not suffer much.  
And as you know, it's so hard to not have an explanation.

One of my worries of course is that this will get worse. Because from the glute, went to the leg and affecting the foot.. as everything in our body is connected.

SOrry I know it's a long post and I am sure I left out important things, but I really don't feel understood by anyone and you know when all friends and colleagues seems to be healthy and fit and you struggling just to be able to... sit!

Thanks in advance for any reply!

&#x200B;

&#x200B;

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ebfm43b] (score 3, diepte 4) Pelvic floor problems do not necessarily imply you will have bowel or bladder dysfunction. I had mild urinary retention and some issues like that, but my main symptoms were pain in the glutes, lower back, tailbone, sacroiliac joints and groins. I also had pain in the perineum, but this didn't develop until much later into the disorder. Everywhere you have pain can definitely be influenced by the pelvic floor, but I am not implying the pelvic floor is your problem. I am merely saying that a pelvic floor physical therapist is the one most likely able to treat you. 

Contrary to what many physical therapists will tell you, posture is fairly overrated. There is very little evidence that posture has any influence in causing chronic pain: https://www.painscience.com/articles/posture.php

My main postural "defect" that I developed was posterior pelvic tilt. The correction for this is simple: don't stand that way! The only reason posterior pelvic tilt is problematic when you're already in pain is it does chronically pull the pelvic floor muscles tight. But correcting my posterior pelvic tilt had nothing to do with helping my pain, it just made walking, lifting, and other activities more efficient. I had a habit of sitting slumped in a chair as well which we have mostly corrected, but like I said, exercise and manual manipulation by the therapist was far more effective at alleviating my pain than postural concerns were. 

I went down the same road many people are telling you to go down here: getting MRIs, having various tests done, etc. I can pretty much assure you these tests will reveal absolutely nothing. MRIs are the most difficult modality for radiologists to read, and unless there is something obviously wrong, they won't see it. I did get a second MRI of my hips, groin and pelvic floor that revealed a slight groin tear on the RIGHT side, but that was not the side that was painful. So in the end, those very expensive tests were not helpful and I would've benefited more by getting into therapy sooner.

The only MRIs that may be worth investigating are: labral tear check, and spinal MRI to rule out things such as a herniated disc, arachnoiditis, tethered cord, etc.  

I hope this is helpful to you.
[ebgahuv] (score 2, diepte 7 OP) lol yes my entire life. I have never been able to sit normal on a chair, no idea why.  
My main posture was to put one foot under the buttock of the other leg while sitting. Don't know if it makes sense how?  
And I would spend hours like that. Always the same leg. Working in IT and not realizing time passing.

As I tried to change this I got into maybe worse postures!!

And now, for the pain, I am unable to sit ergonomically :(

In work I bought all sort of cuschions, the best so far with the holes where the sit bones are.  
But it looks like the best position is still crossing one leg over or bending forward not leaning back on the chair.

And this strains my back anyway..

I don't really have any comfortable sitting posture and even laying down is quite painful, for all the tightness.

Now I am in a recliner and it seems to be not too bad, but you know when you have that background dull pain of having muscles stretched?  
I don't know how to explain it. It's not cramps. 

The way I feel better is walking or working out (or laying down with heating pad).

But I can't live walking loool!

Anyway your comments are very helpful and reassuring. Knowing that some of the symptoms are similar and you have been able to feel better!
[ebf3t8v] (score 2, diepte 1 OP) Thanks a lot for your reply.  
I have no idea why here in Europe they seems to think doing MRI is worse.  
All the doctors in Ireland, Italy and Germany are saying that if there are no very bad symptoms from hernia, doing MRI is psycologically worse for the patient.  
I don't get it, to be honest herniation is bad ok, but I prefer to know it is that compared to some obscure problem we can't pinpoint!

For example I managed to get MRI of cervical spine because I had bad pain in my arm. It came out a protusion which doesn't affect the arm. I am more happy to know it might be the protusion and doing some therapy on it, than thinking oh my god what is this.

Sorry, just a complaint :D  
But I also read a lot that many times herniation don't cause symptoms and that's why they don't rely so much on MRI anymore.. no idea.

&#x200B;

My emotional status is a bit a rollercoster. I  have been able to move country and it is true that when I very busy itno something, I still have the pain but cope with it better. But I can't live my life trying to be super busy all the time.. :/ need to find a half way.

Being physically active is important for me also to feel I am not just loosing my body.

So I bought a MTB, I subscribed to the gym, but of course I am also afraid to make the pain worse. So I do it slowly. And to be honest level of activity doesn't seem to have an impact on pain (apart the discomfort I have all the time on the back/glute or feeling my leg stiff.. but this happens also at rest.. so it's the same).

Thanks a lot for your support!!!
[ebduki7] (score 1, diepte 0) Have you tried a chiropractor? Maybe some yoga for good stretching, and it could be from tension. You mentioned an IT job that has to be stressful, on top of not feeling well. I know with my old job I had high stress and being at a computer all day, with bad posture. Getting glute rubs daily, and getting adjustments by a chiropractor helped completely
[ebduu0n] (score 1, diepte 1 OP) Hey thanks for your reply!  
No, I haven't tried a chiropractor.  
I admit I am a bit scared to go to one :/ but I might think about that and wanted to try also acupuncture.

To be honest my job is rather boring than stressful :D but yeah all the pain started in a high stress moment.  
The only thing is that it's not changing at all if I am stressed or if I am happy!  
Only thing that changes is my emotional response to pain.

But I will keep that in mind for sure!
[ebdvweh] (score 1, diepte 2) I haven't tried acupuncture but my dad lives by going to one. I liked the chiropractor if feel so good after a session. But do whatever upu think is best. If one doesnt work maybe try the other. Oh I bought the the most expensive purple cushion to go with my economic chair and that helps. I have to say I think two of them being stacked together worked better too.
[ebf5969] (score 1, diepte 3 OP) I heard many people felt better with chiropractor. Can I ask how it has helped you? Did he do movements on the spine etc?
[ebf7lzt] (score 1, diepte 4) Yeah, and after each adjustment he would put the large tens unit on my muscles. He always started eith my hand/wrist or my neck and move down my back.
[ebehpeg] (score 1, diepte 0) You need to see a physical therapist that specializes in the pelvis. These physical therapists typically run their own practices that focus exclusively on the pelvis, or work in a hospital program that exclusively focuses on the pelvis. To help you find one in your area, the keywords would include things like "pelvic pain physical therapist," "pudendal neuralgia physical therapist," and so on. I obviously cannot say specifically what is gong on with you, but I developed a case of chronic pelvic pain that was diagnosed as piriformis syndrome initially because I had a lot of glute pain. Nothing worked except the specialized physical therapist, who does a lot of hands-on manual work and gave me exercises to do on my own. Happy to answer any questions. Also, check /r/PelvicFloor. A standard physical therapist has no idea how to treat these problems. I went to many who dismissed my case as very confusing. 

&#x200B;

I  know what you're going through. I had pelvic pain that began in December 2017 and didn't get treated until June 2018. The uncomfortable sitting pain was destroying my life. Hang in there, it does get better, and there are people who can treat this without surgery and without medication.
[ebeyob4] (score 1, diepte 1 OP) Thanks a lot, I will have a look.  
But did your pain affect also your posture / created problems to the leg or foot as it seems to be happening to me?  
Thanks
[ebf6vef] (score 1, diepte 2) Absolutely. I had severe sciatica on the left side that traveled down the leg and into the top and right side of my left foot. The foot pain bothered me, but I’ve had painful feet my entire life so it was nothing new, just worse than usual. I have never sought treatment for my foot pain because it just doesn’t bother me that much psychologically. 

My gait and posture changed in subtle ways. My upper back became excruciatingly painful after the first few weeks of pain due to these changes.  As my gait has improved and gone back to normal, I have had some recurrence of this upper back pain.  Although it’s unusual in this sub, I see that pain recurrence as a positive tning.  It has since subsided.
[ebffef5] (score 1, diepte 3 OP) I am happy to hear you feel better!  
I believe my posture has changed since my pelvis "shift".  
I have read a bit about pelvic floor disfunction but I do not recognize myself in the symptoms.

Apart from the glute/back/hip pain/discomfort of course, but I don't seem to have the others.

I will try to check if there is anyone experienced in pelvis/hip and see what they can suggest.

How did you adjust your posture?  
I am thinking to go also to check my posture, but apart noticing I sit wrong (because of the discomfort), when I walk or stand I am not aware of bad posture. Only I know my painful foot is more pronated and I can feel that walking.. and I think it's a chain, either up or down, no idea who is the responsible!
[ebg1uvl] (score 1, diepte 5 OP) thanks a lot for your detailed reply! 
I will for sure look into it.
I will do MRI hopefully, just because is the next step and to see if there is something in the spine.

I read a lot of articles for painscience.

For posture, I don't mean necessarily what is commonly thought.

I have been sitting with a bad posture my whole life, but that might not be the problem.
I changed my sitting posture according to the ergonomic lady in my company.
As I was uncomfortable I started crossing a leg over the other.
But I mean, for hours, my leg would go numb and I couldn't walk, still I kept doing it for months.
This is what I mean :) doing something "extremely" bad :P

Also I can see my pelvis being out of alignment because the bone where there are the two holes over the buttock, is a lot more prominent. And I feel in an uncomfortable way the right sit bone.
I believe this has changed my gait, causing tensions and such.

But I do see absolutely your point over "postural problems being overrated" and also "protusion and such being overrated" :)

I read that website a lot of times, it helped me feel better in the past!
[ebg9ykz] (score 1, diepte 6) Ah, you're a leg crosser like me. Yes I do believe the stress of doing this to excess is a contributor to pelvic, hip, groin and gluteal pain. I would also do this to the point of my legs being numb and never paid it much mind because it didn't cause me pain. My pelvic physical therapist has noticed this trend in leg crossers and the tendency to develop pelvic pain, as I brought up my leg crossing to her as well. Needless to say, I don't cross my legs anymore and I sit more ergonomically. 

Pain in the ischiums is very common when there is lumbopelvic involvement. I had severe ischial pain as my initial symptom, so much so they ruled my case ischial bursitis despite the fact that no scans detected an ischial bursa. After they ruled out ischial bursitis, I was given injections at L5/S1 to see if it relieved my pain. It did not, and a later spinal MRI came back with absolutely no abnormalities, not even a herniated disc. Herniated discs often are painless and are present in control patients.
[ebgcjlg] (score 1, diepte 8) I did the exact same thing, one foot under the opposite buttock. I really think that sort of thing is a major causative factor for this problem. Anyway, all things a pelvic physical therapist has seen before. I really think they could help you. It will be of tremendous benefit to you if you're in a bigger city, as this is where it is easiest to find pelvic PTs. They are fairly abundant these days. You want a PT that focuses on neuromuscular retraining, manual manipulation and exercise. Mine is big on Yoga as well. Avoid the stuff like TENS units that we know from reading pain science has no efficacy.
[ebgcv30] (score 1, diepte 9 OP) starting to google right now! I am in Berlin so there should be something. But the main problem is that I don't speak German yet.. ghhh.. although most people here speak English.

Thanks again!!! :)
[ebenshq] (score 1, diepte 0) EMG is not sensitive for enough for a wide variety of orthopedic and even neurologic conditions. 

My advice- get the MRI. Damage to the lumbosacral large fiber nerves can cause these symptoms. If this is truly piriformis syndrome as someone else pointed out, the only modality available today to image this would be MR neurography. This would also assess the health of the nerves, muscles, and musculoskeletal system adjacent to the area and should diagnose the issue if done by an experienced radiologist. This could be an early presentation of different neuropathies as well, including diabetic neuropathy. 

Don't keep doing PT. It's like grinding water for these kinds of conditions.
[ebeymuw] (score 1, diepte 1 OP) Hi and thanks for the reply, although a bit scary :(  
I am extremely anxious regarding neurological illnesses.  
That's why in the last two years I went 3 times to neurologists and different times in doctors in general.  
And this is the reason for the EMG.  
They dismissed neuropathy because I do not have symptoms which seems related to nerves like burning, tingling and similar. And my blood test for diabetes etc are good.  


I hope to be able to get an MRI in January, unfortunately Christmas in the middle makes things more difficult.  
Now I need to cope with my anxiety, expecially the anxiety of this being a bad neurological illness although it has been ruled out by all the doctors :(
[ebezu9u] (score 1, diepte 2) If it's just in your buttocks and back area you have it pretty good.
[ebf1x0e] (score 1, diepte 3 OP) What you mean?
[ebf2lwu] (score 1, diepte 4) Neuropathy can and does usually affect way more than just your lower body.
[ebf3jnh] (score 1, diepte 5 OP) Ah ok, thanks and sorry, English is not my main language so sometimes I do not get things :)  
I am more worried about other neurological disesase, so afraid I am loosing my muscles and that's why I have pain.  
But the PT did strenght test and I have the strenght. Also EMG said tibialis muscle is fine.  
So I have to try and be calm and keep looking for an answer.

&#x200B;

&#x200B;
[ebf4h1s] (score 1, diepte 6) Muscle denervation and clinical weakness can be the last step in a lot of neuropathies so EMG means nothing. In fact NCS is more reliable for diagnosing a good chunk of neuropathies. So you can have no "clinical" weakness and still have serious nerve damage going on and be unable to do certain things, have easily fatigued muscles, etc. EMG is just going to tell them what's happening when it has already happened. It's not as sensitive as MRI for diagnosing the peripheral nerve disorders you are experiencing. Yes, you keep looking. Do everything right, eat right, sleep right, walk right, drink right (i.e., water only). Let the wrong things come out.
(13 reacties met lagere score weggelaten)

=== THREAD 185vmt9 ===
SUBREDDIT: r/ChronicPain
DATUM: 2023-11-28  SCORE: 23  REACTIES: 35
TITEL: Best house slippers?
POST (source_id=post):
For context I have plantar fasciitis, fibro, and psoriatic arthritis. I recently moved into a bigger house with hardwood floors and stairs and my feet absolutely kill me and throb after simply walking across the house. Time to get some comfy house slippers!! What brands do you all recommend the most?!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kb43vjo] (score 10, diepte 0) Oofos now makes an extra thick recovery shoe.  Life changing.  It’s expensive, but worth every penny.
[kb4fg4n] (score 7, diepte 0) Sketchers - have a pair of slip ons that are memory foam inside with soles like boots. Usually I burn through slippers in 6 months or less but these have been going strong for a year now.
[kb5e61x] (score 7, diepte 0) I wear my Chacos or Birks all year around the house. I’ve never found a slipper that’s supportive enough for all my issues :(
[kb4lzsj] (score 6, diepte 0) Crocs for me
[kb4xmpp] (score 5, diepte 2) Just be careful to get a full shoe, not the one that’s a flip-flop or a slide because they are very unstable. They are not meant for walking out to the trash or any kind of walking around.

I have slipped and fallen very many times in my Oofos,
[kb4fnfu] (score 4, diepte 0) Birkenstock Zermatt Slippers
[kb4vbnt] (score 4, diepte 0) [These slippers](https://www.orthofeet.com/products/louise-beige) from OrthoFeet are my go to. They're slip on, closed-toe, and they come in widths. They're supportive and comfortable. They also come with 2 different sizes of inserts.
[kb44kg4] (score 3, diepte 1 OP) thank you!! I keep hearing oofos- I might have to do it!
[kb4zy17] (score 3, diepte 3 OP) That is so helpful as I am prone to falling too!! Thank you 🫶
[kb51yhv] (score 3, diepte 4) You’re most welcome, I only wear mine from bed to bathroom. Etc. I have a photo of them if you’d like to see why, they are super thick on one part of the shoe which is why they are so comfy and then they are uneven on the inner part. I’m clumsy on my best days. On my worst? Yeah I am a hazard to myself!

I need a full back too. Not sure if you’ve tried Dansko but they seem to work for me. I have boots and sandals and clogs and tennis shoes.
[kb47wvv] (score 3, diepte 0) Ergofoot I got them on Amazon,  sturdy with great arch support. Indoor/outdoor wear.  Comfortable,  stylish and comfortable. Priced at a decent mid point too.
[kb5inf1] (score 2, diepte 2) The flip flops work great for me.
[kb4afe2] (score 2, diepte 0) Indoor only sneakers
[kb5n528] (score 2, diepte 1) I tried the shearling-lined; sent them back for feeling flat.
[lwvkrz3] (score 2, diepte 3) Good to know. I have two cats as well so I’ll look elsewhere. Side note- highly recommend the Breeze Liter System, no stink, little mess, easy cleanup. 

The Dylan Clogs look really nice! I’m searching for warmth here in SF though, so it’s gotta be wool. I’m thinking the Glerup slippers with leather soles would stay clean. Especially since I’m only using inside.
[kb4ydnh] (score 2, diepte 1) I’ve tried two pairs of these now the Mary Jane’s, and the slippers with the back, and they are not a good fit for me. Something about them really hurts my feet. 


However, the attention to detail, and how nicely they were packed really wowed me. My best friend recommended them. I was very impressed with their return policy, how nice they were etc. 

No complaints at all.I just wish they fit my foot the way my best friends did. I definitely cannot do a backless shoe for some reason. I’m just clumsy in them. Nice shoe and very well made.
[kb4yzz3] (score 2, diepte 2) Sorry they didn't work for you! I have narrow feet, and these are the first slippers I found that come in a narrow width. Usu I can't wear backless either bc my foot slides all around.
[kb4vqe4] (score 2, diepte 0) I use arch support slides. I cannot walk around without shoes at all, even 2 mins and my feet hurt badly. They weren't expensive, think I got them at Walmart 4 years ago or so
[kb6hoxt] (score 2, diepte 1) I do the same. The only slipper I can handle at all is Sorel mules. But they still aren't as good, just warmer.
[kb71w2v] (score 2, diepte 0) I had really bad plantar fasciitis a few years ago (6 months in PT didn't help) and found that if I put PowerStep  insoles in my shoes and slippers I had greatly reduced pain. If you don't want to buy new slippers maybe give them a try.
[moyp9y8] (score 1, diepte 1) I know this is an old post, but is there a cheaper alternative?
[moyr3zo] (score 1, diepte 2) There is nothing quite like Oofos, Oomega.  I have tried them all.  They last for years.  Skechers has some very good walking shoes now but for an indoor shoe if you can, invest in Oofos.
[mp807vh] (score 1, diepte 2) New find, “Cushionaire” brand.  Sold at places like Marshall’s, TJMaxx, etc for around $20.
[kb4bfih] (score 1, diepte 0) I have a few pairs of comfy sketchers thick flip flops I wear around the house. Easy to put on and good arch support.
[lwvhei5] (score 1, diepte 1) Do the soles collect dirt and grim? I have a Baabuk pair with latex soles and they get really gross.
[lwvkcii] (score 1, diepte 2) oh yes, absolutely yes-- we have two cats and they spread litter dust all over the apartment. the soles of my Zermatt slippers were really gross.

I just switched slipper strategies actually. I was blazing through the Zermatts too quickly, ruining the insoles.

I bought a pair of plastic crocs (Dylan Clog) and have been using socks as the "insole". Too soon to weigh in on the therapeutic benefits, but the nubbed texture inside the clogs is pleasant and can be felt through the socks.
[lwvlf18] (score 1, diepte 4) My spouse had leather sole slippers and had the same litter issue, not as bad, but the leather was soft enough to get embedded debris.

Thanks for litter rec-- we were very happy with World's Best Litter (the cats have rejected pellets in the past) and the litter debris was manageable if the humans (ahem) were diligent about daily clean-up...
[lwxfadh] (score 1, diepte 5) Oh okay, so the soft leather let things get pushed into it. I wonder if more traditional rubber soles would be the cleanest then, like on the Haflinger Classics.
[lx1eijr] (score 1, diepte 6) Let me know what you decide, if you are inclined-- the plastic crocs are working so far, but aren't the best solution for me.
[lx1ew64] (score 1, diepte 7) If I remember I certainly will. What would you change about them?
[kb4gdrt] (score 1, diepte 0) All birds has some big fluffy ones
[kb4ph6y] (score 1, diepte 0) Keen. Howser slip on. It has great support, flexibility, and an indoor/outdoor sole. I also have plantar fasciitis and inflammatory arthritis. L
[kb5291z] (score 1, diepte 3) I think it’s just pure clumsiness on my part. They are wonderful for what I use them for which is true recovery after a long day walking in my regular shoes, sitting on the couch and just need to run to the restroom or from bed to the restroom, etc. but I can’t wear them for any length of time walking because I will fall on my face. 😂
[kb5mmjq] (score 1, diepte 0) I think be sure to get rubber soles. High risk of feeling like you're wearing the box otherwise; IME.
[kb5zgvv] (score 1, diepte 0) I like the Uggs with the fleece lining and heavy rubber sole.
[kb6dr94] (score 1, diepte 0) I got Birkenstock clogs (I only wear indoors) and I love them
[kb6nlaf] (score 1, diepte 0) Wool loungers by allbirds
[kb6r7q9] (score 1, diepte 0) My mother swears by the Isotoner memory foam slippers. She orders them from Amazon, but they might be available where Isotoner products are sold in person.
[kb7calc] (score 1, diepte 1 OP) This is a great idea!!! Thank you!
[kb7c610] (score 1, diepte 0 OP) I so so so appreciate everyone’s suggestions! Will take in everyone’s comments to consideration as I make my decision - thank you!! 🫶
[kb7m6px] (score 1, diepte 0) I got a pair of knock off cloud steppers from Walmart. They don't keep your feet warm but they are super cushiony and comfortable. My feet used to hurt so bad waking in my hard floors. Now I have no issues at all
[kb7x79z] (score 1, diepte 0) I have gotten around 20 people into oofos and I will continue to be obsessed with them. I have sandals and slippers and sneakers by them. 

I have plantar fasciitis that no longer is blaring at me. I no longer have bunions causing feet issues. And my knee pain is so much better.
[kb8aehd] (score 1, diepte 0) I recently got Isotoner Mallory Hoodback slippers and they are extremely comfortable. I don't have plantar fascists but is do have undiagnosed pain in both feet. Plus, I multiple structural problems with both feet but mostly my right foot. 

My doctor recommended to wear my orthotics in my house shoes. So whenever I will be on my feet for an extended period I take my insoles out of outdoor shoes and put them in an old pair of shoes that are strictly indoor shoes.  I just bought Easy Spirit slip on shoes online and I'm hoping they fit well to replace my old shoes.
[lplz73u] (score 1, diepte 0) Hey! I totally feel you on the foot pain, especially with all that going on. I've been dealing with similar issues and found that a good pair of house slippers makes a world of difference. IMO, you should look for ones that have a lot of arch support and are super cushioned to help with the plantar fasciitis and arthritis. I've personally tried these comfy house slippers and they have been a lifesaver on my hardwood floors. My feet don't throb as much after walking around, plus they're pretty stylish too. You might wanna check out [these slippers](https://link.tastechocolate.co.uk/slippers-plantar) and see if they help you out as much as they did for me. Trust me, your feet will thank you!

=== THREAD rtoh0j ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-01-01  SCORE: 22  REACTIES: 33
TITEL: Long Distance Walking Shoes
POST (source_id=post):
I feel like a dork posting this here, but I don't know where else to go.

I do a "100,000 Steps in 24 Hours" challenge every January. A portion of the steps are from running, which I can do in my current running shoes, but I'm looking for a shoe for the walking portion.

In the past, I have used older versions of the Ghost because that's what I ran in at the time. I've been running several years but just got into better shoes this last year. 

I currently have the Endorphin Shift and Speed. Both hurt my knees when I walk over five miles, likely due to the low speed and rockers. I don't love the Ghost line, so I'm hoping to find a better option than going with those again. 

I am looking for a shoe that I can walk at least 30 miles in. 

The walking will be done on a variety of surfaces including a tightly packed gravel trail, road, and sidewalk.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hqugpuk] (score 18, diepte 0) I’ve studied walking biomechanics over long distances and we found that if you are on a relatively even surface, a minimally cushioned, flexible, minimalist shoe seems to be the most comfortable for most people. 

Anything with a rocker or plate is the very worst for walking. 

Too much cushion seems to cause hip and/or knee pain in a substantial number after a few hours of walking. 

We found the Altra Escalante worked well for long distance walking, or if you have a narrower foot, something like a Nike Free.
[hqtyn9i] (score 9, diepte 0) Perfect place to post this. Sounds like you need something robust, something comfortable because of the duration, and a shoe that is durable. I really think the perfect fit would be the Ultraboost 19 or 21. The fit around you foot is God tier. The Midsole is a extremely comfortable plush feeling. The outsole is continental rubber; one of the best. The boost foam is firm which means less energy expense. Not sure if that’s actually noticeable tho. And there’s even some weird steel plate that supports the midsole and lines the outsole, which no one talks about strangely. 

I use the UB 21 to walk to work (2.5 miles each way) I use the UB for my easy day/rest day active recovery. And it’s this weird, durable, comfortable, tank of a shoe that won’t let you down and feels like heaven to walk in. 

Ppl dismiss the Ultraboost line up bc it’s so heavy, approx: 12 oz for men’s size 12, but your getting a lot of shoe and a lot of value. Specifically for running which is 3x the force load of walking..I bet the shoe could do 600 miles and even more. It will hold up on your roads, gravel and grip in the snow. And… you’ll look fashionable while you do it!
[hqujnf8] (score 7, diepte 2) We think it is because the cushioned soft platform “turns off” proprioception in the foot and this causes a transfer of forces up the kinetic chain, probably because the foot has to roll through the big toe in a walking gait and too much cushion gets in the way.
[hqui8w1] (score 6, diepte 1 OP) I would not have expected extra cushion to cause knee and hip pain. That is great to know. Knee and hip pain usually plague me in the last third or so of the walk. Thank you for the advice! I'll look into minimalist shoes. I was going to look for the opposite, so I'm glad you commented.
[hqu8f57] (score 3, diepte 2) I got mine in velvet red to let everyone know what’s up
[hqtyjr1] (score 2, diepte 0) I used the Hoka Cavu 3 Slip as casual shoes. Had no issues with them. They are unfortunately discontinued. Pretty sure the Cliftons would also do the job.
[hqu7tgi] (score 2, diepte 1 OP) This is a great answer. Thank you! The Ultraboost is a beautiful shoe and I've had my eyes on them. It sounds like I have a good excuse now, especially if they're decent for easy running days too.
[hqueipg] (score 2, diepte 5 OP) Ah, that makes sense. Thank you!
[hqu1gg2] (score 2, diepte 0) Invincibles or something simple like a Nimbus?
[hqu8tuh] (score 2, diepte 1 OP) Oh wow, I just looked these up because I hadn't heard of them. They look amazing.
[hquo74e] (score 2, diepte 0) I got the Ultraboost 21 and it has been great for walking (10 miles is what I usually do) but average-mediocre for running though in case you are thinking about it
[hqu821k] (score 1, diepte 1 OP) Cliftons do look like they would be super comfortable. Thank you!
[hqucgqk] (score 1, diepte 3 OP) I love it.

Do you know if the 20 is any good? Or should I stick to 19 or 21?
[hqudeoa] (score 1, diepte 4) About the UB 20.. I just remember it has less Boost foam in the heel, and looks like a much smaller shoe. I don’t really know too much
[hquogho] (score 1, diepte 1) I tried an older ultraboost for walking and I got really sore feet. Because the boost is so squishy and wobbly it moves around too much under my feet. Didn't like them a lot for running either to be honest, but for walking they were terrible.

I'd try something "low tech" like the new balance 680
[hqyqwvn] (score 1, diepte 2) The UB21 is quite firm.
[hqu8miz] (score 1, diepte 1 OP) The Invincibles look like they have great cushioning. Good call!
[hqvvs6u] (score 1, diepte 2) I just started running a couple months ago. Bought Invincibles.

Developed IT Band Syndrome in my knee running with them. Admittedly after seeing a PT and doing stretches and strengthening for a month its now gone, and I am realizing it was primarily due to my running technique being poor (Heel striking and overstriding).

With that being said, the shoes not that stable so be careful. Now that I've fixed my stride ill be trying them again and think they'll be fine. I've walked a few miles in them before and had no issues. Haven't had a chance to test them at higher mileage walking yet but they sure are cushiony.
[hqvwipv] (score 1, diepte 3 OP) This is good to know, thank you.
[hqu4ajj] (score 1, diepte 0) Their price tag hurts (though you can find discounts) but the New Balance Lerato is a phenomenally comfortable and supportive walking shoe. They're heavy and built up enough to hurt their running performance, but for hours and hours of walking they're hard to beat.
[hqw3num] (score 1, diepte 1) I had these and wasn’t a fan at all. Made my feet hurt after 1 hour. Had to sell mine
[hquduej] (score 1, diepte 0) I don’t think this will be a popular opinion as they  do not have a ton of support or cushioning but I have always enjoyed walking in the Saucony Kinvara.  

They fit my feet well and are very light and flexible so I forget that they are there, which is basically all I want from a walking shoe.
[hquf0tv] (score 1, diepte 1 OP) So far I haven't met a Saucony I don't like. I'll look into these. Do you know how they compare to the Ghosts, support wise?
[hqul0x9] (score 1, diepte 3 OP) That does make sense!
[j0i3fgo] (score 1, diepte 1) Which Nike Frees specifically? there are many models and look different on the insoles. Also I reckon these are almost like a sock, so would be cold in winter.

I walk one hour a day and I bought my first running shoes, Adidas Galaxy 6 M, my forefoot become stressed, like my weight sits there, boomed. Now I need to find an alternative.
[hqur8e8] (score 1, diepte 1 OP) Do you have any knee or hip pain with these when you walk 10 miles?
[hqurlrt] (score 1, diepte 2) Nope
[hqurov2] (score 1, diepte 3 OP) Awesome, thanks!
[hqw7bop] (score 1, diepte 0) Rather than shoes, i would prioritize getting good insoles.  I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com) and immediately all my foot  pain went away and i can walk in them non stop.. These are made from cork so they mold to your arch and absorb shock/impact. and obviously way more affordable than custom, and really comfortable.
[hqwnk3a] (score 1, diepte 1 OP) I didn't think about insoles, thank you!
[hqx57p5] (score 1, diepte 0) Yours is the topic I like the most. The one I'm here for.

On my walk to find the best shoes that answer it, I've discovered: **New Balance Fresh Foam More v3** and **Nike Zoom Fly 4**.

The first ones are the most comfortable; the latter the faster.
[i02e5x5] (score 1, diepte 0) I just found this thread on a Google search. I’m wondering what you ended up getting, /u/powelale000, and whether it worked well for you.
[i03nhn6] (score 1, diepte 1 OP) I ended up using the Adidas Ultraboost 21 and they did work well for me. I didn't have any foot, knee, or hip pain for this year's challenge.

=== THREAD 1baizsl ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-03-09  SCORE: 17  REACTIES: 33
TITEL: My Dad's suffering through awful chronic foot pain for months now and the doctors don't know what to do, he's barely functional
POST (source_id=post):
I'm sorry if this is the wrong place to post this, especially since it's technically not me whos suffering but I'm desperate and don't know what to do at this point.

I wrote a more comprehensive post about the situation [here](https://www.reddit.com/r/FootFunction/comments/1b858i9/awful_ongoing_foot_health_crisis_in_family/) since I don't think I can write a post this long here, if anyone is interested. I made a throwaway for that post but since I can't post on here with it I dug up this old account.

Long story short, my dad got a horrible stinging feeling on his 5th metatarsal seemingly out of nowhere and despite not really bearing more stress on that foot than usual. The swelling itself seems to be the cause of the pain, which is excruciating and constant, independent of weight bearing, cooling or anything. Nothing can stop the inflammation and pain except Cortisone, which he was forced to take for almost 2 months now. If he stops using it it will return and things will be just as awful again. The doctors couldn't see a fracture or bone bruise on the MRI or X-Ray and the blood tests don't show anything out of the ordinary. They have been going back and forth on a possible fracture, gout or arthritis but nothing seems to really be the case and the doctors aren't digging deeper into this. They've even made tons of mistakes on the way which cost us a few weeks. 

He can't go outside, he can't go to work and the cortisone is starting to show sideeffects. Over these last 2-3 months my dad and my mom (who is also chronically ill) have become incredibly depressed and suicidal and I have to somehow help two parents with seemingly untreatable diseases through all this. I'm starting to lose it and don't know what to do. Does anyone have a similar experience or can offer any advice? These last months have been hell.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ku2pqfv] (score 8, diepte 0) I saw a similar case in the past, and after two years, it was finally discovered that the problem was in the spine. Maybe you could have your spine checked by a doctor.
[ku2qvrf] (score 4, diepte 0) I have a lifelong struggle with foot pain. I had extensive reconstructive surgery when I was around 25. One thing I stumbled on that helps my foot pain is a walking cast (aka air boot). So while I don’t have help on the diagnosis side, I would say an air boot might be worth a go. If you’re in the US, you can get one relatively inexpensively on Amazon.
[ku4tj11] (score 3, diepte 3) Ah ok. Best of luck on getting relief.
[ku2v939] (score 2, diepte 1 OP) Oh interesting. I do know he has Scoliosis and struggles with back pain. He also suspected a fracture first cause his posture distributes the weight unevenly on the problematic foot (but the scans say otherwise).

Do you remember how the back caused such weird behavior lower in the foot and how it was treated?
[ku2xmdu] (score 2, diepte 2) A small hole was found in the spinal cord. I don't remember it very clearly now.
[ku30bog] (score 2, diepte 2) Is gout like other autoimmune diseases? I have suspected rheumatoid arthritis and my doctor warned me that my blood test could very likely come back normal, but that wouldn’t mean that I don’t have it.
[ku2sc3d] (score 2, diepte 0) Had he seen a Podiatrist?
[ku2u98r] (score 2, diepte 1 OP) Not yet, the next available one is super far away and it takes over a month to get an appointment. But it's something we'll try
[ku39631] (score 2, diepte 3 OP) Yeah you're right. My dad is also suspecting Morton's Neuroma or something similar. We got MRI, x-ray and even ultrasound images but the Orthopedist didn't find anything crucial in there. But maybe a Podiatrist could see more. Do you know how something like Morton's Neuroma can be treated normally?
[ku3aogi] (score 2, diepte 1 OP) That really sounds like horror. We'll try to get in contact with a Podiatrist somehow to find a solution. My dad considered Morton's Neuroma as well so we'll keep this in mind. Also thanks for the insight on the medication, I'd love to hear an update on the Lyrica and am wishing you the best. I really hope it's gonna help you!
[ku3b4nh] (score 2, diepte 1 OP) Yeah sadly it really is. It was just especially frustrating that during this entire ordeal the doctors we went to just came to the most basic conclusions and despite my father giving them feedback that would contradict their diagnosis they simply dismiss it instead of digging deeper. The orthopedist was convinced it's gout while the house doctor is somewhat clueless and switches between micro fracture and arthritis.
[ku3cbc4] (score 2, diepte 2) Go see a sport orthopedic doctor. They might have better understanding of the issues. It could just be a pinched nerve.
[ku4b5zi] (score 2, diepte 3 OP) We went to one for over a month now and that guy insisted it is gout even though the inflammation doesn't start in the joint and it shouldn't last this long. The MRI just showed slight irritation next to the bone so he immediately ruled out a fracture. He became really passive aggressive as soon as my dad suggested looking deeper into it from other angles. Definitely someone that did not want to be questioned at all. Still, My dad even takes medicine against gout currently which is risky just to be sure. A rheumatologist is someone we will probably look into as well. Just sucks that it takes over a month to get any kind of appointment with someone that isn't your main doctor here.

But you're right, an orthopedic doctor should know what this is about.
[ku4kcpe] (score 2, diepte 4) Sounds like a sound next step. Have you tried a neurologist?
[ku9mdxj] (score 2, diepte 5 OP) No not yet unfortunately. It takes ages here to get in contact with one. It's all a painfully slow process
[ku380vp] (score 1, diepte 3 OP) Oh damn that sounds bad, I hope it's not so severe
[ku2uyf8] (score 1, diepte 1 OP) Yeah it really really sucks. He's actually already got one. And while it helps him walk in the worst case scenario he can't drive manually with it and public transport is awful where I live. I think the main issue is that the inflammation starts without a real cause and keeps getting worse no matter if the foot is under any weight or not. Even when he stays in bed, cools his foot and doesn't move it, the swelling and inflammation increases the the point where it's starting to creep up his leg. And only Cortisone can stop it which is bad. That's why some doctors thought it wasn't a fracture but instead gout. His Uric Acid was a little high when he made the first test for that but now they're normal. The pain is also not directly in a joint but right below it. And the acute pain lasts way longer than a normal case of gout would, so it's really up in the air still.
[ku38l85] (score 1, diepte 3 OP) Not really. The way I understand it it's your body having too much Uric Acid and that can lead to crystals forming, which mostly happens within the joints. It would explain the accute pain even when elevating the foot and all that but most of the time gout doesn't persist for so long. He's currently taking medicine for gout but it's a shot in the dark. 

But you're right, you could even have gout despite your Uric Acid levels being low. This, bone fractures and arthritis all seem plausible but nothing can be determined for sure which makes treatment such a pain. And currently only steroids can help his inflammation.
[ku30fuh] (score 1, diepte 2) I do hope he finds the answer and starts feeling better soon. Foot pain is so devastating because it affects the whole body.
[ku38rn1] (score 1, diepte 3 OP) Yeah it's awful. He's normally moving around a lot and loves being outside and this is killing him. Not moving his foot is also detrimental to his tendons and muscles there and increases his bad posture so he kinda has to walk "somewhat" normal without putting too much pressure on the foot.
[ku344ez] (score 1, diepte 2) This is it. Mine is nerve issues. A podiatrist recognized it immediately. Said my neurologist n primary would never find it n he was right. Ask n look into Morton’s Neuroma and any other issues know to affect the nerves in this area of the toes n feet. MRI n Ultrasound is usually needed to find the problem areas. A Podiatrist is probably your best.
[ku3bdp2] (score 1, diepte 4) Ok so there’s different ways. Injections are first obviously. Now it gets crappy. There used to be a very effective dehydrated ethyl alcohol injection that was commonly used. The patent was bought a few years ago n the company rebranded it for cancer treatment. Used to be $1000 n totally covered by insurance. Now it’s $20,000 and good luck finding it. Cryoablation is another promising option but is also impossible to find a doc what does it outside of cancer treatment. Radio Frequency Ablation deadens the nerve with heat n that’s scary to me. Surgery to remove the peripheral nerves is another option but I read about lots of problems with nerve regeneration. The most promising surgery I’ve seen is where, in Morton’s Neuroma, they cut whatever is pressing on the nerve to allow more room. I’m desperately searching for answers myself. I would love cryoablation but nobody does it outside of treating organ n heart stuff and cancer.
[ku2v1u9] (score 1, diepte 0) I get stinging pain in my 4th toe. It about drops me to my knees. It’s coming from my spine at the S1 nerve root. Have they looked at his spine?
[ku2vq5i] (score 1, diepte 1 OP) I'm so sorry, that's awful. We haven't yet but it really sounds like it's worth checking out since he does have back problems. Did it also lead to awful inflammation and swelling?

Cause the weirdest thing is that the inflammation itself seems to cause the most pain. Cortisone, which is a steroid that should only treat the swelling and isn't a real pain killer, eleviates 90% of the pain he has.
[ku2whni] (score 1, diepte 2) Yes, my feet swell too. It eventually started affecting my heels too and they swell and get pink.
[ku2wuen] (score 1, diepte 3 OP) Yeah that sounds quite similar. It's only when the swelling reaches a certain point that the pain becomes unbearable.   
How are you treating this condition? I hope something worked out for you!
[ku2y1ur] (score 1, diepte 4) In my case there’s not a lot they can do for me. Mine occurred after spine surgeries. In your fathers case, he would have a lot of options on the table if it is indeed spine. It seems like something to consider at this point if every local foot problem is coming up negative. 
My stinging pain is a localized spot. It feels like somebody took a hot needle and stuck it in my toe. Or I got stung by a bee on my toe.
[ku39piz] (score 1, diepte 5 OP) I really hope that something can be done if it's the case. It really does sound like a very similar case. Can you even walk with pain like that? Or do you take something to treat the symptoms? I mainly worry about his mental health currently cause it's declining rapidly together with my mom's.
[ku335pq] (score 1, diepte 0) I have a similar issue with my right foot second toe for over a year now. Still being treated for a solution. A podiatrist actually found the problem. For me it’s the nerve that splits into the peripheral nerve of the big n second toe. It’s pinched or entrapped. I’m waiting on better images. He accidentally injected the nerve directly the first time n it lit up exactly where it hurts, then went numb for two days. Never had such relief. Later injections that didn’t hit the nerve directly did not help as much. Also look into Morton’s Neuroma. This affects the area described and presents similarly… What helps me? Gabapentin, doesn’t always erase the pain but it makes it manageable. I’m trying Lyrica today but it’s literally the first day. Opiate meds help if flare up is insane but not as much relief as expected by themselves. Benzodiazepines help a bunch but it’s not sustainable, n docs don’t prescribe for it long term. Idk how I feel about this honestly and it’s a quality of life issue for some. NSAIDs don’t do much. Tylenol helps a little. Waiting on a prescription cream with gabapentin in it so I’m hopeful. Can update on the Lyrica later.
[ku3ap9f] (score 1, diepte 1) If the nerve is pinched or entrapped they're not going to release it?
[ku3cknf] (score 1, diepte 2) Waiting on better images to determine exactly where n what I’m dealing with and how to proceed. Injections have not worked so far. Nerve could also be damaged too bad. Idk right now.
[ku9mmw7] (score 1, diepte 3 OP) Uncertainty like that really is the worst. I'm wishing you the best as well!
[ku36iyd] (score 1, diepte 0) What doctors actually know especially about nerves is so little. A comparison my neurosurgeon told us, “If all medical knowledge was the entire pacific ocean, what we know about nerves wouldn’t fill a thimble.” 

It’s so hard knowing this, having chronic nerve pain from nerve damage. But my dentist has a nerve issue in her wrist yet they don’t know why after months of testing… 

This is our norm.
[ku375oi] (score 1, diepte 0) The swelling is foreign to me.  Foot pain for 4 years now.  Due to diabetic neuropathy and I deal with a compressed L5 S1.  I’d recommend going to a pain clinic who can also offer PT.  He need to function and they will help.  I had a great physical therapist who taught me to to properly exercise to improve my state (I’ve also had ablation in between the 2nd and 3rd and 3rd and 4th metatarsal to cool off the nerve in both feet.  It felt like a hot coal embedded in my foot for over a year.   I found a specialist who agreed to that procedure since the pain was so intense.  It helped considerably.  Good luck I hope you help them find relief
[ku379tf] (score 1, diepte 0) L4 L5 nerve impingement,, I’ve suffered for many years, next is neuropathy,
[mlhn4fd] (score 1, diepte 0) Did yall ever find out what was going on?

