# Label-batch batch_0120

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
Schrijf het resultaat naar `batch_0120.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1q4tngd, 1jhcvqp, q7a16u).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1q4tngd ===
SUBREDDIT: r/Military
DATUM: 2026-01-05  SCORE: 211  REACTIES: 70
TITEL: Imperialist idiots like this deserve to return from their wars of aggression feet first.
POST (source_id=post):
honest to God this asshole sounds like a military officer from Imperial Russia in 1902

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nxv3qv8] (score 128, diepte 0) I mean, when you have to preempt someone’s argument by saying don’t mention morality, you know you’re in the wrong you just don’t want it pointed out to you.

Imagine a German soldier saying, “why shouldn’t we just take it?” about Poland.
[nxv2hwk] (score 73, diepte 0) US won’t have to « invade » Greenland, they already have a dozen of military bases there.

They also already have access to any ressources on the island. 

The only major effect of US seizing the land of a NATO ally would be to destroy the alliance. Who would benefit from that again?
[nxv163d] (score 49, diepte 0) Chickenhawks always do...
[nxv6fsp] (score 38, diepte 0) "I will not be accepting Rules Based International Order as answers."

  
you know, the thing America specifically invented and enforced to prevent world war fucking three.
[nxv4asb] (score 36, diepte 0) Downvote me if y'all want, but ngl I think the US needs to get fucking humbled at this point.  
Way too many Americans live in a bubble and think they're superheroes who can just go at it alone.  
The US is just as reliant on its allies as everyone else, the US military can't operate and build or develop its equipment alone, heck even if US '' enemies '' like China cut all trade with the US it'd be a total disaster.  
Now imagine the US loses all support from its actual allies.

 The reason the US is in the position its in as the most powerful country is BECAUSE of its allies not in spite of them.  
The same allies btw who fought and bled for you after 9/11, Denmark had some of the highest casualties and saw some of the bloodiest battles.  
Even non-NATO members came to your defense.

 Americans quite frankly need to stand up for its allies more, it's just sad even how quiet non-MAGA morons are, I feel like I barely if ever hear anything about this.  
When Trump held his speech to congress he said he wants to annex Greenland again and every Republican in the room stood up laughed hysterically and applauded, that's sociopathic and terrifying and should be treated as such.  
Instead it feels like it's a footnote at best.

 When you make Canada and Denmark your enemy it's probably time to accept that yes you're the bad guy.
[nxv5cg9] (score 29, diepte 0) No one loves war more than a coward who wasn’t in one
[nxv69aj] (score 25, diepte 1) I 100% think Trump just looked at a map and legit thinks Greenland is that big and just wants to make the US look bigger on a map.

People circle jerk the US military a lot but the US military has never really gone up against an actual legit modern and professional army in a VERY long time, and most US equipment wouldn't even work on Greenland even in perfect weather.  
If as I hope NATO would actually go and defend Greenland it'd be very bloody and NATO has a lot of members that are specialized in that climate and have equipment specifically built to operate in those conditions.  
That's also not even touching the internal turmoil in the US ( or so I'd hope at least, if Americans just sat by and watched it happen then wow... I'd have nothing but ill wishes at that point. ).

 Underestimating the little guy and the effects of climate is a mistake that has been repeated time and time again and pretty much always ends poorly.
[nxv212w] (score 24, diepte 0) Dumb as dirt. These people are completely unable to put themselves in the other persons shoes. They are incapable of rationalising how they might feel if it was their home, unable to understand that America isn’t the only way to live. He will shout freedom but mean the freedom that he agrees with.
[nxv6t33] (score 23, diepte 2) Denmark would not even fight but say bye to Olympics and the current world order. That shit would isolate US (LiKe wE nEvEr seEn bEfoRe)
[nxvg29n] (score 19, diepte 1) >Imagine a German soldier saying, “why shouldn’t we just take it?” about Poland.

Can we just have the US instead? 

You know, Poland got the short end of the stick a couple times in history, but the US? Maybe it needs the short stick once too at this point.
[nxv5t9b] (score 17, diepte 0) He’s a field grade officer who sucked up to Stuart Scheller on Twitter and now works for Stuart in the OSD office at the pentagon.

He was above the zone for major and was passed over for LTC until this year when he became schellers buddy.

He used to stream under the handle generaldort
[nxvm5tn] (score 15, diepte 3) Never heard of Vietnam or Afghanistan?
[nxvjalp] (score 14, diepte 2) If the U.S was humbled by having their shit kicked in during one of these imperialist wars it’d probably think twice before launching another one
[nxvw9tw] (score 11, diepte 5) "You can't fire me, I quit"
[nxv88s0] (score 11, diepte 1) Oh fucking Christ. Nothing worse than a Major who overestimates his own importance. See SECDEF as another example.
[nxva4w5] (score 8, diepte 3) Hitler attended the Olympics. The only way the Olympics dont happen is if the site gets cratered.

The IOC fucking loves dictatorships and totalitarians regimes, all the better to profit from. FIFA fucking wishes they were on the IOC’s level of corruption and fraud.
[nxvmmv2] (score 8, diepte 4) The withdrawals from those two were essentially on the U.S’s terms though, not because of military defeat
[nxvcgei] (score 8, diepte 0) This dude was openly and explicitly calling GOs dumbasses (using that exact word), by name, while @'ing them and bragging about how he was smarter than them, and Randy George's response was to make sure the Army PCS'd Dort to work direct for Sean Parnell lol
[nxviik6] (score 8, diepte 1 OP) You realize this asshole is talking about invading a peaceful country right?
[nxvimky] (score 7, diepte 2) I think you meant to say SECDUI
[nxv71gg] (score 7, diepte 0) dude sounds like a piece of shit
[nxv6wlu] (score 6, diepte 1) Obviously Putin Xi and Trump have agreed (or Trump has been suckered into) a three way global split 
Deranged demented maniac needs to go
[nxvfkrv] (score 5, diepte 4) True. The only way would be if enough countries and athletes pulled out to make it unwatchable.
[nxvsbtd] (score 5, diepte 4) Hitler in 1936 wasn’t viewed the way he is now. It was 3 years before the war, even before he violated the Munich agreement and took Czechoslovakia. So them hosting the Olympics was crazy but not that crazy it was just another racist country at that point, not full on genociders.
[nxvf621] (score 5, diepte 1) And I'm sure a lot of them said it.
[nxwb4ip] (score 5, diepte 7) To be fair the vast majority of the Vietnamese people supported Ho Chi Min and was democratically elected as their first president (and later prime minister) and he only became 'communist' because the US refused to support him in ousting the French from Vietnam while the Chinese and Russians did agree to giving support. He was considered more a nationalist revolutionary by the OSS during WW2 and aided the allies in fighting the Japanese in Indochina. Had the US supported his goal of Vietnamese self-determination we (the US) probably wouldn't have gotten involved in this "police action".
[nxvncmw] (score 5, diepte 4) It didn't really affect the mainland US at all, plus the economy of the US doesn't suffer from rampant military spending, since that's basically the welfare program now.
[nxvgynw] (score 5, diepte 1) He's a child playing with his toy soldiers.  That's all the troops mean to him.  He's a juvenile, narcissistic pig.
[nxvefal] (score 5, diepte 1) And yet they’re going after Mark Kelly for saying exactly what is written in the UCMJ.
[nxvu3ic] (score 4, diepte 5) From is historical perspective it sure looks like we were defeated pretty handily in Vietnam. Our goal was to stop the spread of communism in SEA and last I checked Vietnam is still ruled by the CPV (Communist Party of Vietnam). The US tucked it's tail between it's legs and left the country. But it was a 'police action' and we were 'advising' the south Vietnamese, so i guess we can't count that as *losing a war* due to a technicality.
[nxveqag] (score 4, diepte 2) Yes, His name is Adam D'Ortana, he was a twice passed over major (therefore unlikely to be promoted to lieutenant colonel) until somehow, COMPLETELY COINCIDENTALLY I AM SURE AND UNRELATED TO HIS NEW JOB AND FRIEND PETE, he was recently promoted to LTC
[nxvdvuc] (score 4, diepte 0) Why do we “need” to take over Greenland for national security when it belongs to a NATO ally?  I do understand it’s strategic significance. 

In a rational world these strategic goals could be achieved diplomatically and with amity between partner nations. 

Unfortunately we no longer live in a rational world.
[nxvh473] (score 3, diepte 4) Have fun going down the rabbit hole and learning that the Olympics is a massive eugenics exercise.
[nxvuixw] (score 3, diepte 3) General Armchair, have you reported this weakness to US military high command?

It seems the Americans are unaware that their airbases are vulnerable to attack!
[nxve8yd] (score 3, diepte 1) There’s one base there, a missile / space base, and around 150 US troops. There are multiple Danish bases, ships and hundreds of Danish troops.
[nxvm5e9] (score 3, diepte 2) Exactly and we don’t want to be like them.
[nxw1s53] (score 3, diepte 3) I agree.
[nxvoaf8] (score 3, diepte 1) Spot on. Even indirect attacks on specific foreign ports would have HUGE impacts on US industry and quality of life.
[nxw4f33] (score 3, diepte 1 OP) People like this need a good ass, kicking to be honest they are so full of themselves much like the German army was at the beginning of World War II. Yet an awful lot of those master race. People wound up fucking pushing daisies up by the end of it.
[nxvtyww] (score 2, diepte 2) >>but the US military has never really gone up against an actual legit modern and professional army

Who else has? Ukraine against Russia? Are we calling a fight between two deteriorating post-Soviet states a fight between two “legit modern and professional” armies?
[nxw88at] (score 2, diepte 6) Won every major battle and still lost the war
[nxvt51v] (score 2, diepte 1) or the US with Texas and Hawaii……
[nxvu56a] (score 2, diepte 2) Hawaii, yes. Texas was a bit more complicated than that.
[nxvj1mr] (score 2, diepte 1) Fox News Chickenhawks.
[nxwe736] (score 2, diepte 3) His proper title is Triple SECDEF!
[nxvmf2z] (score 2, diepte 0) Sounds like a musk bot
[nxvrtf0] (score 2, diepte 0) Reading that tweet was wild. Not caring about "rules-based order" is against the spirit of the Declaration of Independence and Constitution. Not caring about "morality" is against the spirit of the Bible. In that sense, the tweet is very anti-American and anti-Christian. I hope the individual carefully rethinks what they tweeted.
[nxvxeh3] (score 2, diepte 2) Jesus fuck thats the grossest shit ive ever seen and i worked as a paramedic after I got out and had to help find a guys skin after his arm got degloved in a chicken processing plant. I am so glad I am no longer in the Army or had to serve under someone like that.
[nxw2pb6] (score 2, diepte 0) Only do to others what you'd willingly accept from them. 

It's amazing how many life's problems can disappear if you just Actively Try To Not Be An Asshole. 

It really is that easy. Crazy.
[nxvcahg] (score 1, diepte 1) He’s still in?
[nxvem7a] (score 1, diepte 2) Yep
[nxwka7r] (score 1, diepte 1) If it's the same guy, he also used to bang cadets when he taught ROTC at UC Davis... Allegedly.
[nxwpntl] (score 1, diepte 2) I don’t think this dude bangs anyone that’s not an anime waifu
[nxvc7cb] (score 1, diepte 0) Because (you) don't really want to wake up Europe's military industry? Ukraine used to be meh and Russia's supplies were rotten, now Ukraine is sending drones to far regions and Russia is producing in bulk. Because (your) aahhh will be stretched thin between Latin America, Canada,
[nxvdk9k] (score 1, diepte 0) Grunts are grunts for a reason.
[nxvfnqi] (score 1, diepte 0) Very nice, let’s see where that IP address is located.
[nxvhoa2] (score 1, diepte 0) Maybe Denmark would accept a trade say Florida for Greenland. I Think that would be a win for the US.
[nxvk3p0] (score 1, diepte 0) Interestly enough he may be that guy alwas screaming about his second amendments although it’s far more likely he’s not even American.
[nxvnung] (score 1, diepte 0) I bet you he also thought that he was „too tough“ for bootcamp
[nxvso52] (score 1, diepte 0) Looking at that "persons" previous posts, i'm 110% certain they are a cosplayer or a bot. AI portrait with captain bars, claims they are an LTC now. Every post is MAGA talking points and chest thumping aggressive appeal to emotion instead of anything of substance. Persons not an Infantry anything. I was an 11B1P back in the 90's and blue falcon soldiers with that lone-wolf kill everything mindset were the ones we worried about sharing foxholes with because they'd get the rest of us killed.
[nxvvc88] (score 1, diepte 1) https://girlcockx.com/DC_Draino/status/1883900634207752523
[nxw0qso] (score 1, diepte 0) Twitter Imperialists are comical, if they are real people anyway
[nxw1iim] (score 1, diepte 1 OP) Sadly he’s very real an actual serving military officer named Adam D’Ortano.
[nxw5irt] (score 1, diepte 2) Sadly when ignorance and principle are mixed, even a good beating might not start the self to questioning. 

I always fully believed that the average person could do with a little self-doubt now & then. Forgetting to check for rust won't help a bucket hold water.
[nxw5grs] (score 1, diepte 0) *gestures at historical examples* probably not a great idea. I swear these people did not attend schools or read books.
[nxwe4qt] (score 1, diepte 0) Such people usually have seen wars only through Rambo movies at best, and won’t actually participate sticking to comments and shitposting instead
[nxwkg3m] (score 1, diepte 0) Hi Any-Guarantee-128, your post of Imperialist idiots like this deserve to return from their wars of aggression feet first. has been removed because:

Your post has been removed at the discretion of the mods. 



Please contact the mods if you need further assistance
[nxw8a5p] (score 0, diepte 6 OP) Gee that quit a large police department nearly 70,000 cops died /sarc
[nxvtl1l] (score 0, diepte 1) Let’s be realistic hear, if the US decides to take Denmark by force we are not responding militarily. Not in a million years. We probably impose sanctions on them and kick out US troops and that will be the end of NATO, but we are under no circumstances going to fight them. Even if we wanted to, our armed forces are currently a joke, we are in the process of rearming. We RELY on American weapon systems. Our air defense systems are American, our fighter jets and missiles are American, most of our ISR is supported by American satellites. We’ve got no chance.
[nxvn8ym] (score -2, diepte 2) >If as I hope NATO would actually go and defend Greenland it'd be very bloody and NATO has a lot of members that are specialized in that climate and have equipment specifically built to operate in those conditions.


You have become so used to fighting goat herders in the deserts that you forget that an actual war will hit you at home just were you choose to fight.


If it came to it, and in this case it won't, a fight with any near peer adversary will see you hit with financial and trade sanctions, and then when things get kinetic, cyber and physical attacks on your infrastructure and port systems.


Your stealth aircraft are damn near invulnerable in the sky, but many of your airbases are relatively soft targets. 


An opponent wouldn't just fight you in Greenland for instance they would attack behind your lines in Alaska. They would use the political turmoil you have created these last few years to target your NORAD facilities colocated in Canada.
[nxvfgub] (score -8, diepte 0) Let’s just pull the us military from the world to return back home and let all the hand holding stop… of all the countries and let them really see what happens when we are gone. I’m tired of all the big talk from people who think it’s better if we are gone. Let’s straight up leave and let everyone fall to crap… then people will see what they forgot.. how we have securities in places there were none.

=== THREAD 1jhcvqp ===
SUBREDDIT: r/travel
DATUM: 2025-03-22  SCORE: 13  REACTIES: 70
TITEL: Recommendations of good walking shoes with a wide toe box
POST (source_id=post):
I'm planning a trip that will involve a lot of walking. Most athletic shoes cause pain in my toes after walking for a while. My go-to shoes are Skechers Go Walk Joy, because they have a wide toe box. However, I'm between sizes, and the ones that fit the toes best tend to slip in the back. Also, it seems most of the newer Skechers models fit loosely in the heel regardless. Can anyone recommend a reasonably-priced walking shoe that might meet my needs?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mj664en] (score 14, diepte 0) Hoka's are pretty great for walking and not too tight in the toe.
[mj66b9x] (score 13, diepte 0) Keen shoes have a wide toe box - I own several pairs.
[mj6r0kl] (score 10, diepte 0) Altra, Topo, or NB (wide models)
[mj66iua] (score 9, diepte 0) They are ugly but a pair of Brooks running shoes made a huge impact on my knee and back pain from walking

8-9 miles of city walking would do me in but with the Brooks I don’t even feel it

Well worth the money
[mj674nj] (score 9, diepte 1) Second Brooks. Since switching to Brooks ghost I have zero forefoot/toe pain. Ever.
[mj7jx8d] (score 8, diepte 1) I love my Altra trail runners.
[mj6ubi0] (score 8, diepte 0) Altras if you want a thin flexible sole. Keens if you like a thick sturdy sole.
[mj6c5tj] (score 7, diepte 1) Unfortunately I can’t really recommend hokas if you’ve got toe issues and need a wide toe box. I’ve been dealing with a big toe issue for a few years now, and I didn’t realize how restrictive the Hoka toe box was (even the wide size I was wearing) until I switched over to Altra’s. 

I was also getting a lot of blisters with the Hokas that magically went away with the Altra’s, so I don’t think they fit my feet properly from the beginning.
[mj6whaj] (score 7, diepte 0) Topo for wide toe box and a natural arch
[mj68upd] (score 6, diepte 1) Another vote for Brooks. Brooks Glycerin is very cushy and has a wide toe box.
[mj7lnfe] (score 6, diepte 1) Brooks are not ugly lol. They’re the most average looking shoe out there.
[mj7acyj] (score 5, diepte 1) Just did a heap of travel/walking in Hoka Bondi 8s, and they were great.

Important note:  they are available in Wide (me) and X-wide sizes.  This makes *all* the difference.
[mj67ciq] (score 4, diepte 1) Hokas for sure. My feet never hurt when I wear them (on my second pair) and neither do my legs or back. Can’t recommend them enough!
[mj6hxgb] (score 4, diepte 1) this...
[mj6qi40] (score 4, diepte 0) I found that Hokas hurt my feet. I really like the Saucony Triumphs, which can be found in older versions on Amazon at reasonable prices.
[mj7hiyv] (score 4, diepte 1) I second Saucony.
[mj6s469] (score 3, diepte 1) I have wide feet and I’ll also endorse Brooks.  I’ve worn them for quite a few years. My GF recommended I try Hokas but they hurt my back so I’ve gone back to Brooks and am happy.
[mj6di19] (score 3, diepte 0) I have a 4e foot and enjoy new balance. Extra wides.
[mj79hih] (score 3, diepte 0) Extra wide New Balance 860s are the only ones I can wear with insoles without pain (bunion, arthritis in toe)
[mj7a5v7] (score 3, diepte 0) I swear by Altra, but beware they're zero drop so you may need time to get used to them.
[mj7cew7] (score 3, diepte 0) Adidas terrex free hiker 2. Awesome light hiking shoe/boot (high and low model) with a roomy toe box and a clever lacing system that keeps the shoe snug in the back. 


Do try them somewhere before ordering as the sizing seems different from regular Adidas shoes.
[mj7xe7o] (score 3, diepte 0) Someone at REI told me about the heel lock style of lacing and it changed my life. I have wide toes plus bunions and relatively narrow heels. Running shoes are more likely to have the extra hole you need, but I have punched extra holes in other shoes. I wear Brooks Ariel in wide because I overpronate.
[npbjpx8] (score 2, diepte 4) Awesome. I am going to a shoe store Thursday to try things on. Thank so much.
[npe6ik5] (score 2, diepte 5) You're so welcome! If the targhees work for you, stop there. If they're not quite 'it' for you, try some other styles. Once you figure out your size you can order online, free delivery and free returns. Enjoy, and let us know what you end up going with!
[mj997t3] (score 2, diepte 1) Specifically look at brooks 4e wides.  I have wide feet and screwed up big toes and the ghost 16 are great for me as they have added height that allows my custom insoles.
[mj8ag4v] (score 2, diepte 1) Seconding Topos. Good secure heel and mid foot with plenty of space in the toe box for splay. The atomos are super cushy in the insole too
[mj77xbq] (score 2, diepte 0) On (or On Cloud)…so comfy.
[mj79nyl] (score 2, diepte 0) New Balance 10 v12.  It's has to be V12 because the later versions have a more narrow toe box

I walked all over London and Edinburgh in them. At least 5 miles a day.
[mj88awm] (score 2, diepte 1 OP) Too true. I have a pair of Tree Skippers, most comfortable shoes I own. But I got the infamous hole in the toe.
[mj8ckyf] (score 2, diepte 2) Haha yeah my 2 skippers also got a hole in the same spot so won't buy them again. My 2 dashers have been going through all the trips and activities but no signs of hole and as comfy as skipper so these are my go-to's
[nomy4r4] (score 2, diepte 4) Yeah it's draining to me. Me too continuing  to look.
[mj7cqib] (score 2, diepte 0) I used to have lots of problems with my toes but brooks runners have sorted it out. Think I'm on my third year now of pretty much wearing them 96% of the time.  I had to go for a larger size to solve my problem, i.e., size 5 instead of 4
[mj7dicc] (score 2, diepte 0) Topo’s have the best toe box and wide sole base.
[mj7xhf8] (score 2, diepte 0) Lems, they’re just what you’re looking for.  Signed, 2E guy
[mj7znh2] (score 2, diepte 0) A different kind of shoe altogether, but I have wide feet and have similar issues with a lot of shoes. I live in (and do a ton of travel walking) in Dansko clogs.
[mjaalrf] (score 2, diepte 0) Merrils
[mjbcoxv] (score 2, diepte 1) Seconded. I hiked the Kokoda trail in them, backpacked Asia and now use them as gym shoes.

That being said, my daughter hates them and has been pestering me to buy a better looking shoe. But I refuse, I love em.
[mjazylz] (score 2, diepte 0) Merrell gore tex . Nice , comfortable and if it rains they stay dry. Only have to take 1 pair of shoes .
[pdm94or] (score 2, diepte 0) No one mentioned Reef Neptune
[oj3cq9j] (score 1, diepte 2) Good to know about the availability of wider toe boxes for Hokas. I’ve developed pinch calluses on both feet from them and assumed they only come in the standard size (narrow).
[mjb67h4] (score 1, diepte 1) Also recommend Hoka’s! I wear the Clifton 9, I have Morton’s neuroma in both feet along with high arches and these are great shoes for walking.
[mrc2hsb] (score 1, diepte 1) My podiatrist just told me to ditch my Hoka Clifton 9's and get something with a wider toe box.
[mjdesn8] (score 1, diepte 1) Agree! I recently bought the KS86 and was surprised on how much room my toes have! 

I also sized down a 1/2 size in the KS86.

My feet are happiest in Keens and Teva.
[nombl7i] (score 1, diepte 2) Hello...did you buy these online and went to a store? I have never hear of Keens before.
[nomgy4i] (score 1, diepte 3) Purchased in store at DSW.
[nomyder] (score 1, diepte 4) Ahhh ok. Yeah I use to work next to a DSW. The way I would get off work and hop over there 🤣🤣🤣🤣. Ok thanks. These are so cute.
[npat7q3] (score 1, diepte 3) Keen ate awesome shoes. I've been buying them for about 15 or 20 years now. A lot of their newer styles I do not find very comfortable, they've gone to fashion over form; but any of the Targhee line (especially v2, not so much v4) are comfortable and supportive at the same time. My feet love them and they have great support. The "bumpers" are ridiculous but still cute and protective. 
Until about 10 years ago I only had a few pairs of shoes total, now I have 3x targhee hiking boots (for walking in rainy Vancouver in winter) 1x Elsa red plaid, 1x walking targhee low, a pair of howser slippers and a pair of sandals. 
Really important to try them on in store if you can to determine which size works; Keens have an awesome return policy but it's nice to get something you can wear :)!
It took me years to find shoes this great, hope you enjoy them too
[nomc82l] (score 1, diepte 2) Hello...did you  buy them online or go into a store? Thank you.
[nomtvy2] (score 1, diepte 3) I would recommend going to try them on in person to see which style fits you best. I purchased my first pair in store then ordered another 2 online.
[nomyhmf] (score 1, diepte 4) Ohhh ok thanks so much. Good idea.
[mj6a1d9] (score 1, diepte 0) Toe pain? Are you sure your shoes are the right size?
[mj891im] (score 1, diepte 1 OP) Yes. Skechers just seem to fit oddly, which is a shame as they are quite comfortable. I've tried this style in 7w, 7 1/2w and 7 regular. They are either slightly too big somewhere, or slightly too small. My regular size is 7 1/2w.
[mj8at0r] (score 1, diepte 2) Oh darn. I need custom made shoes. My left foot is an 11 narrow and my right foot is a 12 regular.
[moj6ba0] (score 1, diepte 3 OP) I guess I shouldn't complain!
[mj8ur6w] (score 1, diepte 1) I'm a New Balance fan, wide size as well. 

If I'm walking around 10k a day I wear waking shoes from them. If it's a lot of walking and over 10k days frequently, I'll wear their running shoes, which are uglier but more comfortable for me when walking a lot.
[nomchkq] (score 1, diepte 1) Hello...how did you  calculate  that you have 4e feet? Is 4e for hella wide?  Because that's me.🤣🤣🤣🤣
[mj6eky3] (score 1, diepte 0) Ryka
[pdw0c0x] (score 1, diepte 1) Recently the D widths for new balance haven’t been that wide.
[mj73yqp] (score 1, diepte 0) Hokas, but break them in! Walk around for a month or two inside your house. They have a wide toe area and don't hurt my feet. I see big people in hokas, runners in hokas.
[mj8jg7i] (score 1, diepte 1) I also wear NB — 577 in a wider width even though my feet are narrow (lace ups fix that.)

These are my street shoes and my hiking shoes.

I use orthotics, but NB also has really comfortable insoles with arch support. Expensive but last forever.
[mj7avhi] (score 1, diepte 0) Allbirds running shoes are my favourite for travels as they are stretchy and also breathable. (Don't go for their daily use sneakers tho - they are fragile)
[mj91m6y] (score 1, diepte 3 OP) Sadly the Skippers are the widest style when it comes to the toe box. That's why I selected them. Ah well.
[nomeugw] (score 1, diepte 2) What did you end up getting? Thank you.
[nomfowk] (score 1, diepte 3 OP) I gave up and went with my trusty Skechers Go Walks. Still looking, though.
[mj7azow] (score 1, diepte 0) Easy Spirit wide size
[nomdyyq] (score 1, diepte 1) Hello did you buy offline? I don't see this brand in stores.
[mj7bqp9] (score 1, diepte 0) Hokas 100%. I have narrow heels and wide at the toes. They have a wide toe box and are like walking on clouds. They are the only shoes I can wear without my feet and back hurting. Go to a running store and get fitted for the shoes that work best for your needs. You don’t have to be a runner. They have all kinds shoes and know their stuff.
[mj87enm] (score 1, diepte 1 OP) Thanks. I've often gone up a half size to get more toe room, but then the shoes slip because they're too long. How do you avoid that with Brooks?
[mj7d3c9] (score 1, diepte 0) Keens, Altra’s
[mj7f3w7] (score 1, diepte 0) Fitville (available on Amazon) advertises their shoe have a wide toe box. I'm a 14 wide and they, and new balance are about the only ones that fit me.  They have non-wide also. Plus you can find them on sale a lot, you can usually pick some up for $50 - $75.
[nomemfd] (score 1, diepte 1) What shoe do you  get from Fitville on AZ? Now are they wide with w wide toe box or just wide toe box?
[mj7f5x2] (score 1, diepte 0) Walkhero shoes have been life changing for me
[nomepad] (score 1, diepte 1) Where did you get these? Never heard of before. Thank you.
[mj7hb2t] (score 1, diepte 0) Altras & I also wear astrals. Astrals are not designed for walking but I find them super comfortable with a wide toe box.
[nomdtax] (score 1, diepte 1) Hello...which Brooks do you like?
[mj7oso3] (score 1, diepte 0) This is a brand new company that has wide toe box sneakers:


https://velocirunning.com/
[mj7tdyy] (score 1, diepte 0) I wear Ultra Armour 4e running shoes and Altra in both Lone Peaks and leather Torins for dressier days.
[mj7wr1r] (score 1, diepte 0) Dansko Paisley!
[mj9rcbv] (score 1, diepte 1) Just got a pair of trailheads the other day. Loving them so far.
[mj80hkw] (score 1, diepte 0) KEEN
(16 reacties met lagere score weggelaten)

=== THREAD q7a16u ===
SUBREDDIT: r/Mommit
DATUM: 2021-10-13  SCORE: 282  REACTIES: 70
TITEL: Foot fracture and I want a divorce
POST (source_id=post):
I've fractured my foot since this fucking family never lets me sit down. I work on my feet and come home to endless chores before going to bed late and getting up early to do it all again the next day. I'm off work for a week and yesterday was day 1.

My husband stayed home from work yesterday with a sinus infection.

I cried. I said please dear God why would you do this. I was looking forward to watching TV all day by myself but I can't when he's home. I said tomorrow will be better. I'll take my son to daycare and finally have the house to myself. 

The kiddo is staying home today and SO IS MY HUSBAND.

I'm crying on my back porch.

I want a divorce. 

I yelled at him because I get so many sinus infections and just GO TO WORK ANYWAY because we have bills to pay. He knows how I felt and still chose to stay home anyway. Now I have added bills stress because we're both out of work. How fucking useless. I should go to work anyway with my boot and my fracture since I'm surrounded by people who don't give a shit.

I'm so so so so fucking angry.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hghnifl] (score 265, diepte 0) This is only a drop in the bucket of problems represented here, but it's the immediate one: why can't you watch TV by yourself if your husband is at home? I get it once the kid is home - obviously you're no longer taking a break.

But you don't have to watch your husband, right? Why can't he let you watch TV in peace?
[hgh5u1z] (score 215, diepte 0) When I was pregnant with my first daughter, my ex stayed home for a full week because he felt "wonky".
Finally, after losing a weeks worth of income (that I had to cover) I asked him what his symptoms were. He said he was low key nauseous, his back hurt, he had intermittent headaches... I looked at him and said "You're fucking pregnant! Go the fuck to work. It doesn't stop me and I'm actually pregnant!"

THEN! When I was pregnant with my son, I had the worst gastro of my life. Ex puked 3 times and slept for 20 hours, leaving me with a toddler. Then, when I got it, I puked every 20 min for 4 hours...and finally it tapered off a little and I could hold down water. I was still puking the next day when he left for work and left me with a toddler again. *THAT* he could go to work for.

AND THEN...... again, pregnant with my son, I got appendicitis. I had a prenatal appendectomy. I got a whopping 3 days of "recovery time" at home before I had to do chores such as getting on my hands and knees cleaning under the dining room table because he thought it was unreasonable to expect him to look under the table when he vacuumed the dog hair. (I put recovery time in quotation marks because he still went to work and left me with a toddler)

I don't say all this to personalize your problems or to make like others have it worse... I did it to point out a word I said over and over... EX. He's now my ex.

I figured, if I was acting like a single parent already, I'd go whole hog.
I refuse to be in a relationship that isn't a partnership. I'm busy raising my own kids, I won't raise his mother's kids too.

Now, I did as much as I possibly could to keep the relationship together and he put as much effort into the relationship that he did the housework but eventually I hit my limit. 

You're not alone in your struggle but you also don't have to struggle.
I've found one of the worst feelings is being alone to deal with life when there's someone next to you who should be helping you and refuses to do as such.
I'm viciously independent and I'd personally rather do it alone than sit and rely on someone who has built a relationship foundation on letting me down.
[hgi2tqk] (score 96, diepte 3) I’m certainly not in this sub because I cater to my husband…
[hghtn43] (score 88, diepte 1) This was my first thought as well. I mean, there are a lot of problems here, but this raises some questions
[hgijjmx] (score 81, diepte 2) So many problems here. The biggest one to me is crying because your husband is home with you. I LOVE having days off with my husband. He’s my best friend. OP’s relationship must be really awful for this to be her response.
[hghu44j] (score 72, diepte 1) I’m not the OP so Idk how she feels but for me it is a different kind of relaxation when my husband isn’t home.  The guilt of watching TV when there are dishes in the sink, or staying in pajamas half the day is something I only feel when someone is home.  Even though my husband doesn’t care, it makes me feel guilty knowing someone knows that I’m kicking back when there’s stuff to be done,  because let’s face it, with kids there is always something to do.
[hgiaieh] (score 61, diepte 5) Ummm I was completely unaware this is a sub for women married to shitty men....? My husband is awesome. Can I still be here?
[hghp1qi] (score 55, diepte 0) I don’t understand. Why can’t you relax when your husband is home sick? Can you not take your kid to daycare anyway and watch TV at home for a change? Tell your husband to get some sleep in the bedroom and you sit in the living room and chill right? Am I missing something here?
[hghwy2f] (score 48, diepte 3) Then don't? I really wish you didn't feel that way. They're grown enough to have sex and make babies, they're grown enough to clean up after themselves and get their own food.
[hgh5b7j] (score 43, diepte 0) If you can't afford it, tell him that you are taking his lead and will start taking time off for sinus infections. Viral ones don't go away with antibiotics and last a few weeks, but antibiotics aren't good for your gut biome anyway. And make sure you get plenty of rest!
 You are supposed to be partners. If he wants to be a stay at home dad he can do the chores for it. If he doesn't, he should probably get back to work. If you two as a couples can't afford to take time off for sinus infections, that's something you both should talk about.
[hghwilx] (score 43, diepte 0) Why can't you watch TV while your husband is home?
[hghtqqp] (score 42, diepte 0) With all due sympathy the thing you should be angry about is a system where people have go to work with sinus infections, not your husband.

In the US I went to work (teaching) with the flu, and no doubt spread the joy. In Europe, I actually got to fucking rest with 80% pay during my high risk pregnancy and almost certainly prevented a stillbirth. My American friends actually had miscarriages and stillbirths in the same position.
[hgi5fbb] (score 40, diepte 5) 🤮 Stop with the shitty all men are lazy and don't know how to take care of themselves or be a father generalizations. Gross. This isn't a 1980s sitcom. 

The majority of married women are not getting screwed over by their husbands. Stop being a doormat if that's your truth.
[hgi1u4h] (score 35, diepte 4) Because many men don’t behave this way UNTIL the child comes. Then they suddenly become the third child. They don’t wake up when baby cries, don’t know how to get kids dressed and on. It’s a cultural learned helplessness and it’s exhausting. Each generation of men gets better so all I can hope for is raising my son to be a better man.
[hghmxw2] (score 29, diepte 0) Yeah I was always worried about leaving my ex because of money. Turns out that when he left I didn’t have it any better but not any worse either. I gained financial control in the sense that money wasn’t going to expensive food orders and nights out with the drinking buddies anymore. I was saving money with him gone. 

Oh the kids? No that was the easy part because I already felt like a single parent. If anyone was sick I had to suck it up anyway. 

It was the money part that worried me but I’ve been doing this solo for 2 years now and ten out if ten I can recommend. The fu*k we need men for. So my ex is now living together with another lady and I wish her well. I really hope she doesn’t tolerate his bs and that he is stepping it up. Me I have a new bf but I’m not living together anytime soon. Solo is the way to goooo

Good luck Op. you’ve got this.
[hgidule] (score 29, diepte 0) I don’t want to come off flippant but if you don’t want to do the chores then don’t. No one is making you do them, you are doing them. Stop and maybe he will do them. If he says something then tell him he has the ability to do chores too. Don’t tell him you aren’t going to do them, just stop and say nothing.
[hgin81i] (score 28, diepte 1) ALL OF THIS!  If you are already acting like a single mama, might as well just be one for real.

We get married to have a partner and if our partner isn't acting like one, then we should move on.
[hghzewr] (score 27, diepte 3) Okay, genuine question, no judgement, I'm just trying to understand this dynamic. Why have children with someone like this? Better yet, why be in a relationship with someone like this at all? I get that it's not always that simple and that there are a lot of reasons why someone might stay in a less than ideal relationship, but why do we keep accepting this type of behavior? I never would have gotten to the point of marrying my husband, much less having a child with him if he behaved like this.
[hgiwki3] (score 25, diepte 3) That part made me really sad, too. My husband and I have had our ups and downs in the 13 years we've been together, but I am for sure happier when he's around. We're currently on parental leave together and even the crappy parts have been better because we're tackling them together.
[hgi27gr] (score 23, diepte 5) I love how men think we just automatically know how to do this shit. Like no, I barely know what I'm doing either but I figure it out because I'm an adult.
[hgijsg3] (score 20, diepte 6) Lol my husband isn’t perfect but he is awesome and my literal favorite person. I didn’t realize hating the person you committed to was a prerequisite for this sub. Whoops. /s
[hgj5n25] (score 20, diepte 2) It is also a different kind of relaxation. I have shows I watch by myself but if my husband is home I will usually watch shows with him that we both like. Sometimes when you expect one thing to happen, it can be disappointing when it changes, and pile that one disappointment on top of everything else OP is dealing with and you get a breakdown.
[hghu5oo] (score 20, diepte 0) This is when you say fuck it and do the bare minimum at home until you get your rest. Go to a cheap motel on your day off and veg in front of the TV.
[hgim6lt] (score 18, diepte 1) Idk, not so easy for most when the partner doesn’t care that the dishes aren’t done, there’s no clean clothes to wear, the fridge isn’t stocked up, the dog hasn’t been walked, the floor hasn’t been vacuumed etc but you care. You care so you want it done. Their threshold for a messy house is a lot higher than yours and it’s so tiring to keep telling them to do things because they’re not bothered.
[hgjsqsn] (score 17, diepte 2) Sure, that’s understandable. But that’s why “taking turns” is a thing. If her husband doesn’t let her *watch TV* when she wants, then that’s indicative of a deeper problem, IMO.
[hghwv8v] (score 17, diepte 3) If everyone in my house is perfectly comfortable sitting around relaxing while there's chores to be done, why shouldn't I? I worked hard to make sure I stopped feeling that guilt and just do the chores whenever I feel like it.
[hgh96m5] (score 15, diepte 0) That sounds terrible im sorry hes not helping you. File some papers and see if he cares about the big wake up call
[hgil3zg] (score 15, diepte 7) People are much more likely to post and seek support if they’re in a bad situation. Why would I post about how supported I feel by my awesome husband? If you went to r/pregnant you’d think no one ever had a healthy pregnancy either.  If you’re unhappy in your marriage you should make a change. It’s not “the truth” that all men are lazy assholes, plenty of us are in happy, healthy relationships and you could be too!
[hgiherx] (score 13, diepte 5) 100% When I met my partner he was the most gentle kind and generous man I’d ever met. I was certain it felt right and I generally dated nice guys before that.

After the baby came. Miserable, defensive, selfish and uncaring; his problems/illness/work stresses are bigger and worse than mine…

He works at an executive level. I’ve seen him ‘working’ in his pants on the sofa whilst watching tv. I meanwhile have a three hour round commute + a 9 hour work day and earn a third of what he does. But I still carry the mental and physical labour load when it comes to our son being fed, clean, clothed, healthy, entertained, comforted. Not to mention the housework.

You’re right, society is imbalanced in favour of men climbing the career ladder, whilst being able to step in when it’s fun dad time. 

This isn’t all men. But there should definitely be a boot camp where dads are left with nothing but a messy house, a limited budget, the baby, and are just told to go figure it out for a month.
[hgkfntx] (score 13, diepte 3) In this case it clearly is an issue for OP, but I would like to offer another perspective. I love my husband dearly and he is my best friend but I also am deeply introverted. I desperately need alone time at home sometimes to recharge from anything and everything happening in life. I was like this growing up when living with my parents, later with roommates, and now with my husband. My husband similarly benefits from alone time at home. It isn’t a reflection on our relationship but instead an inherent part of our personalities.
[hghwehi] (score 12, diepte 2) This is the first thing I thought as well! It’s so true.
[hgieg69] (score 11, diepte 0) Are you getting stress fractures in your feet? From work? Jesus. 

Is there anywhere you can go tomorrow? Get on a bus and go for a coffee? I know your foot is busted but it really sounds like you need some alone time.
[hgio0m2] (score 10, diepte 5) I think you are in the wrong sub. I’m here just to share stories with other moms. My husband is a wonderful father and partner.
[hgixlkx] (score 10, diepte 3) This makes me sad.  I love when my husband is off and can be home with us.
[hgjb9wq] (score 10, diepte 3 OP) Thank you, yes, this is 100% it. Did I feel terrible for being mean to my husband? Yes. But it's also how I truly feel. I can't take 1 more problem so he gives me 2 instead.
[hgj9c49] (score 9, diepte 1) I LOVE “viciously independent.”  That’s exactly how I feel / have felt for the past four years.
[hgib072] (score 9, diepte 0) Does your husband not allow you to watch tv....!?
[hghyixo] (score 7, diepte 0) This whole thread just makes me so angry and resentful. Why do we even bother with men?! Damn the devil’s eggplant.
[hgi1doj] (score 7, diepte 0) I feel you OP. When I was on maternity leave I could not wait until my husband went back to work and left me alone during the day. He was just a nuisance around the house. And man colds are just impossible. They can’t even function with a stubbed toe let alone a sinus infection. Just do bare minimum this week and don’t go above and beyond. Let him feed himself and don’t worry about him. Put the 2 year old in front of an iPad and watch your shows with your feet up.
[hgin9pu] (score 7, diepte 2) There has to be consequences or they will never step up, what are you going to do about it? You will keep getting walked on if you don’t do something about it.
[hgk5y9w] (score 6, diepte 3 OP) Oh man we had that conversation a year ago...
[hgkl3w5] (score 6, diepte 4) Oh, I’m also a huge introvert. If I ever need alone time, I just tell my husband and he’s happy to oblige. The fact that OP feels so trapped she’s crying indicates she can’t just tell him she needs alone time because it sounds like he’s a major asshole.
[hgjqaca] (score 6, diepte 3) This I get. My husband isn’t half as unhelpful as OPs (actually, my husband is very helpful) and I hit the same wall earlier this year. I switched jobs and gave 2.5 weeks notice. My employer wouldn’t let me stay beyond 2 weeks so I was supposed to have 3 days off before I started the new gig. I was desperately looking forward to that me time, I even avoided the habit of scheduling that time down to the second for productivity.

Then my daughter got strep throat, the fever started the evening of my last day. So I spent 3 days and the weekend caring for her, running errands that I had to do anyway and generally trying to keep me and husband healthy. I cried. I was so angry and disappointed that my first break in 2.5 years (we have no family within 14 hours of us) was taken by a damn bacteria. The disappointment was worse than the actuality.
[hgjwyml] (score 5, diepte 2) I told my ex Something when things were starting to rapidly decline 
"I don't need you. I want you. I'll never need you but right now I want you. It's up to you to make sure things stay that way."

He didn't listen
[hgi2wcu] (score 5, diepte 4) >Why have children with someone like this?
I can't answer for OP just me.
1) expectations- women+man=forever love
2) expectations- women in relationship = baby
3) low self esteem - don't want to be alone so anything will do.
4) expectations- wife=duty=sad noises 
5)expectations- It's law of the land that we do this. Its are duty as women
6) lazy/depressed/ negative ideas of self worth 


>might stay in a less than ideal relationship, but why do we keep accepting this type of behavior?

They don't start that way, when the honeymoon stage ends you are already trapped. You would be surprised how much this world is designed for us to lean/need them. 

>I never would have gotten to the point of marrying my husband, much less having a child with him if he behaved like this

It's why we leave, we are not dumb we just think this is the way. We have been told that you need to be with a man.
[hgio5hy] (score 5, diepte 6) She seems to be a lost Redditor here.
[hgihuby] (score 5, diepte 3) My partner cooks all the meals and I absolutely do not cater to him!
[hgkwnvz] (score 5, diepte 5) Yeah.. I don’t mind having my alone time either. Especially when I’m living in a one bedroom apartment lol. When he’s home I don’t mind it now more than ever that we have a baby but before if he stayed home I just did my own thing if I wanted my alone time and just chill in my room I didn’t have anything to do or watch. I would completely zone out.
[hgii0e2] (score 5, diepte 4) This 100%.
[hgils5n] (score 5, diepte 2) We live in a one bedroom and husband WFH so watching tv while everyone is home is difficult. I get her views, sometimes catering to a sick husband is ridiculous.
[hgiw030] (score 4, diepte 5) This is so sad, and I'm really sorry that it's been your experience. Every time I read posts like these I'm more and more grateful to my in-laws for the values they modeled to my husband. I'm glad to hear you're doing the same with your son.
[hgj6bl2] (score 4, diepte 1) maybe there's only one TV
[hgifhc0] (score 4, diepte 1 OP) I am! And thank you, I do need some alone time. I have a dentists appt, not sure that counts! I walk around 5-7 miles a day at work. A bus and coffee sounds lovely quite frankly!
[hgklmwj] (score 3, diepte 2) Get that alimony and child support. Don't stick around just because you can't afford to leave.
(15 reacties met lagere score weggelaten)

