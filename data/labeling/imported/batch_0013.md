# Label-batch batch_0013

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
Schrijf het resultaat naar `batch_0013.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1kk7vpn, yamnus, tg6rkm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1kk7vpn ===
SUBREDDIT: r/ChronicPain
DATUM: 2025-05-11  SCORE: 28  REACTIES: 58
TITEL: Looking for sandal suggestions for my specific needs- What I need doesn't seem to exist for adults
POST (source_id=post):
I have hypermobility, overpronating weak ankles, moderate flat footedness and all these issues require me to always wear rigid hiking boots with a lot of ankle support and custom made orthodics from podiatrists... but wearing hiking boots in the heat of summer makes me absolutely miserable due to my (not yet diagnosed) Erythromelalgia symptoms (makes feet red hot) and extreme foot sweating from the heat which can result in sandals that reek that I desperately want to take off to cool my feet down but can only do so when I'm completely alone and in a well ventilated area...otherwise it's unfair to others to subject them to the smell. 

In the past I've had birkenstock sandals with my orthotics built in but they weren't ideal for ankle support and more importantly- they reeked because of the fabric insoles which would build up dead skin cells because my feet sweat so much it's like soaking them in water and eventually they fell apart because I tried to hand wash them often to get rid of the gunk and smell but they were not waterproof. 

They were quite expensive and barely lasted 2 years so I'd rather not go through all that again with un-ideal sandals. 

Can anyone offer me any suggestions? Thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mrssqkv] (score 20, diepte 0) Sounds like you need a cobbler. They still exist. Your design looks easy to accomplish with leather.
[mrshowf] (score 13, diepte 0) Don’t have any advice but I’ve noticed it’s really hard to find good shoes with support! I hope someone can help. I wonder if any companies do custom shoes?
[mrso9h3] (score 8, diepte 0) Good luck op but this second page could be cross posted to blurred images. We really didn't need the ai to get the point across. Anyways I would love if a company made similar designs to the first picture for adults. I also have only had luck with hiking boots
[mrsj38q] (score 7, diepte 1 OP) All I've found is hiking boots because shoes are always below or on the ankles but not fully supporting and I've had "breathable" orthopedic shoes but the only way they are breathable is if air is blowing directly on them
[mrsq7r4] (score 6, diepte 0) Might suggest some gladiator type sandals. Did a quick search but the ones I immediately came across the ankle support looked a bit dainty. The style seems awfully close and I'm sure if you searched longer than the two minutes I did you might have some luck. Not too mention looking like some sort of badass gladiatorial warrior
[mrsq4d9] (score 5, diepte 0) AI is ruining the planet
[mrt71xp] (score 5, diepte 0) Why don't they exist!? I wish I could have the kid's pink ones! 💖
[mrv5lcp] (score 4, diepte 3) Way off topic. Pain dude. Not ai generated argument. Lame.
[mrssyw0] (score 4, diepte 0) "Orthopedic gladiator sandle with ankle support"

https://jerusalemsandals.com/products/rebecca-brown?variant=19760372580448&gad_source=1&gad_campaignid=22238124623&gbraid=0AAAAACsI7F2d2o4Q_VXEK48xj0t09ShlV&gclid=Cj0KCQjwlYHBBhD9ARIsALRu09o3jNPUarQgxtDkmINHS1Vd_TjvjnGCMSElphoZq0gl6MEmkl8r4X4aAgkTEALw_wcB
[mrsvlbs] (score 3, diepte 1) I got custom orthotics that fit into shoes specifically made for placing otthotics in. I first heard of a brand with zippers that catered only to kids, but Dr Comfort made shoes with the top removeable by velcro. I can post a picture of them if my description doesnt make sense.
[mrt8r9c] (score 3, diepte 5) https://taycobrace.com/products/athleticx-brace

How about an over the shoe style brace?
[mrsz28o] (score 3, diepte 1 OP) Honestly I would have drawn a design myself but I'm dealing with pain in my hands at the moment
[mrtg9xq] (score 3, diepte 1 OP) Foot pain is ruining my life?
[mrt2cu8] (score 3, diepte 0) i just wear an ankle wrap with the sandals. my current functional sandal is Nike Air Deschutz. size up and add your insoles
[mru0izz] (score 3, diepte 0) Dr martens have a sandal that goes around the ankle
[mrt9pkq] (score 2, diepte 6) https://www.mouldedshoeny.com/custom-in-house

I've also seen good things in reviews mentioning this particular shop. They seem to be able to make custom shoes and deal with orthopedics. Perhaps reach out to them or a similar shop and they can give you some advice.
[ms1fu82] (score 2, diepte 2) Exactly I can’t use my hands fuck Ai haters
[ms1fzlb] (score 2, diepte 4) Don’t feed trolls AI is fine also artist with hand issues. Use what works. Love this idea
[mrvdxdg] (score 2, diepte 2) oh so you have no skill
[mrthhmw] (score 2, diepte 1) “hand crafted in East Jerusalem” or we could boycott israel
[mrt0k0l] (score 2, diepte 0) Custom orthotic insoles basically precludes off the shelf sandals?

  
I don't know how many cobblers still make their own shoes, but I think that finding a custom route is going to be the way you need to go.
[ms6lktj] (score 2, diepte 2) Yes! 💖 xx
[ms6ou9b] (score 2, diepte 3) I talking to factory workers in China for yall.
[ms7o9a8] (score 2, diepte 3) “We have not yet developed the adult section “. Maybe in the works. Change.org or get me a pair I can reverse it. Just parts.
[msdfya1] (score 2, diepte 5) Prob. Molds. Resin printer. Laser cutter. I’m a professional reverse engineer
[msdg2f2] (score 2, diepte 5) Can almost do this with enough pictures and material info.
[mso4rd4] (score 2, diepte 7) Ok I’ll approach with my quasi Dr nomination and ask for a trial in USA for adult versions and see what is up. What size are you?  No promises but if these are truly in demand and I can prove it, plus say prescription coverage it’s bank for them. Long shot. I’ll look again but if I had a pair I can figure out everything like stitching and make low volume replica, might need industrial sewing or a form of molding. Everything else looks like I can laser cut. Eva foam and leather. I essentially need to know their raw materials. I’m very serious I know the guy who made croc gloves and got cease and dedist. Gotta hustle art but love side quests. I’m getting into accessible fashion anyway. 

Accessible Accessories
[mrvtkql] (score 2, diepte 0) It sounds like you need to visit an orthotist, who will have some ideas for better ways to support your feet such as an AFO.
[ms1i1lr] (score 2, diepte 0) I dig these. https://www.drmartens.com/us/en/vegan-blaire-womens-felix-gladiator-sandals-black/p/23806001

Keen also
[ms1isbf] (score 2, diepte 0) Try r/hypermobility sub?
[mrt7btn] (score 1, diepte 4 OP) Yeah that's unfortunately what I've come up with too in my research. Sadly, I've been to over 8 different podiatrist/chiropodists over the years and it's something I've been dealing with for over 20 years or so since the age of 9. 

The pediatric shoes I've seen do not go as high as a women's size 9, wide Sadly. 

The problem with most if not all ankle braces I've come across require it to go underneath the center of my feet and it's either extremely uncomfortable as I have a mystery chronic foot pain condition that's completely baffled doctors, chiropodists, podiatrist and physiotherapists (that's why I've seen so many through the years) but the pads of my feet are hyper-hyper sensitive and cannot take any form of pressure to them (unfortunately this includes simply wearing shoes or resting my feet on the floor while sitting) and any lumpyness the under the foot part of the brace. Also the under foot part is too tight if I put my custom orthotics in between it and my foot and it's too lumpy with my orthotics underneath the brace. 

Plus, a lot of the braces are thick cloth that isn't as washable either and will add to warmth which adds to the sweating and when my feet feel hot it makes the rest of my body overheat. 


So the choice is either do a brace and sandal combo thing which wouldn't be as comfortable if not actually be more painful with hardly any breathability which leads to stink and sweat...OR...wear more physically comfortable hiking boots that give ankle support and fit my orthotics fine but have chronic swamp feet and extra rank boots. 


I'm desperately hoping that I don't have to compromise and that something out there exists because surely I'm not the only adult out here with weak ankles and hot feet right???
[mrtf358] (score 1, diepte 6 OP) Wow! I haven't come across that kind before! That definitely could change things! I'll definitely look into that, thanks!
[mrv5z18] (score 1, diepte 5) We can just reverse engineer the child stuff bigger
[mrv5hbt] (score 1, diepte 1) I needed the AI. Speak for yourself. I’m putting this in fusion to generate a shape. Plus comfy ui workflow then unwrap to cut.
[mrsq0s2] (score 1, diepte 0) Sounds like you're looking for some type of gladiator sandal?  I don't know from experience which ones will meet your needs, but that search term might help.
[mrtk7eb] (score 1, diepte 3 OP) I've been dealing with this issue since the age of 9, I'm nearly 30 now. I've been to over 8 different chiropodists, podiatrist, doctors, foot clinics etc etc etc... I can be incredibly descriptive when I need to be but it got me nowhere. Now I'm having my last ditch effort with Reddit and posting photos to hopefully gain more attention and potentially more responses in the desperate hope for change. 

I live as sustainable and environmentally conscious as I can within my means and definitely a bit better than the average person at the very least. I am an artist and I understand the downsides of AI art and the jobs it effects....but it's hard to care about it when my feet are on fire.
[mrv5ti2] (score 1, diepte 4) AI is fine. I can help prototype I have laser and design skills. It’s just straps?  Leather?  We could reinforce with delran. Keep doing AI screw the haters it’s cheating to them but we get ahead.  Love the generations. Dm if wanna jam.
[mrvpb2w] (score 1, diepte 6) Have you seen the good?
[mrv5j6n] (score 1, diepte 1) Uhhh I’m making these with AI.
[mrvp8wt] (score 1, diepte 3) Can you make these?  I’m skilled and just faster directing as needed to offload. 

Again off topic, AI is just a tool.
[mrtfpu4] (score 1, diepte 1 OP) Unfortunately not all orthopedic style footwear means it has ankle support like this particular sandal. Sometimes "orthopedic" just means they've got more cushioning and can accommodate orthotics
[mrt3y2s] (score 1, diepte 0) I wera Finn Comfort sandals.   They don't have ankle supports, though.
[ms1friz] (score 1, diepte 1) Let’s reverse engineer them!
[mscqwby] (score 1, diepte 4) If only!💖... I wish it was possible! Should I become rich enough to get a custom made pair of shoes, this is what I'd get! Also, we would need a winter version!
[mscrexw] (score 1, diepte 4) 😍.. Ooh, maybe they'll make adult ones?... 🤞 could you really make a pair if you had one to copy?! 🙏😍xx
[mskslmz] (score 1, diepte 6) Ok now I'm excited! 💖 xxx
[mspmf50] (score 1, diepte 8) I'm in the UK, so I'd have to pay. But I don't care! I'm a UK size 4. Sometimes 3 if they come up small. 3 1/2 is perfect! OOOH let me know how you get on! 🤗💖🤞🌸
[mrv5usa] (score 1, diepte 1) Pointless comment
[mrvp0i2] (score 1, diepte 3) For u
[mrzqqm4] (score 1, diepte 5) Ah yes, the objective claim that generative AI is environmentally harmful—bold words from someone probably typing on a lithium-powered device built halfway across the world.

Yes, training large models like GPT-4 can consume significant energy—estimated at around 552 metric tons of CO₂ for one training cycle (Strubell et al., 2019). That’s not nothing. But declaring AI as inherently harmful ignores the downstream benefits: faster scientific simulations, energy grid optimization, smarter agriculture, and even carbon sequestration modeling—all powered by generative AI.

Plus, inference (the actual use of the model) is dramatically more efficient than training—more akin to streaming a video than building a data center. If you’re going to make sweeping environmental claims, you better include life cycle assessments and supply chain offsets, not just Reddit-fueled rage.

Otherwise, your ‘objectivity’ is just bias in a tweed jacket.

Mic dropped. Citation included. Model asleep. Try again
[ms1gkuz] (score 1, diepte 7) Oh you said “very harmful” as objectively factual.  I responded to your issues about the environment. Now local AI is ok and you have no issues with that?

So is it bad for the environment only when not run locally?  

Is there any other way you can elaborate or explain like I’m 5 what your issue is with any of this?  

Can you just converse with citations?
[ms1h4rh] (score 1, diepte 7) What is your evidence these are not locally generated images?  I’m positive I can fool you, you’d never know if local, online, handmade. Same software. Less effecient
[ms3wiqj] (score 1, diepte 7) 🧪 Technical Innovations for Sustainable AI
	•	Sprout Framework: Researchers have developed “Sprout,” a framework that reduces carbon emissions during large language model inference by over 40% without compromising output quality. It utilizes “generation directives” to optimize the generation process . ￼
	•	CodeCarbon Tool: This open-source tool enables developers to monitor and manage the carbon footprint of their AI applications, promoting more sustainable development practices .

⸻

🏛️ Policy and Regulatory Measures
	•	Artificial Intelligence Environmental Impacts Act of 2024: Introduced in the U.S. Senate, this bill mandates environmental impact assessments for AI technologies, emphasizing transparency and accountability in AI development . ￼
	•	Biden’s Executive Order on AI Data Centers: In early 2025, President Biden signed an order to enhance energy resources for AI data centers, requiring developers to ensure sufficient clean power generation and mitigate impacts on electricity prices . ￼

⸻

🌱 Corporate and Industry Initiatives
	•	WEKA’s Sustainable AI Initiative: WEKA launched a program focusing on reducing the environmental impact of AI workloads through efficient data management and storage solutions . ￼
	•	Phia App: Co-founded by climate activist Sophia Kianni, Phia is a browser extension that promotes sustainable shopping by suggesting secondhand options, aiming to reduce the environmental footprint of consumer purchases . ￼

⸻

🌍 Community and Research Efforts
	•	Earth Friendly Computation: Led by Keolu Fox, this initiative integrates Indigenous knowledge with sustainable technologies to develop decentralized, renewable-powered data centers, aiming to reduce AI’s environmental impact . ￼
	•	Yale’s Research on AI’s Environmental Impacts: Yale researchers highlight AI’s potential to enhance energy efficiency and environmental monitoring, suggesting that AI can support sustainability when applied thoughtfully .


I skimmed but didn’t see discussion on this legislation.  https://www.congress.gov/bill/118th-congress/senate-bill/3732/text

Or this. https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2025/01/14/statement-by-president-biden-on-the-executive-order-on-advancing-u-s-leadership-in-artificial-intelligence-infrastructure/

It’s initiating cleaner power generation going forward.  But don’t believe me, I’m just refuting your assertion, simply not enough evidence AND it’s actively being worked on. 

Can you articulate your argument or just giving me a link?
[mrunl5o] (score 1, diepte 0) Not what you’re looking for, but maybe generic sandals paired with an ankle brace? If they’re the same color they could be made to look like the same piece, or maybe even sewn or velcroed together?
[mrv0if5] (score 1, diepte 0) Any chance you can link to those orthopedic kids’ sandals in your first pic? I can probably fit into them
[ms1hlus] (score 1, diepte 1) https://princepard.net/products/acy96h5f
[mrv5avk] (score 1, diepte 0) I can laser cut leather.
[ms4ryft] (score 1, diepte 1 OP) I did also
[ms4wnlc] (score 1, diepte 2) Damn. I did see similar asks. I’m talking to 4th shift China factory that makes them.
[ms3xtj3] (score 1, diepte 0) God did not want a machine designing sandals, that task is for manual slave labor for those we disagree with. Jesus would be a beefy GPU if AI was the coming of our Lurd.

Jokes aside I know some wackos and saw these are made in China. Which means reproduction and possibly small runs for bigger sizes. 

I’m talking to them about it and licence or royalty or small drop. I can get it published in fashion and a cessibilty areas and get attention for fancy fun shoes that don’t hurt. 

I’m betting they made larger sizes or could. 

Some of my peeps can get whatever just send a picture. 

If it exists I’ll find it. If not reproduce it. They probably ripped off America. 

No patent…
[mrspcg5] (score 0, diepte 3) AFO Foot & Ankle Brace for Adults

My ChatGPT said you can try to see if the largest child size would fit. I'm assuming it won't hence you posting here and asked what options are available for flare ups, ankle brace and adult sizes.

It recommended a separate ankle brace that you can pair up with sandals. And encouraged going to the proper professional to ensure the pieces you choose fit together properly. 

Perhaps try breaking it up into 2 different products you can use together like it suggested? A Google search of the afo ankle brace it mentioned shows a variety of products that might work and can be used with your choice of sandals.
[mru3whg] (score 0, diepte 0) Great post, minus the AI use.
[ms0wlk7] (score 0, diepte 6) Whataboutism. 

I did not declare AI as inherently harmful. Generative AI can be performed locally for all the purposes you listed. That is not what is being done with this post. 

Give [this](https://mit-genai.pubpub.org/pub/8ulgrckc/release/2) a read. 

Mic dropped? Okay, lol.
[mrvb2dv] (score -1, diepte 5) exactly, you are able to help without the use of AI. have you seen the damage its doing? the giant cooling centres? the stolen art?
[mrvayu1] (score -1, diepte 4) disagree ? i also have chronic pain but i dont use it as an excuse to use such a damaging piece of software
[mrvs3o0] (score -1, diepte 4) No, my opinion was objective. Generative AI is very harmful to the environment
[mrsk0yb] (score -2, diepte 1 OP) I generated the images through an art ai app, but I've used every possible search term on Google to find anything out there. As for Cobblers, I know theoretically that there must be some still in existence but all I've ever come across is shoe repair cobblers and not any that actually build custom shoes. I suspect that I'd have to have "old money" connections to find those types of artisans who only go by word of mouth and cannot be found through a Google search. I suspect there's actually not many people out there, especially in North America, left in the trade.
[mrskdv9] (score -2, diepte 2 OP) Plus, the images generated just look like Roman style sandals which don't actually have ankle bracing...my designs are with the assumption that they have metal or plastic reinforcement inside the ankle straps
[mrthaft] (score -3, diepte 2) and im sure you can describe what you need without further wrecking the planet
[mrvbyq1] (score -3, diepte 2) No? The post itself is detailed and informative. The AI images were not needed
[mrsiyh9] (score -8, diepte 0) Have you asked the AI for products like you had it generate an image of?

You can also research if a custom shoe maker would be able to help you. Will probably be expensive for a custom shoe but shoemakers are still a thing.

=== THREAD yamnus ===
SUBREDDIT: r/ChronicPain
DATUM: 2022-10-22  SCORE: 23  REACTIES: 46
TITEL: Heel not "heeling"
POST (source_id=post):
About nine weeks ago my very large puppy dragged me off a curb. She broke my heel in three places, and it's excruciating. My Dr won't even consider prescription meds and said I should just take Tylenol )you know, the great healer of broken bones. I'm icing, heating, staying off it it, but it's not getting better. The first image is my broken hell on the left, and an intact heel on the right. The single image is of my ankle as it was Wednesday. To say it aches would be an understatement. It ACHES. I can't sleep, can't eat much, due to the pain. Have any of you gone through this? What made the difference for you? 
Mfd[https://imgur.com/a/eijOhsL](https://imgur.com/a/eijOhsL)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[itbsvhy] (score 27, diepte 0) Best advise is to go to a different doctor.  

What kind of doctor are you seeing right now? Is this a primary care doctor saying just take Tylenol for a broken heel? If so, you really should see an orthopedic surgeon.  If it’s already a surgeon you’re seeing that’s telling you that, they are a bad doctor (or they have a prejudice against you, it happens more than you would think) - you need to see a different surgeon who is willing to treat you.

Denial of pain medication after a weight-bearing broken bone is a clear signal they have no intention of treating you otherwise either.  You could need surgery! This doctor is going to neglect you until it becomes a permanent problem.  I would get a second or even third opinion.
[itbvffn] (score 22, diepte 2) Ok, so I can tell you that surgeon is probably not going to help you at all: no pain medication, no surgery (which you could need, it could be a torn tendon or something too), nothing whatsoever is likely. They are basically telling you to fuck off, but they don’t have the balls to actually say it.

So go to another surgeon.  There is no rule that says you can’t get another opinion.  Don’t talk much about the first guy when you see the second. Let the second guy analyze it himself.  If the second guys asks what the first guy said you just tell him “the first guy didn’t think anything is wrong, but I am still having severe pain so I disagree”.  Try not to even mention pain medication if it’s avoidable, but do emphasize you are still in pain.  Mention you can’t take NSAIDs, mention that Tylenol is not controlling the pain, but then don’t escalate it any further, let them realize you may need pain medication while they figure out what’s wrong. 

If it’s still hurting, something is still wrong.  It may be just the bone and nothing can be done, but if that’s the case, a reasonable doctor would give you a small amount of pain relievers in the meantime.  It could be something need to be actually *fixed* though, and that’s what I think your focus should be.

I’ve been doing this shit for 9 years now after breaking my femur: doctors neglecting me, denying surgeries I needed, denying medications, the whole 9-yards - to the point it nearly killed me.  I can spot bullshit from a doc right away these days, and that doc is bullshitting you.
[itbtha0] (score 12, diepte 1 OP) It's an orthopedist. He won't even have a conversation about pain management except to say to take Tylenol. I have a condition where I can't take NSAIDS.
[itdfcvn] (score 9, diepte 0) It took me three months of absolutely no weight bearing and two additional of weight only on the toes to get over my heel break.  The pain returns with each barometric pressure change.  It’s been almost thirty years
[itccoi6] (score 7, diepte 3 OP) Thank you for this suggestion. It's been 8 (9??) weeks since the fall, and the ER told me it was a fracture and was fine. It still couldn't bear weight, so I went to the orthopedist and that's where he was like "It's really badly broken." I went back this week and the X-ray still shows it broken. I would have expected some improvement by this point, but no. He said everything is in place so I won't need surgery, but he seemed completely unsympathetic about it still being broken and little improvement after 8 weeks. I'm so exhausted from all of it.
[itct6wi] (score 7, diepte 2) Unbelievable, I don't get it. Severe pain is severe pain, which is why I don't understand the bizarre "anti-opiate" stance of your area. I'm so sorry.
[itbrr1v] (score 6, diepte 0) This infuriates me!! You have broken, damaged bones and tylenol is a shite treatment. I know it's nearly impossible with what we go through with getting any help at all but I feel that reaching out to your hospitals orthopedic department and explaining the situation and asking them to help in any way they can is warranted.  I know that with the pain contracts some of us are on getting meds from a different provider is banned or deeply discouraged but possibly seeing someone and asking if they can try to work with your team is worth it. If that isn't an option maybe try to write a letter and include scans to the higher ups in your clinic/hospital system or possibly insurance company, therapist, or even social work and ask if with the debilitating injury something can be done at least temporarily to help you get by while healing.

Best of luck to you dear.
[itcnga3] (score 6, diepte 0) I'm beyond gobsmacked. You're in terrible pain, your heel is not healing and your idiot of a physician refuses to give you suitable pain medications. Do you have a GP who could/would prescribe the proper opioids you so obviously need until you can find another orthopedic doctor? Or, what about going to an acute care walk-in clinic for relief? Just to get something to hold you over for the immediate future?
[itcxxlq] (score 6, diepte 3 OP) So many people abused them, which means the people who need them can't get them. My PCP has a "red screen" for people who should not be prescribed opiates, and I'm on it. Apparently when I injured my back 5 years ago the Dr prescribed opiates, so now I can't get them from anyone in that practice. I don't even try. It's humiliating, really, to see the red screen whenever I go in for disparate reasons. Most of the time I don't even need pain meds, but they still get the red screen.
[itd9514] (score 5, diepte 1) Exactly! This should be illegal and criminalized for Dr’s to act this way!
[itccys8] (score 4, diepte 1 OP) Thank you for your reply. Unfortunately, because of a digestive condition, I can't take NSAIDS. If I do, my stomach will bleed and it's awful (I tried one ibuprofen once and was sick for days). So yeah, Tylenol is it. 😣
[itcpm1w] (score 4, diepte 1 OP) None of the clinics or Doctors around here will prescribe anything. When I left the ER, she wrote me a scrip for 20 tramadol and said not to expect anything more. No one else in my medical sphere will even consider anything else. We are in a really tight area where Drs are afraid to prescribe.
[itd1e6u] (score 4, diepte 5 OP) Thank you. I'm about as far away as you can get (Southern California), but I appreciate the offer.
[itcy72m] (score 4, diepte 1) Walk in clinics around here won't give pain meds other than ibuprofen under any circumstances, ever.
[itcyrbf] (score 4, diepte 0) My mom was 89 years old when she broke her hip. Surgeon messed up the surgery so she's been in chronic pain ever since. After fighting for 4 years, she finally got Norco, when she went on hospice. That was the only way we could get real pain meds for her.
[itd1bco] (score 4, diepte 1 OP) Your poor mom. And Norco, one of the weakest opiates out there. Ugh
[itfdekq] (score 4, diepte 6) If your walking on it, it won't heal properly and will take longer that usual.
[itczz6i] (score 3, diepte 4) Again, I'm so sorry you're in such a horrific situation and can't stand the fact that you're in such agony. If you're anywhere near SW Florida, feel free to DM me. I have an excellent PM physician who's part of a large orthopedic practice. These are medical professionals who take the treatment of pain not just seriously, but properly. (hugs)
[itdfa6c] (score 3, diepte 0) Can you take CBD? I have chronic pain and I have been pushed to using this to ease my pain.
[itdv2f2] (score 3, diepte 1 OP) My ortho told me I could avoid surgery if I didn't walk for a couple of weeks. I laughed. I'm a mom of three, a wife, homeowner, employee, etc. As much as I try to stay off it, it's impossible not to walk. Did you break your heel in the same spot? I have no idea how I managed to break THAT bone, where I did.
[itebgug] (score 3, diepte 3 OP) Even the description of your injury gives me the chills. How awful for you.
[itece51] (score 3, diepte 4) Only took 3 months to get diagnosed, doctor claimed X-rays were clear…they were not.  Those 3 months made the break expand.  While not fun it was not the worst pain or treatment
[ited68x] (score 3, diepte 2) JFC. In the UK, you can buy a pack of 32 8mg/500mg cocodamol (codeine/acetaminophen) OTC after a short chat with a pharmacist. Ephedrine/pseudoephedrine aren’t available on their own (unless you buy online) but they’re in a lot of cold/flu medicines that you can buy right off the shelf in the local shop/pharmacy anyway. 

I’d be terrified to live in the US with my chronic pain/health issues. A broken heel is no joke and they’re treating it like your bog standard sprain.
[itey05y] (score 3, diepte 3 OP) Now I want to move to the UK. I hate the policies here and how afraid doctors are to prescribe anything beyond Tylenol or NSAIDS. I hear you're taking applications for Prime Minister, so maybe I'll throw my hat in the ring. I used to be able to manage 200 high schoolers on a daily basis; how much worse could parliament be?? 😉
[itemx9y] (score 2, diepte 2) Yeah, forget this doctor, you need a different doctor ASAP.
[itexm8y] (score 2, diepte 7 OP) It is legal and available, but I can't stand the smell or taste. Plus I have small kids I'm responsible for, so I can't be too out of it and not be able to care for them.
[itdkq6l] (score 2, diepte 1) Try Santa Cruz medicinals website , you can get a 5,00mg bottle of CBD for around $70-80 iirc. Also I found that I needed like 100mg in a single dose to be effective at all, that’s why I recommend that source.
[itecop4] (score 2, diepte 5 OP) I went to the ER and she told me it was fractured. No, it was a giant-ass break in the bone. My issue is it's not showing improvement. After eight/nine weeks I'd think it wouldn't still be broken so badly.
[itdzl9j] (score 2, diepte 0) My only suggestion my friend is to demand a second opinion.
[ite909k] (score 2, diepte 0) Seek another opinion. Get a referral to a pain specialist if you need to. Is it not possible to buy cocodamol OTC in CA? 

I’m on a buprenorphine patch after being on 60mg of codeine every 6hrs as needed from ages 16-26. That fight was astronomical, but I’m lucky to have a pain mgmt clinic in the UK. Even still, I get treated like an addict when I present pain as a symptom…even if it’s because I’m tachycardic or broke a bone 😂
[itebugm] (score 2, diepte 1 OP) Codeine is so seriously monitored here, it's near impossible to get. I wish we had a system where you could buy a limited amount, like they do with ephedrine here. It's behind the counter at the pharmacy but you can get it without a prescription. It's the cough/decongestant that really works, but some people used it to make meth so now we have to show ID to get it and it's tracked.
[iteuybu] (score 2, diepte 0) I had my ankle reconstruction surgery 15 weeks ago (Achilles tear, ligament tears, tendon tears, bone spurs, and calcifications on the heel). I was given 30 norco right away and 10 days later another 30. Plus 90 muscle relaxers with refills.
    
I had to have a revision surgery 2 weeks ago. I got another 30 norco and more refills on the muscle relaxer. 
    
Your doctor needs fired. Any good provider knows that you heel quicker if your body is able to relax and be out of pain.
[itf2kog] (score 2, diepte 0) Find a different doctor.
[itgkh7l] (score 1, diepte 2) Well it is technically malpractice, but it’s impossible to prosecute in almost every case. It’s sucks. It’s discrimination; denial of care because of personal prejudice, but no one who can do anything about it cares.
[itc4klr] (score 1, diepte 0) If your doctor won't prescribe stronger painkillers, try combining Tylenol and Ibuprofen or Naproxen. Acetaminophen (Tylenol) works differently as a painkiller than ibuprofen/naproxen (which are NSAIDs) so you can take them at the same time. (I have fibromyalgia and I do this all the time.) HOWEVER you have to be careful with other medications like cold medications which often include one or the other so you can't take them together. Also be mindful of the [dosing limits as expressed in this chart](https://www.getreliefresponsibly.ca/use-pain-medicine-responsibly/adult-dosing-charts). 

The summary: MAX 4000mg daily of Tylenol, MAX 1500mg daily of NSAIDs. My doctor keeps me on 1000mg daily of naproxen (500 in the morning, 500 at night) and 3300mg daily of acetaminophen (1000mg/2 extra strength tablets in the morning, 1000mg/2 extra strength tablets at lunch, 1300mg/2 slow release (arthritis) tablets before bed.). If you're going to take NSAIDs, it's always best to take them with food as they are hard on the stomach. 

Keep in mind, **I am not a doctor**. I am a person with chronic pain and over-the-counter painkillers comprise a part of my pain reduction regimen. Please consult your doctor or a pharmacist, especially if you are on other medication that might conflict!
[iteo2fk] (score 1, diepte 6) What about marijuana?  Google says it's legal in California even for recreational use, so you wouldn't have to even get a prescription.  Obviously that won't fix the broken bone, but it might help with the pain, as lot of chronic pain suffers get significant pain relief from it.  Never tried it myself and I'm not a doctor and so can't say whether it might interact with any other medications you might be taking, but I say it's worth at least considering.
[itga5gw] (score 1, diepte 8) That's too bad.  It's my understanding that not all types of marijuana make you feel high though. I imagine you could ask at the dispensary what the different types are and how they tend to affect people.  I get hating the smell and taste, but might it be worth putting up with the bad taste and smell for a few minutes if it reduces the terrible pain in your foot?  

Regardless, I hope you're able to find a new doctor who will give you proper treatment really soon.  I'll say a prayer for you.
[itcq0pm] (score 1, diepte 0) Ugh, I had a broken foot for 4 years - my orthopedic surgeon also didn't prescribe anything. I did crutches for 8 months straight, a knee scooter for over a year, air boot on and off for a few years. 

I ended up pairing up with my GP for better pain killers. 

Good luck, I hope yours resolves sooner than mine! 

(PS, my pro tip if you have an air cast, try and wear a slightly elevated heel on the other foot, it really helped my hips from the constant misalignment).
[itcy5vp] (score 1, diepte 1 OP) Funny you say that about the misalignment. My sister told me about a thing you can put in the shoe of the other foot to prevent pain on the other side of my body. My hips and knees hurt just from lurching due to the height differential.
[itd1rd8] (score 1, diepte 2) I hope you recover soon 💙

4 years later now, I'm having weird hip problems on the foot affected side. They can't seem to figure out exactly what's wrong, and no one will say it's related, but I can't help but think it is. I was in a boot for over a year a half cumulative, and the scooter was very rough on my upper leg. I'm only 32 and feel like I live in a 80 year old body. 

Take care of yourself, and don't be afraid to stick up for yourself. Be stern! I know it's hard, it took me years to get even remotely better at it... I still struggle but our bodies are precious and only replaceable to a very small extent. There's a lot of great advice in this sub, and lots of support.
[ite9moi] (score 1, diepte 2) I dropped down from a jacked up jeep type vehicle.  The step down was about 5’.  I wedged my foot in between two rocks.  Bad part was this was on the job, my boss wanted impressive pictures for his online auto sales.  The break was almost dead center at the rear of my heel.
[itfu4sx] (score 1, diepte 6) It does not take much pressure to keep that break from healing.  Maybe you could rent one of those kneel devices that you can roll around one footed and still have at least one hand free for the kids.  Doctors put people in casts to stop us from using or twisting the broken area, knowing that time is the only thing that will work.  Take some anti inflammatorys.
[itdhptx] (score 1, diepte 0) Is this your regular doctor or is this a podiatrist or orthopedist. If you're not seeing a podiatrist or an orthopedist my suggestion would be to ask for consult ASAP.
[itdurqe] (score 1, diepte 1 OP) Orthopedist.
[itere93] (score 1, diepte 1) This. I get that drs want to stem prescription drug abuse, but they're driving people with real pain issues to drug dealers. The people who have chronic pain aren't usually the ones abusing. It's people who get access to the drugs like family, guests, roommates, and theft. Please don't ask for a source, I saw it years ago on a program about drs who hate that their patients are in pain.

=== THREAD tg6rkm ===
SUBREDDIT: r/ChronicPain
DATUM: 2022-03-17  SCORE: 0  REACTIES: 45
TITEL: I am a 21-year-old female uk who after nearly dying is on 50 mg of fentanyl an hour for a year now and foreseeable future for foot and toe and leg pain... need answers
POST (source_id=post):
I was in the ICU for 2 weeks sedated in a coma, had a heart attack, colon removed liver failed kidney failed brain damage, 6 pint transfusion and in-hospital a month in total and lots of other horrible stuff

curious if you can help me

I want to know why my foot is like this if it will get better, also your opinion on the pain relief

&#x200B;

doctors or just fellow chronic pain sufferers

&#x200B;

thank you :)

oh and if you want to use the comments to show off or patronise me because im a woman and 21 or you want to call me names or attempt to bully me (all of which i have endured since putting up this post) then dont bother commenting, but if you want to answer me kindly and get a kind thank you back just don't be a dickhead or a bully which a surprising amount of people in this chronic pain page have been. i have a zero tolerance policy for bullshit and cruelty and bullying.

alot of you are very angry and not used to being told no. please grow up before you think i need grown adult middle age strangers calling me a bitch in my messages. k? cool thanks.

 your unkind words mean nothing to me xxxxxxx

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i104wxv] (score 29, diepte 0) Try to get used to writing out 50mcg/hr for your dose. Its not being picky and it will save you from a lot of looks like you dont know what youre talking about. Nobody expects you to develop a medical degree along with an illness, but you will develop something like one about your condition and what you say and how you say it will matter how  your medical providers listen to you.

Its impossible for anyone in here to know about your prognosis, I'd bet even your docs arent really sure about how full your recovery will be at the moment, but the body is amazingly resilient given enough time. You have been through a great deal, maybe too much to expect a complete recovery but that doesnt mean you cant enjoy your life and have the things that everyone else has. A lot of it is attitude. Be a fighter and advocate for yourself, even when nobody else will. 

50mcg/hr (micrograms per hour) of fentanyl is a pretty healthy dose of pain medication. But everyone and every situation is different. There may be better drug choices or combinations that will give you better relief, even if the "literature" says a drug is weaker than what youre taking. There are 5 main types of opioid receptors in the nervous system that makes these kinds of drugs effective against pain. Each drug like to work mostly on one or two of these receptors, so drug to drug you can have a wide variety of effects. Dose plays a role too, but not as much as you might think. Its more a matter of the right medicine for the job.

I wish I could tell you more about what your future holds, but nobody has a crystal ball. The best you can get are odds and so much depends on how much damage was done. It can take a while just to sort all that out and it doesnt take your specific condition in to account, just other similar cases. Very few people are just average, some do better, some worse. You still get out of recovery what you put in to it, so keep fighting even when it gets so very hard and frustrating. Its a process and it takes as long as it takes. Best of luck...
[i10ac53] (score 18, diepte 2) What the fuck kind of ungrateful behavior is this? Their answer isn't shitty, yours is. What happened to you is truly awful, but you're in a forum with tons of people who struggles with chronic pain, having gone through something awful and being in pain is not unique to just you here.
[i1067ye] (score 15, diepte 2) Ok, fuck it. Give up. Thats what you want to hear? I hope that makes you happy now....
[i108cz8] (score 15, diepte 2) Your best bet is talking to your doctors who know the details of your specific case- there’s not much to go on here in terms of details, and with the level of trauma you’ve gone through it seems to be beyond our level of knowledge to be able to give you the answers you need. 

What Old-Goat said wasn’t shitty, it’s the truth, and parts were quite supportive. You’ve gone through a lot but that doesn’t give you a free pass to be rude to someone trying to offer advice you’ve asked for. 

For now, I’d advise giving your body a chance to recover a bit more, rest a bit more, then slowly but steadily work with your doctors and specialists to find ways to reduce your pain and build your strength up, and talk to them about what they suspect. Every body is different and responds differently to trauma, and it may be that they aren’t certain right now why you’re getting pain, but hopefully with some time they can give you the answers you are looking for.
[i10d6zp] (score 15, diepte 0) What's wrong with your attitude though. People genuinely reaching out and you shut them down rudely. So what if someone doesn't have all the answers you need? Why would you expect people online to have them all anyway? Let people care without being mean about it and move on
[i10dm4a] (score 12, diepte 2) Wow old glad answered your questions and was honest and open about no one knowing your prognosis and your fentanyl dose being significant.

What have your doctors said about your foot pain? Without knowing more as to why they think you have it I don’t think anyone can say how long it may or may not last. I woke up from a surgery with crps and it’s not gone away at all in four years but then someone I know in a similar situation to yours went away within a couple months. So the answer really is could go away tomorrow or may stay forever but likely somewhere in between. 

You should be nicer to people trying to help you - you have been through a lot but that doesn’t give you a free pass to be a jerk to someone who took the time to type a lengthy and honest reply.
[i106gl0] (score 11, diepte 4) My pleasure...
[i10djor] (score 11, diepte 4) Everyone here is pain. That doesn't allow us to be rude with each other. Shame on you for this childish behaviour.
[i115d91] (score 6, diepte 5) You are by far one of my favorites to get a response from!! *hugs*  you are awesome!!
[i10mjk3] (score 6, diepte 0) Most people in this forum are going to save any help or answers they could give for someone who isn’t treating people like a twat.
[i110kqb] (score 5, diepte 5) You are an immature person plain and simple. Your 21 and think the world owes everything to you. We all suffer in our own ways some more then others. But we all suffer. You sound like a bad person. Whatever happened to you happened no one can predict the outcome most of us are still in pain years and years later. #Old-Goat is someone you shouldn't be a prick too. This person knows more then most doctors and is very well educated in chronic pain. Read his posts. If this person is giving me advice I'm listening. You come to a community then disrespect people trying to help. The advice everyone here gave you was solid. Also you went against one or the most knowledgeable people in this forum. Don't post here if you don't want to hear the truth or looking for answers you only want to hear.
[i4340yy] (score 4, diepte 2) Plenty of them were perfectly respectful. The problem often rested with you, at least, in the comments I read.
[i4333jk] (score 4, diepte 2) This sub is full of the most supportive and understanding people on Reddit. And everyone is overwhelmingly downvoting every comment you make because you’re being a bitch for no reason.  I don’t need to look in the mirror; I’m not the dumbfuck asshole coming to a sub to ask for answers and treating everyone who attempts to give you kind words like shit.  I imagine your real life is just as miserable as your Reddit presence.  Hope you Illness clears up. I would hate to have chronic pain AND be a chronic asshole ✌🏼
[i118ay3] (score 3, diepte 6) Thanks, I appreciate that a lot....
[i12j81p] (score 2, diepte 1) I love your advice about learning the medical lingo!  I did some pre med Latin terminology stuff for extra credit in high school.  My first son was 6 weeks early and had several issues for years after. The ability to understand the medical staff made a huge difference with how much time they would talk to us.

Knowledge is power
[i10jypu] (score 2, diepte 0) We aren’t doctors here and don’t know the particulars of your case. You need to ask these questions when you see your doctor next. No one here is qualified to answer your questions.
[i433924] (score 1, diepte 6 OP) his reply had no helpful advice at alland he spoke to me like shit im not going to not stand up for my self, my age has nothing to do with anything and ts very pathetic that your using that because i disagree with you. grow up. i am so far from a bad person its actaullylaughable how much you are trying to assume about me. i wasnt given any truth. you wouldnt belive what happend to me and so because of this you need to wind your neck in. you dont now me, you are a childish, but hurt person who disagrees with my opinions and so is trying to bullshit things and assumtions about me and it wont work, you made me laugh xxx trust me at 21 im more mature and have been through more pain and traume than you could even imagine
[i432sqc] (score 1, diepte 5 OP) no, his reply was toxic and i can call that out as i wont be treated like that. its very sad that you think i am in the wrong, you need to look at your behaviour and treatment of peole , i wont ever let anyone tal to me like that, and calling me childish because im 21 is a very transparent thing to do babe x shame on you hun x
[i43248y] (score 1, diepte 3 OP) yes it does, better than your toxic advice.
[i434duf] (score 1, diepte 3 OP) i know thats what i am doing,  and it was shitty, he was patronising and rude and i dont need to thank him for that just ebcause im 21.  he is giving bad and dangerouse advice and i have never let anyone patrnise me . im not starting now. how dare u pretend that me calling someone out for eng rude to me is getting a free pass for rude ness after nearly dying on an operating table how dare you think i would think that means  can be rude, dont patronse me. you dont now me. he was rude so i told him so. dont assume thigns. ill be as rude as i like to old men who think they can speak to people like that. disgusting. you need a long hard look in the miror.  since your so blatently unaware of how to treat people exscuse me if i ignore your advice. x
[i4741gz] (score 1, diepte 4) I’m not trying to be rude or patronising so I apologise if I come across as so. I’m aware I don’t know you, but at the same time you don’t know me and the situations I have gone through or the person I am, so please don’t assume things about me in the same way you don’t want me to assume things about you. This is intended as a kind and supportive group and we just want to offer help but it seems we don’t have what you’re looking for and as a result you may have taken some comments the wrong way.


I’ve found people commenting in this group are genuinely trying to be supportive- sometimes tone and intention don’t always translate as intended, but that’s a risk that you take when you interact online rather than in person. 


I’m glad you are working with your doctors and I hope they are getting you the support you need, and that in term can help you come to terms with the trauma you’ve gone through. It’s tough being young and dealing with chronic pain (I’m not much older than you from what you’ve shared) and it sucks seeing life continuing on whilst you’re sat back trying to figure out the pain and your best way forward. It’s tough- I do honestly wish the best for you, nobody should have to go through these situations that each of us in the group are facing, yours sounds awful, and I do hope that you managed to get the advice you were searching for.
[i432jcp] (score 1, diepte 3 OP) yeah i know theres a chance it could go away or not , i think i need surgery. and he was not trying to help me he was sying toxic disgusting things and i dont need to put up with it just because his reply was long. i wont be spoken to like that. 

&#x200B;

you should reconsider how you speak to people and so should he
[i433s9j] (score 1, diepte 1 OP) any one who was being kind and helpful was treated the same back, anyone who was trying to patronise me because im 21 was told to get fucked, and rightly so. im not going to thank people for writing online even if its unhelpful or unind. i dont exspect all the answers. i exspect respect but i guess thats too much to as from a bunch of americans
[i10jndt] (score 1, diepte 0) Ask your doctor lots of questions. What is the medication doing? How can I make the most of it? How long will this be necessary? What is the expected outcome? When should pain subside? 

Act like you want to be an expert on your condition who works *with* the doctors, as opposed to just being subject to their wished.
[i431yi2] (score 1, diepte 1 OP) yeah, i think i need surgery, my house mates a doctor and said that i need to speak to a cardiac surgeon, but thanks for your advice anway its good advice
[i431sfm] (score 1, diepte 1 OP) i am doing that but if i want peoples opinions i can ask for them, if you have no answers why answer me?
[i431o39] (score 1, diepte 1 OP) good for them, and i havent treated anyone like a twat i have just stood up for myself and corrected peopels biast, if you have issues with that id look in the mirror
[i435zbx] (score 1, diepte 3 OP) clearly it isnt. i dont care if people agree with me standing up for my self or not. n nice call someone a bitch and try and act like that dosnt make you the one in the wrong. you really do need to take a long look in the miror you are clearly very angry inside, but yeah keep the name calling comming it just shows exsacly who you are, and what your like, anyone who treated me with kindness got the same back, anyone who spoke to me like shit got the same back. maybe you should ask your self why you agree with those people, what does that mae you. im actually very happy and standing up for my self is what i will always do, i couldnt care less what it makes me look like to people like you. its chronic so it wont but dont worry at least im not trying to bully someone younger than me on reddit. and  i wouldnt now what thats like as i have chronic pain but i get great pankillers so im not in pain so thats pretty great and i am the kindest person you will ever meet so if you are te one calling names i think its clear who the giant asshole is, you btw incase you couldnt grasp my simple explination xoxoxox
[i437jrk] (score 1, diepte 4) Lol. Should’ve thrown a tldr in there because I genuinely don’t give two shits what you have to say any longer and definitely am not reading that garbage.  I regret commenting in the first place. ✌🏼✌🏼
[i43c4wt] (score 1, diepte 4) Lol. Yes. So jealous. Was literally the first medication my PM Dr put me on, before hydrocodone even. They dish out fentanyl patches to people they don’t know yet if they can trust with pills ;) I asked to be switched, and was.  I’m very happy with oxy.
[i11ft5i] (score 1, diepte 0) Can I ask what you almost died of and what is the cause for your leg pain. That may make a difference in treatment options. Before disability I was an ICU RN.
 I suffer from chronic migraine/ cluster headaches. Not the same but advocating and trial and error with different meds has finally made a bit of difference for my migraines. 
Fentanyl will be difficult to get off of if you are able.
[i431itv] (score 1, diepte 1 OP) fentanly is a life saver and has allowed me to live a normal pain free life so i dont really care about the negatives, and i nearly died of paracetamol posoning to the point where i was 5 minutes away from death on an operating table, this cause cardivasular problems as well as evey part of my body failing which has cause m foot to not get enpugh blood and thus the pain
[i43153r] (score 1, diepte 1 OP) are you stupid? why on earth would i do that i would be n agony
[i437x33] (score 1, diepte 0 OP) thank you to the eope who were kind and repectful and treated me with respect. i appriciate your rpelys. and a big fat fuck you to the people who have been calling me names and messaging me abuse. if your rude exspect rudeness back. its simple as that. 

i am going to see a cardiac sergon as my house mate is a doctor and has said thats what i should do. if anyone ver wants a chat on a bad day weather its pain or just life im bed bound so im here for a chat if ou need a little encouragemnt. being chronicly ill and disabled overnight at 21 has made me stand up for my self more but also made me kinder. you can turn crule or kind after the worst pain imaginebale mentally and physically and as i have been through other traumes before this also have gotten to the point where the pain has made me kinder everyday. 

&#x200B;

if you are kind and respectful, feel free to ask anything or message me if you just want to rant. 

&#x200B;

i dont need your opinions in reply to this if you are going to be negative, i have been called enough names by strangers already. 

&#x200B;

im going to make a newpost when i get an update on my foot. 

i don't need your opinions in reply to this if you are going to be negative, i have been called enough names by strangers already. on bad day whether it's pain or just life im bed bound so im here for a chat if you need a little encouragement. being chronically ill and disabled overnight at 21 has made me stand up for myself more but also made me kinder. you can turn cruel or kind after the worst pain imaginable mentally and physically and as i have been through other traumas before this also has gotten to the point where the pain has made me kinder every day. 

so be kind or go away. 

bella xxx
[i438a8q] (score 1, diepte 0 OP) to the unkind disrespectful people, your unkind words mean nothing to me at all xxxxx
[i433cmq] (score 0, diepte 5 OP) good good x
[i438fzm] (score 0, diepte 5 OP) good good babe fuck off then, i wish you had never comented in the first place too! please go away thats exsactly what i want thank goodness!! xxxx
[i434ygs] (score -1, diepte 3 OP) i am not ungrateful at all, there was nothing to be greatful for just a man wanking into my coments, i didnt ask for his patronsising rudeness and wont stand for it. his answer was very shitty and just because i stood up for my self im shityy? you need to tae a long look in the miror. i never said it was unique to me, he dosnt get to treatme like that just because he has pain too. old men dont get to man splain my life to me. thanks tho chrissie xoxoxoxox
[i4357tt] (score -1, diepte 3 OP) no they were not, anyone who was kind and respectful got the same back, just because you think its ok to patronse people because they are 21 dosnt make it ok. the problem did not rest with me. i ased for help not given eole a stage to show off, get a grip. grow up
[i43ebn9] (score -1, diepte 5 OP) iv been on codine, oxy, tramadol, and morphine all in pill form ;) i asked to switch to patches because i have severe pain which is clearly worse than yours as mine needed more than oxy, keep telling your self that, you seem super happy and deffintaly not a massive weirdo who called strangers names on the internet, i pitty you sweetheart, now could you fuck off like you threatened to before? its all i want, to never think about you ever again, so fuck off babe ;) :)))))) xxxxx
[i106drh] (score -24, diepte 3 OP) no i didnt want to hear anything from you because like i said you have no answers to my questions. go away please x
(1 reacties met lagere score weggelaten)

