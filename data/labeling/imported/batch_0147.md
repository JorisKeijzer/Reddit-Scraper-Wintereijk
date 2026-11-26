# Label-batch batch_0147

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
Schrijf het resultaat naar `batch_0147.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: w0szjf, 323aq6, 3jbfzz).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD w0szjf ===
SUBREDDIT: r/skeptic
DATUM: 2022-07-16  SCORE: 325  REACTIES: 76
TITEL: I'm tired of being targeted by woo because of my aesthetics and hobbies.
POST (source_id=post):
I'm a 30 year old white woman with a degree in Geology who goes rockhounding and writes sci-fi/fantasy fiction. I'm constantly bombarded with targeted advertisements and assumptions that I'm into bullshit, and it's really getting on my nerves.

The rockhounding scene is especially bad with crystal healing, because many otherwise reasonable collectors and sellers have to accommodate these idiots to make a sale. Gem and Mineral shows are full of crystal wizards who run around the booths with their hands held out, trying to detect "auras" and "energy" from the specimens so they can charge them in the sun and stick them up their vagoo. You can't have a normal conversation with these people because they get offended by even the most innocuous scientific fact. I've gotten dirty looks for advising people not to leave certain minerals in direct sunlight because the color will fade (amethyst specifically), or pointing out when a specimen has been dyed or heat treated to resemble a different gemstone (most store-bought citrine is actually heat-treated amethyst because naturally occurring citrine is more expensive), or even just advising people not to store different crystals in the same pouch because the harder one will scratch the softer one.

The frustrating thing is that I resemble these people. I love the boho/crystalcore aesthetic and wear things like wire-wrapped crystal jewelry and chakra bracelets. So when I walk up to a vendor, they immediately get ready to sell me a selenite massage wand when I actually want to inquire about the pyritized salt hopper casts they pulled out of the ground when rerouting the local highway. I get talked down to by a lot of vendors until they realize I have a scientific background, and then sometimes they get excited or at least change their tone. Of course, a lot of vendors are grifers or even believe their own grift, which is equally as frustrating when they actually do have some nice minerals and I have to debate the morality of shopping from them. 

Thanks to my hobbies and demographic, my targeted algorithms are absolutely polluted with bullshit. I google a lot of mythology, nomenclature, and folklore when I do research for my book, because I like to make references to historic beliefs and be as accurate as possible. I also like nature and being environmentally conscious, as people probably should. This means my top search results are always anti-vax, anti-"toxin", alt-medicine spiritual crap. It's awful when I want to buy a product like a skin cream or dietary supplement, and it takes me hours to find one with active ingredients that actually function as advertised. 

Yeah, maybe I could just not use skin creams and dietary supplements, and maybe I should go to mineral shows wearing my mud-stained jeans and rock pun t-shirts. But I don't want to. I hate that the things I like are so deeply associated with woo and idiocy, so much that I can't be comfortable in my own interests and hobbies.

I was really angry last night because I was trying to shop online for a copper bangle bracelet. I inherited an antique one from a relative and it's getting worn out enough that I want to retire it and replace it with a new one. Unfortunately, every single copper bracelet I liked the look of was one of those "magnetic healing" bullshit bracelets with magnets on the inside. I don't want a magnetic bracelet! I want a regular copper bracelet that doesn't pretend to do anything but be a bracelet because I like the look and color of it! But now, thanks to lies and grift, people don't make copper bracelets anymore without marketing them as a medical device. And I'm stuck having to go through so much effort to find something I like without supporting beliefs I don't, I'm not sure I'll even want it anymore.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iggcwly] (score 101, diepte 0) That's also pervasive in the modern yarn-spinning community: if they aren't "witches" they're Christian extremists. You have to be picky to find a group of reasonable people.
[igh501i] (score 57, diepte 0) I'm into martial arts and military stuff (I'm in the reserves, so it's not weird LARPer shit... It's weird LARPer shit I get paid for)... I'm also very left wing, proper left wing. But if I use a fresh profile I get all sorts of annoying right wing shit.

I feel your pain.
[iggkd60] (score 52, diepte 0) And to think that Snake Oil peddlers used to be tossed in jail or chased out of town. Now, we celebrate them for their 'entrepreneurial spirit'. Our society needs a serious enema.
[iggui3n] (score 48, diepte 0) I gave up on bikram yoga a while ago, cos I couldn't handle the sheer amount of bullshit unproven claims the teachers proclaim with literally every posture. "This one is particularly good for your spleen!" Really? It is? Or is that just what the sex-pest guru "inventor" said, and you're simply parroting it verbatim because he was such a freak that any script deviation would no longer be bikram and is thus verboten?
[iggd8vu] (score 47, diepte 0) Omg. I feel this op. I love rockhounding, but the constant supernatural bs gets tiring. 

Though I will say it was interesting to see a lapidarist be able to I'd the source country of various gems on sight, and then also discuss "Lemurian singing quartz". It was surreal.
[igh0b6l] (score 27, diepte 0) You may never truly be able to get away from these advertisements, but there's a couple of tricks you can use if you're looking for something specific and you don't want all of your search results to be biased.

If you haven't tried these, try the brave search engine, or the duck duck go search engine. search.brave.com and duckduckgo.com respectively.

These explicitly claim not to track your previous searches or use ads driven by personalized profiles.

And I know the incognito mode or private browsing feature of chrome and Firefox respectively are jokingly refered to look up porn, they can also be used to look up anything you want where your browsing history will not be taken into account. You should not be seeing personalized ads when you use incognito or private browsing. Though some advertising profiles have been able to track things like your IP address. So it may not be perfect.

But if you are looking for something specific and the ads are getting in the way, maybe try one of those search engines inside of incognito mode? Hopefully your search results can be more neutral.

Good luck!
[igh479i] (score 24, diepte 0) LOL. Waves "hi" from genomics and searching for disease issues, which makes google think I'm a hypochondriac.

And I review crank books, so I get really shitty book recommendations now.
[ighgn67] (score 21, diepte 0) Yeah, as someone who's PhD thesis was primarily focused on X-ray crystallography, it's very difficult to tell someone I "study crystals" without making it sound like I'm some woo-woo quartz-carrying shaman type. Especially hard nowadays that I literally do study actual "healing crystals"! (In the sense that I study the crystal structures of pharmaceutical drugs lol.)
[igip4n1] (score 19, diepte 1) I wonder if this is part of a larger trend of extremists deciding to hawk their beliefs everywhere. I just reported a bunch of comments on /r/rccars because the commenters were going on about fringe political beliefs.
[ighf866] (score 19, diepte 1) Yeah, they can take their crap as shove it up their... Wait, Gwyneth Paltrow already did.
[igglhl2] (score 19, diepte 0) They’re not rocks Marie. They’re minerals.
[iggy7hl] (score 19, diepte 0) For searches try Duck Duck Go. It searches Google for you and shields you from the targeted personalization of search results. May provide better results for you.
[ighatee] (score 15, diepte 0) In the 1970s, Rock and Mineral Shows would tour the country and come to any decent sized city at least one time each year. I miss those.

Try [Etsy](https://www.etsy.com/c/jewelry/bracelets/cuff-bracelets?explicit=1&ref=catcard-1198-456056024) > Jewelry > Bracelets > Cuff Bracelets, or whatever style. I’m not saying you won’t find some new age whackanoodle stuff there but the majority of it will be skillfully hand crafted pieces made by jewelers instead of hucksters just adding another item to their cavalcade of crap. 

As a magician I can’t search for “buy magic wand” without being buried in psychic crystal wands, fairy princess toys, Harry Potter and the like. If want a nice hardwood wand with brass tips for my cups and balls routine, I need to go straight to sites that sell magician’s equipment.
[ighk04x] (score 14, diepte 0) Ah yes, I love our society.  You can look serious, or feminine.  My wife bitches about this all the time.  If she gets on her no nonsense pants and a sensible shirt people treat her completely differently than if she puts on something cute.  

>I was really angry last night because I was trying to shop online for a   
copper bangle bracelet. I inherited an antique one from a relative and   
it's getting worn out enough that I want to retire it and replace it   
with a new one. Unfortunately, every single copper bracelet I liked the   
look of was one of those "magnetic healing" bullshit bracelets with   
magnets on the inside. 

Jesus christ I just tried searching this and you're not joking.  Apparently copper has superpowers now beyond 'conducts electricity with little resistance.'
[igghkmg] (score 12, diepte 0) Have you read the Broken Earth trilogy?
[igizdja] (score 11, diepte 1) How do you do, me?

I'm a social democrat tradesman that manages to sneak leftist messaging into our chats. 

"Boss makes a dollar while I make a dime, and that's why I shit on company time."
[ighj2pp] (score 11, diepte 0) Hopefully this little story will make you feel slightly better. I love and follow the band Phish. One of the things Phish is known for is the “lot scene”. Basically a ton of vendors in the parking lot of the venue selling pretty much anything. Definitely a lot of woo crystal folks. 

My good friend worked for a vet tech, and after some surgeries to remove some bladder stones from a dog, he asked if he could keep some.

So on the Phish lot-He walks up to a crystal woo seller and says he has some struvite. The dude looks at it and eventually takes it for a trade. 

I like to think that dog bladder stone is still floating around the Phish community to this day.
[igjh4r4] (score 10, diepte 3) The usual, Hunter Biden's laptop is proof that the global elite want... <INSERT CRAZY HERE>
[igh2obl] (score 10, diepte 0) You might be able to mitigate some of the directed advertising by turning off **Ad personalization** for Google services:

https://support.google.com/ads/answer/2662856

At least that should help for Google searches.
[igh3p2n] (score 9, diepte 3) Better, I'd say. Dune didn't know when to reach the end of its story; Broken Earth in contrast built to an *incredibly* satisfying and thought-provoking climax.
[igj5wzy] (score 9, diepte 1) Oh yeah, "feel the toxins leaving your body."

Am I supposed to pee my pants or something?
[igh1lxy] (score 9, diepte 1) Also, adblocking plugins like ublock origin and Social Fixer (for Facebook, specifically) are great. I can't imagine browsing without them.
[igh2doj] (score 9, diepte 0) We would be best friends irl. Rock hounding and scifi are amazeballs
[iggt4qg] (score 8, diepte 2) It is staggering. It's up there with Dune.
[iggjefn] (score 8, diepte 0) I choose my battles carefully. I have a background in pharmacy and have a lot of contact with yoga-related woo. As long as my friends are blowing a ton of money on herbs and supplements, I don’t push back too hard. But when they start skirting medical care is when I step in. Take the antibiotics and drink raspberry leaf tea.
[iggr903] (score 8, diepte 0) > I should go to mineral shows wearing my mud-stained jeans and rock pun t-shirts.

Marry me.
[igj9dab] (score 7, diepte 1) I watched a few videos on YouTube about the Russian invasion of Ukraine when it started, and YouTube decided next I should watch 2A stuff of a guy telling me I totally need a gun to defend myself and is my god-given right to get one, and a video from a dude showing me how I can modify a legal AR to make it “more fun” (ie. Illegal, felony) in California.

It was crazy to experience that monetized radicalization funnel first person. Any gun/military stuff on YouTube leads to nut jobs really, really quickly. 

My feed is only now recovering from that, after a while of ignoring/hiding gun videos.
[ighf1sv] (score 7, diepte 0) I have a witchy aesthetic and love horror genre shows/films, music.  I'm also a skeptic and into science as well as rocks and gems and minerals. I just try to respect and be kind, and ignore a lot of shit. I make a lot of art that fits this aesthetic, and I make zero claims about anything being "magic" but I'm happy if something I made makes someone else happy and I don't care what they use it for so long as it's not to harm anyone.
[igjhd0q] (score 6, diepte 4) Okay, thank god it isn’t something specific to the RC car world like “ethics in scale model racing journalism.“
[iggijdx] (score 6, diepte 1 OP) I have not, I'll have to look it up.
[iggxzo8] (score 6, diepte 0) I feel like you could have replaced first and second with non-feminine woman into feminism and this could have all been written by me. I don’t think I’m a man or”butch”or any variation of it just because I don’t care to wear my hair long and whatever girly clothes but I still am interested in feminism and getting rid of gender without denying biology and social aspects that constrain and affect it. If you don’t fit the box and you are”an annoying in-betweener”best be prepared to feel frustrated for possibly the rest of your life. Also I have no expertise close to yours but I empathise-I like tarot, astrology, crystals and all that but I take it as trivia. Even when I explain to people that I simply like the looks of crystals and appreciate the art of tarot decks(while at most using them as ink blot test on myself rather than whatever else it was supposed to be taken as)and like many writers enjoy inspiring aspects of astrology or finding new phrases for already established beliefs about myself and others(rather than taking it as prophecy)…people still want to take it as me being full on superstitious. Why do people do this? I’m thinking maybe it gives them some feeling of superiority, whether they’re aware of it or not. To certain degree it’s normal to have prejudices that make life easier but on the other hand a lot of this stereotyping is so easily avoidable if people just bothered to listen or ask questions. It certainly makes life more full filling imo
[igj24hc] (score 5, diepte 1) You should team up with the guys who do Christian movie reviews (God Awful Movies).
[igjdvfv] (score 5, diepte 2) I look forward to the day when someone adequately documents the process by which the internet turned into a radicalization engine.

I suspect that it’s a natural consequence of the fact that already radicalized people part with their money quickly.
[ighk471] (score 5, diepte 0) Hank Green called out Google for something similar.  It would be nice if he could see your post.
[iggiupf] (score 4, diepte 2) You definitely should because it's perfect for you!
[igjdlu2] (score 3, diepte 2) Jesus tell us, wtf kinds of crazy beliefs are the ducking RC CARS people chicken hawking?!?
[igh7iyf] (score 3, diepte 1) It's not really a new problem, it's just the ones people didnt like that got fucked
[ighgi82] (score 3, diepte 1) Preferably not a coffee enema.
[ighjzbj] (score 3, diepte 1) Searching in an Incognito window (Chrome) or Private Browsing (FireFox) will not use your saved profile - so you can buy skin cream without woo.  I agree she shouldn't have to do this.
[igic0p0] (score 3, diepte 1) I think DDG searches Bing, not Google
[igkhyso] (score 2, diepte 2) It's so frustrating. They're making people fitter but also making many of them dumber.
[igi29n0] (score 2, diepte 1) I recommended this to someone else in the subreddit the other day, but if you haven't read it, check out The Castle of Crossed Destinies / The Tavern of Crossed Destinies by Italo Calvino, two novellas (usually published together) about a group of travelers unknown to each other who find themselves at the titular castle or tavern after having been struck mute in the forest and have to tell their tales using tarot cards. The stories are the protagonist's interpretations of the stories. Each novella uses a different well-known tarot deck. From the sound of things, I think you'd enjoy it.
[igr1ota] (score 2, diepte 1) Duckduck go is now also showing cracks: https://www.searchenginejournal.com/duckduckgo-microsoft-trackers/452006/
[igs6orx] (score 2, diepte 2) Hmmm, that was the mobile browser and only going to LinkedIn and ms sites.

But dang, might be on a bag path. Tsk tsk
[igk6jht] (score 2, diepte 3) Right, it’s easier to get someone spending/clicking if they are scared, angered or otherwise emotionally overwhelmed. 

Remember, “there are no atheists in the trenches”.
[igjefmd] (score 2, diepte 1) Okay I feel like there’s no reason to expect a reliable, secular market for “magic wands.”
[ighqht8] (score 2, diepte 0) You might want to check out r/privacy. The way you feel about rocks, they feel about not being tracked
[ighsm9y] (score 2, diepte 0) Have you tried searching for a Viking copper bracelet? There are quite a few of them online and they don't generally claim to have healing properties because the "twist" is that they're Viking, not that they magnetise your blood or something.
[igipn7g] (score 2, diepte 1) I had the exact same experience on facebook, I get that the group I was in was full of desperate people but the gullibility was off the charts. along with a lot of anti western medicine shit.

If any of the stuff worked, the group would not exist but the group collectively lacks the self awareness to realize that.
[igi9n25] (score 2, diepte 0) Interested in science? - prepare for aliens, ufo and interdimensional travel content spam.

Like music and music theory? - endless ads about new groundbreaking methods to learn to play any instrument you wish without actually practicing them. 

Love technology? - constant demands to participate in crowdfunding of random fictitious bullshit-tech companies. Or just cryptocoin spam.

Yeah, seems like a common pattern not just related to your interests.
[igic0f5] (score 2, diepte 0) Sounds like someone needs their chakras realigned. Yooperlite perhaps?
[igiehxe] (score 2, diepte 0) I make my own beard oil. Which involves using essential oils for their scents. But, unfortunately this tends to cause my targeted ads to fill up with bullshit.
[igik2i1] (score 2, diepte 0) Yup, I can relate as a 30-something woman that likes yoga and natural things (food, cosmetics, clothing from natural fibres). I got into knitting and even there you get a lot of completely unnecessary esotheric bullshit when you seek out minimally processed fibres to knit with.
[igiop4n] (score 2, diepte 0) I somewhat feel your pain. I dont suffer exactly the same problem but I can give a couple instances where it feels difficult to avoid woo.

Salt. Should be simple right? the number of products that are full of woo is absurd. I'm just trying to fill a salt grinder, not cure cancer.

Essential oils. I just wanted something that smelled nice to put in a humidifier. Yeah those get really silly.

Energy drinks. I just want some good tasting caffeine in a variety of flavors. I dont need pixie dusting, super creatine etc.

The woo does not target me exactly, but its hard to avoid.
(22 reacties met lagere score weggelaten)

=== THREAD 323aq6 ===
SUBREDDIT: r/askscience
DATUM: 2015-04-10  SCORE: 207  REACTIES: 48
TITEL: Would it be possible to protect space explorers from high energy radiation by generating an (electro)magnetic field around the spaceship, just like earth's magnetic field protects us?
POST (source_id=post):
If it's possible, what/how much energy would it require?

Or is it much easier to coat the spaceship in like, 10 feet of lead/concrete?

Edit: I'm mostly wondering this in relation to different "Humans to Mars" projects.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cq7hchw] (score 50, diepte 0) It wouldn't be able to protect you from gamma radiation. Deflecting charged particles away from you would also cause high energy photons to be directed at you due to synchrotron radiation.
[cq7hl6k] (score 43, diepte 2) A bunch of atmosphere between you and the gamma rays. You are exposed to more radiation by flying in an airplane because of this.
[cq7hjr7] (score 21, diepte 0) Most radiation in space is particle radiation. The proper sheilding is water, not lead. 10 feet of plastic might also work... Or just 21 cm which is still very heavy. 

Magnetic shielding for charged particles is possible but difficult. You need an oddly shaped ship and you also can't expose the crew to the magnetic field.
[cq7i6h8] (score 20, diepte 2) Basically, for blocking this type of radiation you want low atomic masses. Water and plastic are both full of hydrogen. 

Hydrogen is resistant to being made radioactive by the impinging radiation.
[cq7hk2p] (score 16, diepte 1 OP) I understand that gamma rays and high-energy photons are the same thing. Well, how does the earth protect us from those?
[cq7nodo] (score 15, diepte 4) I don't see a reason why ice wouldn't work. 

Currently one of the plans is that it would actually consist of *food* (inside the pressure hull but outside the radiation shelter/sleeping quarters) in shrink-wrapped blocks. As the astronauts ate the food, they would replace the space it took up with shrink-wrapped... shit., as both of those things are good radiation shielding.
[cq7on49] (score 15, diepte 6) There is no reason why the food wouldn't be safe, in general. In the majority of cases, things that get irradiated don't become radioactive (they do if they are hit with neutron radiation.)
[cq7tokm] (score 15, diepte 7) To expand a bit, the issue with most radiation isn't the energy component (that's what happens in radiation burns), it's the DNA damage. We don't integrate the DNA of the food we eat into our own, so it wouldn't really matter if we ate something with DNA damage. In fact, a lot of digestion is breaking down DNA into constituent amino acids that we can repurpose  for our own needs.
[cq7ixih] (score 14, diepte 3) The engineering problem of using water as a radiation shield is very interesting to me. It would be fun to play with the idea of creating an insulating layer of water around a ships hull...orrrr you could just create a layer around the living area of organic cargo.
[cq84jrw] (score 13, diepte 4) I believe the issue is that you're mixing up atmosphere with em radiation. To block a spaceship from the gamma rays you'd need a physical shell, like lead, or water, or something.
[cq7mnj4] (score 10, diepte 2) It wouldn't *attract* photons, but when you accelerate a charged particle, photons are produced. Since to deflect something you need to apply an acceleration to it, and these particles would be moving at very high velocities, you would produce high energy photons by deflecting them.
[cq7rtss] (score 10, diepte 6) The danger of radiation is that it will break up living dna, increasing rate of dna repair/replacement, which increases the risk of copying errors, which leads to cancer.  As an analogy, think of them as little bullets doing damage to your body.  If they are slowed or stopped by the food, they won't be able to hurt you the same way.
[cq7hs8v] (score 8, diepte 1 OP) Why is water/plastic better?
[cq7mfn8] (score 6, diepte 3) Would ice work as well as water, or would the regular structure of the ice make it less effective than the essentially random structure of the water?
[cq7q2ry] (score 5, diepte 1) There is very little known problems with exposing crews to magnetic fields. NASA has a relatively low "safe" upper limit which is almost certainly overly conservative. Magnetic shielding is an active area of research and does have potential uses and benefits.
[cq8hhyj] (score 4, diepte 8) Well, breaking DNA into its constituent nucleic acids, as DNA isn't made of amino acids, but the rest is spot on.
[cq7mmbc] (score 4, diepte 0) This is why when you watch/read some SciFi they describe the ships as mushroom shaped. The water acts as both shielding and a reaction mass. You have to remember when designing a space ship every kilogram matters. I don't think it would matter ice/water in terms of shielding but water expands when frozen needing more space for storage, larger ship, more reaction mass for same mission.
[cq7ve6s] (score 3, diepte 0) First off, Earth's magnetic field doesn't make a big difference in the radiation dose that we receive from space. It's the *atmosphere* that gives us the most significant protection. In fact the ISS is very deep inside Earth's magnetic field and still their radiation dose from cosmic rays is so high that astronauts are not kept there for more than 6 months.

http://upload.wikimedia.org/wikipedia/commons/e/ef/PIA17601-Comparisons-RadiationExposure-MarsTrip-20131209.png

In that graph you see 1/4 of the radiation of deep space, but only 1/2 of this is due to the magnetic field. The other 1/2 is thanks to Earth's *solid body*.

So if you were in deep space protected by a magnetic field equivalent to that of Earth, you'd get 1/2 of the average dose, which is still too high to go to Mars.

Another problem is that Earth's magnetic field is not very strong, but HUGE. It extends several tens of km above the surface. We won't be able to make such a big thing around a spacecraft without making it very strong at the center.

For that purpose, the effects on human health of a very strong magnetic field are not well known. This paper gives an overview:

https://engineering.dartmouth.edu/~d76205x/research/Shielding/docs/Parker_06.pdf

> If it's possible, what/how much energy would it require?

The biggest concern would not be the energy, but the magnetic field intensity. Also, this could only be achieved with superconductors, and keeping them cool enough for this doesn't sound feasible in space.

> Or is it much easier to coat the spaceship in like, 10 feet of lead/concrete?

Lead and concrete are good shields *proportionally to their size*. But in space we're much more concerned about mass, so it'd be much better to use water or polymers.

Anyway, even with those light materials, a radiation shield thick enough to provide a meaningful attenuation of the radiation dose would still be way too massive for any realistic budget. Consider the launch costs of around 5000 $/kg - one liter of water in space costs more than [the world's most expensive champagne](http://www.forbes.com/sites/nickpassmore/2014/12/06/the-worlds-most-expensive-champagnes/).

The radiation issue is still an open problem in space exploration.
[cq83j5r] (score 2, diepte 3) So how big would the magnetic field need to be?
[cq95bqj] (score 2, diepte 5) This. The basic problem is, that you cant influence photons with an EM field. The only way to stop them is to put stuff between them and yourself. The more (and denser) stuff the better. Air consists of gasses which have quite a low density. But since the atmosphere is quite big (compared to a plate of lead) it protects us very well.
[cq8ip4g] (score 2, diepte 4) Brems is usually used to refer to the effect of charged particles entering matter. This effect falls under the general term of synchrotron radiation which I stated in my original comment and applies to all accelerating charged particles.
[cq8iqbq] (score 2, diepte 4) Brems refers to the synchrotron radiation when particles enter matter. The general term is synchrotron radiation.
[cq7ojpa] (score 2, diepte 5) Wait a second, how is the food safe to eat if it is soaking up all that radiation?
[cq7vl7h] (score 2, diepte 1) The problem with space radiation is that it's just not the solar wind, which is how our earth's very weak magnetic field deflects the protons in the solar wind. It's also cosmic rays and a lot of micrometeorites, which our atmosphere deals with. There're also UV and X-rays from the sun and other more distant objects can also generate a huge amount of radiation.

So, no, a magnetic field around the space craft will not protect the crew from most of the radiation, esp. if they are well away from the sun.

for that, simple mass is needed, about 2 kg./sq. cm. which roughly approximates the earth's atmospheric mass, saving us from most radiation, such as cosmic rays. Still, most won't protect us from that.

IN a very long space trip, the velocities would likely be so intense, that the 1 proton/cu. m. of space would hit the craft with very high velocity, or rather, the craft would hit the protons/mass with very high velocity and create a lot of damage.

the way round that is to fire an ionizing laser forward, thus ionizing the incipient atoms and such, and deflecting those charged ions  with a very large, supermagnetic field from SC magnets. That would deflect such mass. & if they wanted to refuel with hydrogen, even collect it, as in a Bussard ramjet, which picks up fuel from space, fuses that to hydrogen (by some still unknown efficient means) and thus propels itself ever faster from the fuel as protons are picked up from space.

Still, it wouldn't block cosmic rays, and so that heavy shielding of 2 kg./sq. cm. would have to be used for journeys over a few months.
[cq803a3] (score 2, diepte 1 OP) On Mars they can burrow down under the surface though, if they have the tools.
[cq831fx] (score 2, diepte 2) To add to my other comment, since you said you're interested in comparing projects of humans on Mars, you might appreciate these:

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3797711/

http://www.researchgate.net/profile/Marco_Durante/publication/261063768_SpaceradiationprotectionDestinationMars/links/02e7e5331eaa52750c000000.pdf

The second provides some additional info on active shielding (magnetic fields).
[cq7tkx0] (score 1, diepte 3) Are you referring to [Bremsstrahlung](http://en.wikipedia.org/wiki/Bremsstrahlung)?
[cq89iel] (score 1, diepte 3) http://en.wikipedia.org/wiki/Bremsstrahlung
[cq7qxxb] (score 1, diepte 1) Also neutral atoms, neutrons and any other chargeless particle traveling at high speeds, which while not as significant as the charged particles is still significant enough during months of time in space.
[cq8im04] (score 1, diepte 9) Thanks, knew I was missing something.
[cq8e0mg] (score 1, diepte 4) Ice is less dense, so it would be a bit less effective because of that.
[cq7thwi] (score 1, diepte 4) Light elements are more likely to slow down neutrons (whereas heavy elements will tend to bounce them around without absorbing any of their energy) until they are slow enough to be absorbed.

The downside is that this process often produces secondary photon radiation (which light elements are not very good at impeding), so water shielding would probably require a second, high-density layer of shielding to deal with this.
[cq7srxf] (score 1, diepte 0) Would it be possible to electrically charge the hull of the spaceship that would prevent the radiation from penetrating?
I'm guessing that by doing so you would turn the ship into a giant magnet whose field would divert the radiation like earth.
But then, could humans survive inside that magnetic field? Or does that create a dead-zone inside the ship that would keep them save?
[cq83cv1] (score 1, diepte 1) Take a look at the paper I linked in my other comment, your question is pretty much answered in it: https://engineering.dartmouth.edu/~d76205x/research/Shielding/docs/Parker_06.pdf

Basically, cosmic rays have so much energy that you'd need an overwhelmingly strong electric field. If you do this then you will start attracting electrons from the solar wind, concentrating them in a small area and causing them to emit secondary radiation. In the end it'd only make things worse.
[cq8b0m8] (score 1, diepte 1) >astronauts are not kept there for more than 6 months.

Scott Kelly just went up a couple weeks ago and will be staying for 1 year.
[cq7zcoh] (score 1, diepte 0) It's difficult to protect from high energy photons, as in gamma rays.  Photons are not affected by an electric or magnetic field.

However, we do have the technology to protect against charged particle bombardment, such as energetic protons and electrons.  The ISS and some low-Earth-orbit satellites have what is known as a 'plasma contactor', which sprays a cloud of ionized gas around the satellite.  This cloud creates enough of an electric field to deflect incoming charged particles and thus prevent an electrical charge from accumulating on the craft.

A plasma contactor probably wouldn't help much with a mission to Mars, though.  The barrage of high-energy photons are the real danger to deep space astronauts.  But we still might use a plasma contactor on a Mars mission to deflect the solar wind, if there are sensitive instruments on the spaceship hull.
[cq89069] (score 1, diepte 0) As others have already said, it's not the EM field that really matters.

However, if you really wanted one, I would guess a superconductor where you pump a lot of amps into would cost very little energy to maintain (assuming we have high-temp superconductors, or they are well insulated or something).

Basically, we're pretty screwed for space.

=== THREAD 3jbfzz ===
SUBREDDIT: r/askscience
DATUM: 2015-09-02  SCORE: 43  REACTIES: 28
TITEL: The Ehrenfest Paradox?
POST (source_id=post):
https://en.wikipedia.org/wiki/Ehrenfest_paradox

The faster an object goes, the more it seems to contract relative to a stationary observer. 

The Ehrenfest paradox:

1. Places the observer at the center of a rotating disc (Or let's say the observer is suspended above the center of the disc by helicopter - so he does not contact the disc)
2. Places measuring rulers along the perimeter of the disc. 
3. Draws a measuring line on the surface of the disc that leads from the observer's feet to the perimeter (The line marks the radius of the disc). 
4. Spins the disc up

The observer should see the rulers along the perimeter of the disc contract, while the radius seems to stay the same length.

The Ehrenfest paradox points out that this is a contradiction. The only way the perimeter of the disc could contract without the radius changing would be if the perimeter were to break apart. The rulers would have to separate from each other, allowing you to fit more rulers into the gaps created.

I encountered this problem when trying to imagine what a charge "sees" while passing through a loop or coil of wire. It is placed at the center of a seemingly rotating disc of charge (The current carrying conductor). There -IS- some kind of Lorentz contraction taking place, since we know the charge experiences a magnetic force. I'm trying to understand why/how, relativistically, that happens. But I keep encountering this paradox while trying to visualize it.

**Bonus Question #1:** What does the person see if the helicopter flies upward, allowing them tolook down onto the disc?

**Bonus Question #2:** If the person is level with the surface of the disc, does it matter whether the disc is spinning or the person is spinning?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cunwdol] (score 24, diepte 0) The resolution of this paradox, as hinted at in the article you linked, is that rigid bodies do not exist- and relativity precludes them from existing even theoretically. 

Not only is an absolute rigid body not possible- this one often comes up when discussing "why can't you have a light year long rod and poke things with it, thus transferring information faster than light?"- but even a weaker form of rigidity, called [Born rigidity](https://en.wikipedia.org/wiki/Born_rigidity) isn't possible. That is, any real disk, as it is spun up will deform slightly. No matter how strong you make it, you know it has to deform some based on the argument you made here.
[cunwgoq] (score 4, diepte 1 OP) So then what causes a charge to feel the magnetic field of a loop of changing current? I assumed it was relativity. If it is some form of relativity, could you explain what the charge sees when it is at the center of the loop, above the loop, or spinning relative to the loop? This goes back to my original question regarding the spinning disc.
[cuodw1f] (score 4, diepte 2) The standard definition of "rigidity" is that a body will maintain the same shape though movement. It does not apply only to discs, but to anything. To imagine it, if you had a record on a record player and you painted a grid of dots on the record, when you start rotating the record player the dots would stay the same far apart with the same angles between them. 

Of course, lots of things are approximately rigid, and so for a lot of calculations, assuming a rigid body is accurate enough and helps solve problems quickly (so firing a rifled bullet so that it is spinning). Not trying to account for deformation makes the calculation easier and since it doesn't deform much, it is basically correct. 

But when you start talking about things moving really fast, you can start to get some nonsensical answer if you assume absolute rigidity (like the paradox described above). Thus, you start to realize that things are not rigid, they do deform when moved, and if you try to spin something too quickly it will rip apart. And thus for these types of problems, the rigid body approximation no longer works.
[cuotgn0] (score 3, diepte 4) I think you're missing the strength of the statement that's being made here. I'm not saying "don't worry about Ehrenfest's paradox because things will deform and fly apart at high rotation speeds" I'm saying "Ehrenfest's paradox is proof that no body can be a rigid body (and not even locally rigid)." It's not dismissing the paradox, it's looking at the paradox and saying "how is this resolved?" 

And the resolution is that not even local rigidity can exist. That is, the idea of a rigid body is very easy to describe away- as mentioned you can't poke something with a light year long stick instantly. But for a while, people thought that a local rigid body could exist, that is a rigid body where any two points of the object which are in the same inertial frame (traveling with the same, constant velocity) could maintain a constant separation vector. This paradox is proof that not even this type of body can exist. Thus, we're not stating "our technology isn't good enough to make something like this" we're stating "the laws of physics don't allow this."

So it isn't side stepping the question. The answer to this paradox has been worked out- at low speeds and high. It is that any body must deform enough to counteract these relativistic effects. At low speeds, the relativistic effects are so small that you don't measure the deformation (but it's there!) and at high speeds the relativistic effects are great enough that you will have to notice the deformation.
[cuoxp9p] (score 3, diepte 6) Remember that a charge does not experience a magnetic force if it is stationary at the center of the disk. If you think about the direction the charge must move in order to experience the lorentz force you will notice that the symmetry of the problem is broken and the length contraction as seen by the charge is different from what you have posed in this problem...
[cunwkde] (score 2, diepte 1 OP) >plus in reality centrifugal force will make the disc expand anyway.

Right, but this doesn't clear up my confusing regarding the three questions I posed. If my example doesn't work to understand the behavior of a charge near a loop of current, please propose one that does. Dismissing the example while not answering the original questions might give off the impression that the questions are unanswerable or not deserving of an answer.
[cunxzrm] (score 2, diepte 2) Bear in mind you've asked (although your initial post contains no questions about electromagnetism) what seems to be quite a... high-level question in a forum designed mainly to allow somewhat lower level questions be answered by scientists. And then been pretty snippy when people have answered the questions you actually posed in your post.

You'll probably need to poke some of the specialists on the board if you want it answered here, but from a quick Google it seems there is some information that might help solve your problem if you look around a bit more. 

Anyway, it is far beyond my understanding of physics but provided an interesting topic of reading, I didn't even know relativistic electromagnetism existed, so thanks.
[cuo1leb] (score 2, diepte 3) > You can see the loop, it looks the same no matter how fast electrons move around the loop. That's how it looks for a charge too.

How would it "look the same" if any effect involving Lorentz contraction changing the perceived density of charge is involved? I mean, imagine that you have only a few electrons in the loop, say, 10. Then changing their "density" would actually require shrinking the very real, discrete distances between them somehow.
[cuoqtse] (score 2, diepte 3 OP) This is wrong. Relativity explains electromagnetism. But it doesn't explain centrifugal electromagnetism afaik, which was my question.

Also it's irresponsible of you to claim things don't have a cause simply because you don't understand how they work. Do your homework before dissuading people from seeking knowledge in the future.
[cuotvmy] (score 2, diepte 4) You are right. I was wrong. I don't quite understand what you're saying though. 
How would a lone charge be above or below or in the center of a loop. Are you saying you're using a bar magnet to induce a current in a coil of wire, or are you running current through a coil of wire to generate a magnetic field? Either way, you have a coil, and not a loop.
Also, Any real wire you could use to do this would be many many orders of magnitude greater in cross sectional area than a lone electrons cross section, so any force any electron would feel would be forward or backward, not centrifugal/centripetal, kind of like the force you feel while the solar system flies through space. You don't feel the earth moving.
[cuousoq] (score 2, diepte 5 OP) >How would a lone charge be above or below or in the center of a loop.

It's an over simplified, idealized version of what happens when anything with moving current (be it a magnet or a conductor) approaches a coil of wire with current running through it.

>Either way, you have a coil, and not a loop. 

A loop of wire is a coil with 1 "layer". It's the simplest coil you could make. Which is why I used it in my example.

>Also, Any real wire you could use to do this would be many many orders of magnitude greater in cross sectional area than a lone electrons cross section, so any force any electron would feel would be forward or backward, not centrifugal/centripetal

Not sure what you're getting at here. My point was that, if relativity (length contraction) explains why a current carrying conductor creates an electromagnetic field when a charge is external to the wire/loop, how does relativity explain the force a charge feels when it is at the center of the loop (Like standing at the center of a marry go round)?

The answer is found by understanding how a person perceives a rotating disc while standing at its center point. The problem is that this situation is a known paradox. I literally can't imagine how a charge would "see" the perimeter of a rotating disc contract because such a thing seems to break the bounds of Einsteins theory of special relativity.

I've been searching through general relativity to explain this situation, but I haven't found anything that describes this scenario.
[cuo3vom] (score 2, diepte 1) What's the definition of rigidity? And does this apply to discs only?
[cuoti4f] (score 2, diepte 5 OP) Ok, so why does a moving charge at the center of a loop of current experience a magnetic force? The charge is at the center of a rotating loop of current, just like the person stands at the center point of a disc. If relativity plays a role, how does it come into play?
[cunxeal] (score 2, diepte 1 OP) The Ehrenfest paradox is specifically about how length contraction does not apply to objects in rotation when observed from a central reference frame. 

Linking to a page that explains length contraction due to linear motion from an external reference frame does not solve the paradox of length contraction due to rotational motion from a central reference frame .
[cuoa6a2] (score 2, diepte 0) With regards to the disc one question to be asked is "is it actually rotating". By that I mean, can we get the same relative motion (rim to hub) if we leave the disk stationary and just cause the observer at the hub to rotate rapidly? The answer is no because in that case there would be no centrifugal forces at the rim. This indicates that this is not a case of relative motion as is required for relativity.
[cunw3cs] (score 1, diepte 0) This is way beyond me, but bear in mind that Lorentz contraction is something that happens in *special relativity*, which requires inertial frames, which this situation does not have.

If you look at the wiki article, it says that this paradox is one of the reasons Einstein was able to move from special to general relativity. The resolution seems fairly simple to me - it is impossible to synchronise clocks around the edge of a rotating disc, plus in reality centrifugal force will make the disc expand anyway.
[cuomn5o] (score 1, diepte 3) Going back to the light-year long pole idea, if I understand correctly, part of the problem is that it's not intuitive to us. If I have a stick, and I stretch out my arm, the stick moves exactly as my arm does, or at least it "seems" too. As you make this stick bigger and bigger, you begin to see that the stick doesn't move instantly with your arm, and the unfathomably short delay starts to increase. Is that right?
[cuoni56] (score 1, diepte 4) Exactly. A metal rod seems quite rigid, but it doesn't have to be that long before you start seeing it droop. That's one way to see it isn't rigid. But even for a smaller rod what you'll see is that movement propagates through the material at the speed of sound in that material. So, for instance, in metal if you move one end of the rod, that movement will propagate through the rod at over 5000 m/s- which is stupid fast. But if you have a long rod you could notice. Or if you start moving the rod really quickly, then it couldn't bend enough to stay together before the motion propagated and it would shear apart.
[cuos1t8] (score 1, diepte 3 OP) No one's claiming the object won't fly apart at near light speed. It is a thought experiment with ideal variables to understand the exaggerated effect of a similar spinning disc at very low speeds. 

If you know what an ideal disc WOULD look like near light speed, you can begin to understand what it looks like at less drastic speeds (where it would hold together).

Dismissing the thought experiment is like telling Einstein that his crazy "rocket idea" isn't worth thinking about because "rockets can't even go the speed of light!".
[cuojpjj] (score 1, diepte 0) This is already kinda answered. Still. Let's say you've a particle accelerator. You're in the centre. This accelerator takes molecules and spins them up really fast. In fact it takes really long molecules that go all the way around the acclerator and twines them up. 

First let's look at the segments of these really long molecules. From their perspective the distance they're travelling is a bunch shorter than from our view in the center of the disk. We see them going 2*pi*r. We can listen to the frequencies of light emitted by their vibrations. It shows they're relativity shifted. Let's say time is twice as slow on the molecules and they take 1/2 second for them to go around the disk.  They take 1 second to spin around the disk from our perspective. For them its a much tighter route. Space shortened for them because they're in an accelerated frame.

While I don't want to break into Wolfram Alpha and start messing with Shodinger Wave equations in relativistic frames my guess is that the molecules would break their bonds at fairly short intervals because they'd be creeping up on each other.
[cuo9x1f] (score -2, diepte 2) Your question (if I understand it right) is: how does an electric current produce a magnetic field. This question has no answer. Scientists have observed that it DOES produce a magnetic field, but there aren't any explanations as to why. This question is analogous to asking why mass warps spacetime. Noone knows the exact mechanism, but they know that mass does this.
[cunx953] (score -2, diepte 0) I think you might be struggling because you've got cause and effect the wrong way round. The origin of a "magnetic force" is a relativistic effect due to length contractions! Here's a page I just googled that seems to do an all right job explaining it. It takes a linear wire rather than a current, but I'm sure it's not beyond your powers to see how the argument generalises to any shape of coil. 

http://galileo.phys.virginia.edu/classes/252/rel_el_mag.html


Also the clue to bonus question 2 is sort of in the word relativity. As long as they are spinning relative to the disk they will see the same effect.
[cuo19hw] (score -4, diepte 2) You can see the loop, it looks the same no matter how fast electrons move around the loop. That's how it looks for a charge too.

If you or a charge move through to the loop, it's still the same loop.

If you or a charge move across the loop, that's a different story.
[cuo495a] (score -9, diepte 4) Of course expert's idea of Lorentz  contraction differs from layperson's idea of Lorentz contraction, right? As we are laypeople, let's stick to our lay ideas, OK?

It happens to be so that our Lorentz contraction law does not apply in this case. 

If an electron in a particle accelerator in France is accelerated to great speed and another electron in a particle accelerator in Italy is accelerated to great speed, what is the distance of said electrons? 

.  

.  

.  



(Answer: distance is the distance of the particle accelerators)

