# Label-batch batch_0089

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
Schrijf het resultaat naar `batch_0089.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: v0iqib, 1o0q3bi, k87dpt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD v0iqib ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-05-29  SCORE: 126  REACTIES: 79
TITEL: I don't understand why waiting in line to talk to an HR rep, they can't provide chairs to sit in. Employees work hard and are on their feet all day. If you have to sacrifice your break for work related issues, they should qt least allow you to relax before you have to bust your butt again.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iagsnyr] (score 90, diepte 0) Never go to HR on breaks. Always do it mid shift or after lunch. No one can tell you that you can't go to HR, so do it when it's usually slower.
[iahan29] (score 37, diepte 1) At our site they tell us we need to be off the clock to talk to them which is bs lol … like bitch im not coming on my day off to talk to yall
[iagncts] (score 36, diepte 0) Make a comment on the VOA board.
[iagyvex] (score 30, diepte 1) The last site I was at, the HR team only came out at certain times to reduce AAs leaving their department to come to them & not working

Edit: 

Or sometimes they wouldn’t come out at all & we had to call them via chime lol. 

The office also has a badge to scan in & AAs can’t scan in, so AAs can’t get to them via the office either. 

HR really didn’t want to deal with AA problems it seemed like😂
[iagzx86] (score 24, diepte 0) I refuse to use my break time to talk with them. If you can’t find them during your shift, email site HR. It’s easier and then you have what they told you in writing.
[iah7c3m] (score 21, diepte 2) Amazon has a no chair fetish, doubt anything will change.
[iahybl8] (score 21, diepte 2) Yeah no way... talking to HR is company business. Should be done on the clock period.
[iagxvyu] (score 21, diepte 0) While I was waiting in line to talk to HR for important issues.   One of the manager Saw me from a distance and yelling at me saying I have to go back to work NOW. It's really so disrespectful that he was screaming  at me in front of everyone. He could've told me that in polite way with respect. Unfortunately, some of the managers are very abusive and look down on their fallow employees.. Yes Amazon company is a money making machine with a good benefits. But it comes with A HEFTY PRICE TO PAY. unfortunately.
[iagp0vt] (score 12, diepte 1) And then?? Chairs at work stations for scan to scan break compliance???
[iagsouu] (score 12, diepte 1) My boyfriend stood and waited 45 minutes for hr to talk to them once because he needed to put in a hardship met day transfer and they just acted like he didn’t exist while they chatted with an associate about their life outside of work. He still didn’t even get to speak to them, he just left the paper on their desk and I’m pretty sure they just threw it away cause he never got the transfer.
[iagnjse] (score 11, diepte 1 OP) I will. I am sure many people have made that suggestion already.
[iah0tsh] (score 11, diepte 0) HR is probably the worst thing about AMZN. The HR at my old FC closed 1 hour before the end of our shift, and breaked for lunch at the same time as one of our breaks. They would also be closed for 30 mins before shift.
[iaha5un] (score 10, diepte 1) you can report that I’m sure.
[iah4jr0] (score 10, diepte 0) They have refurbished ours and there is now couches to sit on while you wait. It looks really nice. I’m in the UK though
[iah0pmd] (score 9, diepte 4) Well the moment an AA is in line, they are technically at HR ,whether they're scanned in or not. Cameras are everywhere with that. But that whole situation just seems sketch as hell. I wonder if that site had gotten a lot of complaints to the ERC?
[iah089t] (score 8, diepte 3) Added onto it, HR had 2 separate desk areas but only used one of them lol. I guess when the site launched they had the first area then moved. 

Only reason I noticed is because the HR & Learning area was in my department. So, everyday when I’m walking up & down checking the lanes I’d see a long line with no HR person. 

The cherry on top was that the site also didn’t use any labor tracking to track AAs who were at HR/scanning them in. So, we have AAs “missing” but they’re at HR & you wouldn’t know unless you swung by
[iagu9rt] (score 8, diepte 0) Dealing with HR is not considered break time
[iai4y6g] (score 8, diepte 0) Im fairly new to Amazon, and I’m an OMR…I feel for those folks who are on their feet and bust their ass all day. If I see someone struggling and just needs a few mins off their feet, I have them come to AMCARE, scan them in, and sit down. I’ll place an ice pack under their knees and let them be for 15 mins. Even if its just a little bit, I just hope it makes their day better. All 10 hours of a shift doesn’t have to be awful.
[iagoys3] (score 7, diepte 0) Why are you wasting your breaktime for it? Before shift, during shift, etc. Don't ask to talk to HR, you tell them. 

They can code you, and that's that. Document time there and back (some AMs and HR are shifty AF, so you still gotta cover your ass) but if you got the time stamps, they can't refute.
[iagzpuz] (score 7, diepte 0) I hate it some people drag out the session more than 10 minutes. Keep it simple. Don't act like a granny. If you have a ton of questions, do it when there is not a line of people waiting.
[iah8jm1] (score 6, diepte 2) Nobody at my site ever showed us how to use chime or
 that we could?? What would be our login?
[iahs0zy] (score 6, diepte 2) I'm not trying to stand in line staring at the floor, waiting for a 3 minute HR fix. I've been at Amazon long enough to know how to take an "extra" break without getting hit with TOT or anything, than going to HR or wasting breaks going to HR.

Edit: And as someone who never struggled with rate other than Single Smalls cuz it kills my fucking back, I never had an issue with that. Plus I switched to a department where rates aren't worried about so that's a plus.
[iah5izg] (score 6, diepte 0) I feel I saw someone post a VOA board about this, also including the fact that on slow days when we stand for hours doing nothing we should be able to sit down, the response they got was basically "We are here to work, not relax".
[iah1fa2] (score 5, diepte 5) Idk if AAs complained about HR to the ERC, but they did to me & other managers. 

I mention the no tracking when AAs are at HR because none of the AMs knew where our AAs were. *(I was an AM at the time if it wasn’t clear lol).* 

So, we (AMs) were accidentally writing up AAs for TOT & stuff, or had to STU them to find out where they were. Yeah, there are cameras & we could verify, but realistically no one was gonna put in that effort to track AAs down at HR each day. 

- It was common for AAs to be gone for 30-60+ minutes waiting in line daily at HR.
[iaho4hv] (score 5, diepte 1) This. At my building you have to hunt down HR from their desk outside down into their own little private offices. They’ll literally hide during our breaks so they won’t have to deal with us.
[iahz53b] (score 5, diepte 1) Would have turned to HR and told them to add that to a report and sign it as a witness.
[iagybfd] (score 5, diepte 0) If it’s that long of a line and if you don’t have a problem that needs to be fixed right away call ERC or come back after break or ask your AM can you go see if the hr line is gone
[iah41vd] (score 5, diepte 1) Yeah but yoy gotta go on your own time. Why arrnt their breaks different? Arent they sitting down? Their break cant be an hour after the first set of breaks?
[iai4t5j] (score 4, diepte 2) That’s messed up!
[iajlh8n] (score 4, diepte 2) The expectation is before or after your break realistically. Really though, there are very little reasons to ever need to visit site HR. Creating a ticket or calling ERC will resolve 99% of issues people have.
[iah63jq] (score 4, diepte 0) Just walk over with a chair from a break room.
[iagqqo5] (score 3, diepte 0) I don't mind the no seating available.. What I find annoying is the waiting in line while HR can see you waiting and keeps you waiting during your break while they are catching up with one another or looking at their screen. It doesn't take much to let you know they won't be long or even acknowledge you. I usually call ERC on my day off unless I absolutely have to see HR.
[iagqx69] (score 3, diepte 0) Just get their email and email them.  That's what I do.
[iagzv0u] (score 3, diepte 2) Lol that shit sounds like a lawsuit waiting to happen
[iahufm7] (score 3, diepte 1) This. I never spend my down time there. I usually go when I first walk in (after I clock in) cuz fuck stand up and this way I’m not getting tot
[iahjrqj] (score 3, diepte 3) Thats what they told me lol. But now they are doing that "only your on site HR team can handle this issue" shit, whereas before they had all my issues solved within 24 hours and sometimes within the same hour.
[iahhbfo] (score 3, diepte 1) f that wow
[iahqs72] (score 3, diepte 0) I don't  punch out to talk to HR or use my breaks.if i need to go talk with them.i am doing it on company time
[iai1o7i] (score 3, diepte 1) That's what it's  supposed to be... so many folks in this post been lied to by ops.
[iai3pqy] (score 3, diepte 0) I don’t understand why anyone is trying to talk in person to on-site HR at all. I do an HR case on A to Z for EVERYTHING. Then there’s documentation of the information I’m given and what they say they are going to do for me. Don’t ever trust that something is taken care of based on a conversation at the HR desk.
[iah985t] (score 2, diepte 3) HR-wise, they don’t want T1s or T3s chiming them or at least that was the response I got from my last HR team lol. 

Chime or well Slack *(because Amazon is supposed to be phasing out chime & converting over to Slack)*, your direct manager has to:
1. Setup your Amazon work email if it isn’t already setup
2. Setup your Slack account 
3. You’ll also need a security key, which your AM can put in a ticket for you to IT to get & get setup — *or at least need it at some point*

Every internals Amazon email, Slack account, Chime, etc… is login@amazon.com *(insert your login where it says login).*

###Edit:

Added to this, for hourly employees HR ideally doesn’t want you to be using Chime or Slack off the clock.
[iaikp15] (score 2, diepte 4) has anyone actually tried the new version of chime? slack?
[ianauu4] (score 2, diepte 4) You will not get a midway key as a T1 except in extremely limited circumstances (such as a role which requires it like an IT equipment coordinator)
[iai02i3] (score 2, diepte 4) Not sure exactly when. Our site launched last year and HR (of course) wanted a lenel put on the office door. LP regional said no because they are no longer allowed. I just came back from a legacy site that has the lenel still next to the door but it’s been deactivated.
[iai0zsz] (score 2, diepte 5) Ah okay. Yeah, I don’t think the site got the memo. 

Now, we did (L6+) including me as the only AM, had an argument about the how lenel scan in & locking the front office. That was an interesting conversation to say the least lol
[iah3qbh] (score 2, diepte 1 OP) Not sure what is pety?
[iah4zic] (score 2, diepte 2) No. You don’t.
[iahmxgt] (score 2, diepte 0) I think it’s because some people fall asleep when they find somewhere to rest.
[iaho24z] (score 2, diepte 0) Lol Amazon doesn't really give a shit about you
[iahy2kv] (score 2, diepte 0) If you look at official documentation you’re only supposed to see HR when you are on the clock, before shift start, or after shift end. You’re not supposed to see them on your breaks or lunch. This is why they are usually not there at the front desk during scheduled breaks. Also, what’s wrong with going to their office? I would much rather go handle an issue in their office with the AC on and a bit more privacy than stand there at the front desk. Familiarize yourself with company policy. Then you won’t have as much to bitch about. And if they tell you that they can’t see you except on break you’re being played. And you allowed it to happen by not knowing what’s up.. 🤷🏻‍♀️
[iahzwi2] (score 2, diepte 0) I fainted in hr once. That’s the only time I was provided a chair
[iajlvge] (score 2, diepte 1) Exactly how I feel, documentation is king and you don't get that talking to people on site.
[iaiy87n] (score 2, diepte 1) There was one week I had to visit HR three times to fix the same issue. They had put in the wrong hours for an accommodation excused absence, and I foolishly trusted them to be able to do basic time counting twice. The third time I just straight up told the guy "you count time like this," he entered it in, and suddenly the problem was solved.

My guess is this is far from uncommon. And if you don't go hold their fucking hand, you'll just be back the next day. (Sometimes even if you do!)
[iai8dj1] (score 2, diepte 0) You should be clocked in when visiting HR, not on break or lunch. Make sure you let your manager know otherwise you will start accumulating tot.
[iaiff7v] (score 2, diepte 0) Don’t go to HR on break. It’s a work related matter so you do it on their time not yours.
[iaixi8x] (score 2, diepte 0) i was just having a conversation about exactly this with a couple coworkers the other day. it just feels like some sort of micro aggression. seeing the HR reps either sitting on their butts the WHOLE time or them not even being there when we walk however tf far to speak to them, it just feels like one of the many slaps in the face the “higher ups” hand to us. hate even calling them that because they are just people like the rest of us.
[iagna1s] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[iajbtlj] (score 1, diepte 5) We use both, Chime is much better.
[iaod2a0] (score 1, diepte 5) That’s true. But if someone who needs all of this then I’d assume they’re in a role that needs it. 

I got many of my T1s midway keys, even ones who weren’t fully yet in the role but we were just about to test them out
[iahyoje] (score 1, diepte 3) When was this? My last site had them from at least end of last year to this year end of Q1. 

I can’t say if it’s still there because I left Q1/2. But it was still there prior to my departure
[iai17zd] (score 1, diepte 6) Or they ignored the memo. Can’t have the common folk wandering about.
[iaikk9s] (score 1, diepte 2) ridiculous that these clowns are even allowed to be deserving and HR position. i’d bleed my heart out for these poor overworked people, i know how it’s like.![gif](emote|free_emotes_pack|flushed)
[iajivdr] (score 1, diepte 2) last time I went to hr, there was nobody there.  I went to the office and interupted a "meeting" and told them I need to talk to someone. they said about 10 minutes of I want to come back.  
they expected me to go back to work and forget about it lol
I sat my ass in one of THEIR chairs for about 45 minutes until someone finally showed up lol
[iaiemt2] (score 1, diepte 1) when I worked at my FC I was told we can’t go to HR during our shift bc they got pissy when ppl did this and expected ppl to go during their breaks or before/after their shift 🤦🏻‍♀️
[iajltry] (score 1, diepte 2) That's wildly false.
[ialzxbg] (score 1, diepte 3) Provide a source saying otherwise
[iah44ji] (score 1, diepte 1 OP) That is correct.
[iah48xh] (score 1, diepte 1) Because you have to go on your own time.
[iaixpb8] (score 1, diepte 1) At mine they have their open time listed as being the same as our start time, and are constantly 10-15 minutes late. Yet we're told they are scheduled to start 30 minutes before my shift does, so they're in the building and clocked on. Allegedly.
[iah86bz] (score 1, diepte 0) but the question is how many chairs? tbh they should allow us to go to hr during the normal shift but i don't know if the chair idea is too practical.
[iajlxtn] (score 1, diepte 2) Source? Because that isn't true
[iajozr0] (score 1, diepte 3) Talking to hr is company business, to be done on the clock. If they call you at the house on your off time ask for them to clock you in.
[iahryb0] (score 1, diepte 0) I always go on the clock before going in or when it's slow . A PA I had would let us go during slow times if needed but usually I don't go to hr just create a case.
[iaj1w4g] (score 1, diepte 1) At my site, HR only staffs the desk during breaks and they don’t allow any AA’s in the office. Company policy doesn’t mean anything when HR just hides. Not that they’re worth waiting for anyway.
[iaja73v] (score 1, diepte 2) It does mean something.. it means you call them on their bullshit and if they don’t comply you escalate the matter. That’s literally how that works
[iajhkjl] (score 1, diepte 3) Look, I’m not here bitching that I can’t see HR. I’m saying they’re useless and there’s no point in hunting them down anyway. They’re gonna get downsized or completely phased out like other companies soon.
[iai7pw5] (score 1, diepte 0) Why do people need to speak with HR so often? I’ve seen them maybe twice in the 4 months I’ve worked there, for a total of 10 minutes combined. I swear I see some Amazonians in line EVERY DAY for HR. I don’t get it.
[iai9ooh] (score 1, diepte 0) I never went on breaks, ever. No one even had to tell me not to. I go on company time.
[iaic7g4] (score 1, diepte 0) At my old site our HR had a whole desk strip where you can talk to them 

They had the office in the corridor but they we’re mostly right there at the desk near the entrance
[iaj6ku0] (score 1, diepte 0) Anyone in my department who needs HR just tells our manager and the manager will chime/slack someone from HR until they show up at our station with their rolling carts. They come to us just to shut up the obnoxious notifications from the AFE Pack manager. lol.
(14 reacties met lagere score weggelaten)

=== THREAD 1o0q3bi ===
SUBREDDIT: r/FASCAmazon
DATUM: 2025-10-07  SCORE: 21  REACTIES: 79
TITEL: Week 4 - My feet cannot anymore
POST (source_id=post):
New hire right here. Guys I never wore composite toe shoes before and OMG, my feet are so so sore today. I'm a gym rat and I worked in restaurants before Amazon (walking the whole shift) so I'm used to workout and staying up and walking. However my Reebok shoes I got are kilking my feet. I git blisters, pain, and even knee aches now. I got my compression socks and insoles as well but they don't seem to be working. Please any advice? Drop your favorite shoes, brands, accesories, or whatever can help. Thank you so much!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nifykhc] (score 5, diepte 0) 5 years in and my feet still be aching by the end of 11 hours. I wear insoles and the whole bit but it is just walking on concrete all day that does it
[niqwspb] (score 5, diepte 0) Former Amazon Safety Specialist here:

Walk into Amcare and tell them the issues you're having with your shoes. If you only wear shoes that Amazon provides, then they will take a vested interest in your foot care, as it would be a workplace-related injury to develop blisters. I use to cover Amcare for the last half of my shift, and at least half of the AA's that walked in were due to shoes and foot pain. 

Unless your site doesn't give you a shoe stipend on Zappos, never buy and wear your own shoes. If you sustain an injury at work that they can pin to "not using approved composite toe shoes" that were on their list, you'll be rejected from worker's comp due to not using provided PPE.
[nibg8bw] (score 4, diepte 0) I have wide feet and normal shoes have never bothered me much because they stretched to accommodate me. Composite toe shoes do NOT. Make sure your shoes actually fit and they're not too narrow and  rubbing on your toe(s) to cause blisters and such. I had to return mine 3 times to get ones that actually fit right and didn't hurt. Good insoles for walking on the concrete help a lot too.
[nieps8x] (score 4, diepte 0) When you use your credit for your composite work shoes, make sure you get a half size bigger than your street shoes.
[nib4hn2] (score 3, diepte 0) It will get used to it . Dont worry buy some insouls and its free from amazon . Same happened with me when i started it feels like my feet gone but after like 1 month its good
[nib72pl] (score 3, diepte 0) I was just like you back in August, even down to the Reeboks, then randomly around week 6 the foot pain just stopped. Idk if it’s because the shoes were finally broken in or what but now I can stand the entire shift with no pain and I didn’t change anything.
[nib7rsj] (score 3, diepte 0) Good insoles, not your 20 dollar ones. If you still have a Zappos credit grab the 12 hour insoles I believe they are called. Made a world of difference, there's a few products on Zappos listed towards 12 hour shifts and most help to a certain degree. Amazon should have some menthol gel to help if your facility has it. 
Foot massager, be the massage your foot with it cheap ones or the fancy just sit and relax. No money get a tennis ball and press down gently and roll your foot on it
[nibg8bz] (score 3, diepte 0) You have to shop for shoes, keen brand is pretty comfy imo
[nic0brm] (score 3, diepte 0) I order my shoes out my own pocket from Amazon. Those Zappos fck my feet up, they’re highly uncomfortable.. unless it’s the boots.
[nicm1ti] (score 3, diepte 2) People held up the line even with composite shoes on.
[nichy09] (score 3, diepte 0) I got the Airwalk Mongos (half size up and wide based on recommendations here) and the orange Superfeet insoles. Also bought Darn Tough Steely socks. They’re nice and thick, and even thicker in the toe. I came from running around a solo kitchen for the past 2.5 years and this hasn’t been shit. Yeah my feet are sore, but not unbearably like you describe. I second what the other person said about talking to your manager about another credit.
[nici47i] (score 3, diepte 0) My first month the foot pain was insanely bad I’m pretty sure the only reason I didn’t lost my feet was because I soaked them in epsom salt every night lol
[nicjesq] (score 3, diepte 0) Airwalks..get the airwalk comp toes. Your feet will thank you.
Also, take your shoes off during lunch
[nicmtp2] (score 3, diepte 0) Comp toes shoes are usually narrow, so try to get wide. Always read the comments on Zappos they usually are from Amazon workers so you can get the perspective of one of us. Search for shoes that are more for what you're looking for like: flat foot, high arch, wider foot. At my FC you can wear your shoes with a pair of shoes covers if you buy the covers on your own.  They won't let you use the Amazon ones.
[nicyg6b] (score 3, diepte 1 OP) Thank you for the advice! I didn't think they were gonna be so bad, so I went for how they look and not the reviews. I think I'll buy a pair but in an actua store so I can try them on first.
[nidr629] (score 3, diepte 3) Toby Il Nano Composite Toe… try to find something closer to reebox… every shoe that I’ve ordered they no longer have and every last one has been comfortable so I always do reebox or something closer to reebox also read the reviews cus they be spot on to .. hope this helps and customer service is very good with helping also
[niea2wu] (score 3, diepte 0) Get wide fit shoes to accommodate feet swelling
For blisters: Injinji ultra run toe socks or something similar. They are thick but moisture wicking and prevent your toes from rubbing. Leukotape on heels. 
After shift: Epsom salt foot bath, use a massage ball to roll out your feet 
Advil while you’re breaking them in 😞
[nieccvi] (score 3, diepte 0) Get the proper size shoes and socks designed for steel tied shoes.
[niez1cw] (score 3, diepte 0) I stand by the airwalk mongo... im a vans wearer and they feel the same. I have had to change the insoles twice
[nifa1j9] (score 3, diepte 0) They will. I think for the first six weeks all I could think about was my feet and one day it just..stopped. I don’t think I broke my shoes in I just grew numb.

 One thing that seemed to be torture at the time but helped me long term was I had a manager who would write us up for sitting. Would say it was a safety violation or insubordination. Seemed cruel but sitting makes it worse, stretch. 

 Good socks, lacrosse ball, read reviews on the Zappos shoes, look here and get a new credit, you can your manager will help. Timberland pros are good. 

 Hang in there, you will get there. I walk at least 17 miles a night now. You’ve got this.
[nihvnp5] (score 3, diepte 0) Some insoles suck, wide fit is a must, I’ve heard amazons insoles they provide don’t do good. The dr schools I use have been a blessing
[nip5127] (score 3, diepte 0) Do one size up and one size wider. I'm typically a size 12 men, but I wear a 13 4E. My brand of choice are the Avenger and Airwalk Brand.
[nib3l1i] (score 2, diepte 0) Here for the comments
[nid2evd] (score 2, diepte 1 OP) I just read your post and comments! I'm on the same boat you were on! We even picked the same brand lol
😂Well it's promising that I'll get used to it, but I'll try to get a second credit for shoes. Thank you!
[nid3s5n] (score 2, diepte 2) You’re welcome! I also just remembered I would keep 2 small water bottles in the freezer, when you get home sit down, put the water bottles under your feet and roll them for a while. Also buy tiger balm in the little jar. It’s great for anything aching you.
[nid0itk] (score 2, diepte 1 OP) Thank you for the advice! Next time I will but them at an actual store so I can try them on 🥲
[nibgia7] (score 2, diepte 0) If you don't already, when you get home, ice your feet. I learned this from a past thread on the subject in one of these subs. Like, immediately when I get home, I take my shower, I get a bag of ice and put it inside a shirt, then I watch an episode of TV alternating which foot is on the ice on top of a pillow in bed. It helps so much with inflammation. I actually want to buy some freezer packs to make it easier soon. They sell socks with pouches for freezer packs, even. It is this whole thing.

I also second the comment about the shoes getting broken in still, and in general things should toughen up a little with time.
[nid02gg] (score 2, diepte 1 OP) Honestly this routine sounds so good! I need to start spoiling my feet 🥹 Thank you for the advice!
[nid3bpq] (score 2, diepte 2) I forgot, also I got one of those "manual" foot massager ball things, it's like a spiky ball that is super nice to roll the foot on. But from what I understand, even a tennis ball can do the trick.
[nid7xqb] (score 2, diepte 3 OP) Oh I need that too! Making my Prime Days shopping right now!
[nibnymg] (score 2, diepte 0) You should be able to talk to your manager and get new credits for a different pair of shoes since yours isn't working for you. I'd just get a cheap pair or two though, at my site most people wear the cheap lounge looking ones that say work on the tongue
[nic2pa2] (score 2, diepte 0) Try 2 pairs of socks. Insoles. Large bandaids on heels, and other parts rubbing against shoes. Soak with Epsom salt after work. Rub Aspercreme on afterwards. Ibuprofen.
[niczces] (score 2, diepte 1 OP) I thought the restaurant life was the worst on feet... I was so wrong! Thanks for the advice!
[niczxs8] (score 2, diepte 2) I never had blisters, just felt like I was not going to make it through 10 hour days. Zappos delivered my shoes the night before training, didn't have time to break them in. Thanks Zappos lol
[nic3s9a] (score 2, diepte 0) I love the Reeboks with Floatride Energy. Very bouncy. Get some cushioned socks. Soak your feet in warm water and epsom salts. I have flat feet and I get by pretty well.
[nicz80k] (score 2, diepte 1 OP) Thank you for this, epsom salt is definitely on my list.
[nicce7q] (score 2, diepte 0) I recently went from a DS to an FC back to a DS. Alloy toed to composite toed back to alloy toed. I swear wearing composite toed shoes at the FC gave me flat foot. So happy to be back in my alloy toed at the DS.
[niclezu] (score 2, diepte 1) Our FC said we couldn't wear steal toes we have to wear comp toes. They had to many people taking their shoes off and holding up security line.
[nicmxdp] (score 2, diepte 3) Truth
[nicj5rn] (score 2, diepte 0) Get some insoles they make it easier power step pro is the brand i got from specialist recommendation they help .
[nidp9al] (score 2, diepte 0) https://www.zappos.com/p/asin/B0C35N6QJD
[nidpaen] (score 2, diepte 1) Try these they are very comfortable
[nijk1ii] (score 2, diepte 4 OP) Thank you ☺️
[nie0wik] (score 2, diepte 0) i was in the same boat when i started almost 2 years ago! i will say it is trail and error for the shoes. the last pair i got are AMAZING. i didnt even have to break them in, they were so comfy right out of the box. the first and second pair i had destroyed my feet/toes for weeks/months. a PA gave me the wonderful advice of getting compression socks too. THEY ARE AMAZING. i worked in restaurants for 10+ years and wish i had known about them then!! hang in there. it’s rough at first but since you are already heavily active i think you’ll really enjoy it! i love coming to work and working out for 10 hrs. (no sarcasm)
[nijm5jf] (score 2, diepte 1 OP) Thanks for this! I started wearing compression socks and they feel good! I'm enjoying my shifts, if I get used to the shoes then it'll be amazing!
[nie5hlc] (score 2, diepte 0) Trust me on these, game changers for me. I had the same issue as you. These are so light and easy to wear, like you're wearing nothing at all. https://www.zappos.com/product/9598532/color/3
[nie8018] (score 2, diepte 0) I feel that, i have had gout flareups a few times, large bunions and weak ankles. I once went negative UPT due to a gout flareup while working at a Delivery Station. I explained my condition to HR with physician writeup and their response was “you agreed to meet the physical requirements of the job”. That was my 2nd time having to quit Amazon. I am now on my 4th hire. I know nearly all L1 roles at FC, DS and SC. My only advice is work at a SC, the expectations are low and you can work with management to manage your foot pain in the wellness center, though I usually just power through it.
[nijncsf] (score 2, diepte 1 OP) Thanks a lot! I can only imagine how horrible that was :(
[nijjl1h] (score 2, diepte 1 OP) Thank you for the advice, I will get some soon!
[nijk43l] (score 2, diepte 2) Walmart for the socks.
[nijjq62] (score 2, diepte 1 OP) I just order a pair recommended here and I got them half size bigger :) Thank you for the advice!
[niew0n7] (score 2, diepte 0) I love the Keen Utility shoes I have 3 pair bought at various times and they’re all the same and I wear a low cut/no show saucony sock. I would recommend Epsom salt soaks, Penetrex roll on for your knees and feet, Vicks on your feet before work, and either Vicks or Penetrex the feet again at every break! Lance rhe blisters or you’ll get a hard spot that’ll flair up occasionally. Tylenol and Advil too. I can say it will get better! Oh and I didn’t order no half size bigger on shoes I ordered a 7 women’s which is what I wear in all my other shoes and they’re fit fine. I see people looking like Bozo the clown wearing shoes to big!
[nijijf1] (score 2, diepte 2) On Amazon:

Dr. Scholl's Work All-Day Superior Comfort Insoles with Massaging Gel - Designed for Men & Women with Hard-Working Feet, Eliminates Sore Muscles and Tired Legs, Arch Support Inserts with Odor Control[Dr Scholls Insoles](https://a.co/d/eqkLjHi)
[nijjg2u] (score 2, diepte 3 OP) Thank you! Ordering them right now!
[nijjint] (score 2, diepte 4) Hell yeah, hope they do you good. Definitely let me know how it feels after a week or two.
[nijg8a4] (score 2, diepte 0) I’ve changed shoes a ton. I have two pairs of insoles in mine and although we’re not longer allowed steel toes at our fc I wear mine in and my street shoes out after work to avoid secondary screening. Like clouds my shoes now.
[nijye8v] (score 2, diepte 0) If your outside toes are hurting it may be a sign that your boots are too tight. Shoes and composite toe shoes/boots run different sizes. You might want to go half a size up or wider. I have to wear the extra extra wide. So my options are limited. I also wear the black new balances. Once I broke them in they were like wearing tennis shoes. I hope it gets better for you.
[nivuent] (score 2, diepte 1 OP) Thanks for the advice! I actually been feeling like menthol or something fresh would feel good on my feet so I gotta try that spray!
[ninguzw] (score 2, diepte 0) I went to wide sizes, and mine stopped hurting. Before I changed my size in width, it was all i could do to walk after a few hours.  
I also went up a 1/2 size. 
Im so glad I messed around with the sizes.. I went to the pro timberland shoes, and they are a dream.
[niodta0] (score 2, diepte 0) Sometimes the insoles are garbage. Especially the ones with arch supports. I always hated reebok. The Georgia boot ones treated me well. Also the survivor shoes at walmart are good too
[nioe809] (score 2, diepte 1) https://www.walmart.com/ip/472595961?sid=e6d292fa-ead1-41e1-aae6-9448b0008105


These will last twice as long as any zappos pair. Just my experience
[niy2sod] (score 2, diepte 2) I also highly recommend Avenger. I had the same issue when I first started in an FC wearing low top timberland pros, I switched to a mid top Avenger shoe and my foot pain went away instantly. And as a bonus they look like basketball shoes.
[niqi10o] (score 2, diepte 0) I had this issue as well until I bought KEEN utility reno mid height composite toe.  They are very comfortable.  You can also return the free shoes you ordered and try a different pair through zappos!
[niy9psg] (score 2, diepte 0) My feet seem of but the biggest thing for me now is my knees 😞 pulling those cages and carts are the killer for the knees.
[nj5j5ox] (score 2, diepte 0) I use Skechers arch fit Leslie. These are good for moderate or high arches, not flat feet. Safety ordered them for me but not all sites do this. Then I went to a podiatrist that recommended power step insoles. The ones he recommended were too hard but then I bought powerstep bridge insoles that mold to your feet. Perfect. But do know both these shoes and insoles require atleast a week to break in. They feel uncomfortable until broken in.
[nje1hwi] (score 2, diepte 0) Always go with the extra wide and a size bigger than what you wear normally
[nib2rbk] (score 1, diepte 0) Welcome to FASCAmazon, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. We have a [Discord](https://discord.gg/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/FASCAmazon) if you have any questions or concerns.*
[nid2gxh] (score 1, diepte 1 OP) Thanks! I hope I get used to them!
[nid815e] (score 1, diepte 3 OP) I'll order it rn! It's Prime days so perfect timing!
[nid0vsc] (score 1, diepte 1 OP) A feet massage sounds like heaven right now, thanks for the advice on those insoles!
[nibfnnc] (score 1, diepte 0) The shoes that say “do the best”. I wear those and they are lightweight and very comfortable though apparently some sites don’t allow them.
[nid0ngz] (score 1, diepte 1 OP) I literally just saw an Operations Manager with those today! I'll look them up! Thank you :)
[nid0cip] (score 1, diepte 1 OP) Thank you 😊 I'll look it up!
[niczsaa] (score 1, diepte 1 OP) Thanka for the advice, I'm gonna ask for that :)
[nicznk4] (score 1, diepte 1 OP) I'm thinking about boots too, I've been told the sneakers-like are the most uncomfortable.
[nicz0rb] (score 1, diepte 1 OP) These are all good recommendations, thank you so much 😊
[nicytyy] (score 1, diepte 1 OP) Thanks for reminding me I have to buy a lotion with epsom salt.
[nie7usa] (score 1, diepte 2) No soak your feet in a warm bath with epsom salts
[nicykwy] (score 1, diepte 1 OP) I'll look for them, thank you!
[nicyj21] (score 1, diepte 1 OP) Thank you for this. I will start taking them off and wearing my Birkens to get them some rest.
(31 reacties met lagere score weggelaten)

=== THREAD k87dpt ===
SUBREDDIT: r/army
DATUM: 2020-12-07  SCORE: 75  REACTIES: 79
TITEL: I’m going to sound like a pussy for this, but are my feet supposed to hurt this much during rucks?
POST (source_id=post):
I haven’t been able to find anything on this, so just bear with me. I’m in the process of increasing my speed on ruck marches, I am super new at this and so my pace is about a 15:00 mile. But my feet, the arches especially, hurt like a mother during the whole thing and the only thing that alleviates it is doing a shuffle trot thing. And I’ve heard that’s terrible on your body. And so here are my questions. 

1: What’s supposed to hurt normally. 

2: Any ideas on why my arches hurt really bad? (It’s not plantar fasciitis because it’s only during rucking and not before or after) 

3: what can I do to increase my speed? 

And I get that my body’s not used to it yet but I’d like a good idea as to what’s normal or not.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gewgv76] (score 108, diepte 0) >It’s not plantar fasciitis because it’s only during rucking and not before or after

It probably is. It doesn't happen when you aren't rucking because it's the additional weight that's causing it. Get boots or insoles with more support.
[gewiden] (score 56, diepte 0) First off, no one actually walks a ruck at a 15:00 pace. That type of speed just creates a weird gait which is why your feet hurt so bad. 

The only way to ruck a sub 3 hour 12 mile ruck is to airborne shuffle on and off.
[gewiyk9] (score 41, diepte 2) Slow down your actual walking and just accept the fact you're going to have to run some of it to make up the time lost.
[gewg7mu] (score 34, diepte 0) Have you tried rolling or stretching at all prior to stepping off?
[gewhydl] (score 28, diepte 2) That’s your first problem
[gewg67c] (score 21, diepte 0) Just keep rucking. Embrace the succ. Maybe some new insoles
[gewgio4] (score 19, diepte 0) 1. Your feet are going to hurt but not be excruciating so that’s definitely not normal.

2. Do you do heel to toe when you step? Either way I’d talk to your provider and get some input, I know some posts actually have specialists that can help correct bad running/rucking form.

3. Only way to get better is to ruck more. However, definitely get your shit checked out before it turns into something more serious. Much better to waste a few mornings at the aid station than to permanently fuck up your legs.
[gewx4bd] (score 18, diepte 1) Uh excuse me, 6’ all legs gazelle master race checking in. Straight power walking the whole way gets me a reliable 2:50-2:55, it’s what i used when I didn’t want to try.
[gewqw5e] (score 16, diepte 2) I can walk a 2:45 12 mile without any running. My legs aren't abnormally long, in fact I'm on the short side for males. You just have to put miles on your feet. And alot of them. Once a week doesn't do much for most people. Make sure you gradually increase weight and distance to let your body acclimate. Most people who claim they suck at rucking do everything they can to avoid it, if you want to be good at it, do it. Alot.
[gewigd0] (score 15, diepte 1 OP) So slow down a little bit?
[gewvhme] (score 13, diepte 2) Can confirm; had some pretty bad plantar fasciitis and thought it was just another sore muscle, fast forward a few months and I could hardly stand up in the morning. From what I understand the onset can be different for people but it typically starts out as DOMS and then its like it snaps, like a rolled ankle and then you're kinda stuck with it for 6-12 months. Do yourself a favor and stretch, KT tape and don't over-exert yourself
[gewh9s2] (score 11, diepte 1 OP) No only after.
[gewjx0z] (score 10, diepte 0) Not saying this is your problem but it might be. I have really flat and wide feet. How I keep my feet comfy: 

1) I religiously wear superfeet green or orange insoles. These give tons of arch support. I only get footwear that fits them. (These also come in handy when you only have wet boots and change to dry socks - throw in a dry set of dry insoles and it makes a world of difference)

2) Get aftermarket (non-issued) boots with solid reviews if you haven't already. When shopping look into if the "wide" sizes fit you better. If your boots have worn a good bit or have super lightweight soles, you might not be getting the support your feet need. 

3) Experiment with how tight youre lacing your boots. 

4) Get some good or at least decent socks. Merrill socks on expertvoice.com can be a hidden gem.

5) I've recently started doing more calf raises and agility ladder exercises and it's helped with my foot issues - mostly issues caused by a foot injury a few years ago, not with the flat foot thing, but I can't imagine it'll make things worse. 

&#x200B;

Best of luck. Rucks suck. There are a lot of tips tricks and techniques that can help. Find smart NCOs and ask them for pro tips.
[gexo5up] (score 9, diepte 3) As a short guy I hated when taller dudes would walk past me saying some shit like "sTeP iT oUt BrO". My legs physically only can go so far compared to yours, chill out.
[gex3mwz] (score 9, diepte 0) I’m a medic with a background in strength and conditioning/athletic training. There’s a lot of comments on here and you’re getting all sorts of wonky and negating feedback. 

This does sound like textbook plantar fasciitis. The true, unpopular opinion is that your feet are weak and instead of babying them by wearing better arch support or insoles you need to slowly strengthen them. 

Rucking is not something you need to do more to get better at. Run more, do more unilateral leg work (i.e. step ups, pistol squats, lunges), and make sure you’re taking care of your body. Stretch, roll out, sleep, eat well, drink plenty of water. 

First thing to do is recover. Take some time off from running and rucking while still rolling out/stretching to let your feet heal. Then start slow and build your feet back up. 

Warning: going to a doctor will probably result in them telling you to get inserts or better arch support because their job is to get you back in the fight as soon as possible. That’s not the long term solution. Strengthening your feet is the long term answer to having healthy feet for the rest of your life.
[gewjfsv] (score 8, diepte 4) Roll everything from your hips down, with whatever you think would work for you
[gex2whg] (score 8, diepte 3) I finished a 12 mile in 2:49 recently. I ran most of the first 2 miles (I finished the first 2 at 22 minutes). I then ran 3 light poles and walked 2, then slowly increased the walking distance to where by mile 9 I was walking 4 and running 2.
[gex9wm2] (score 7, diepte 2) Checking in from the 6'6" altitude and can confirm, never run under load.  Sup 3 hour is easily doable.
[gewhgmo] (score 6, diepte 0) Step 1: check your footprint on one of those machines that determines your arch and buy the correct insoles.  Idk if your case will be like mine, but I was given free insoles from the PA. 

Step 2: buy boots that fit properly. You probably think your boots fit well now; but check out some others. Once I found the boot I like, I haven’t bought any other brand or style in nearly 5 years. 

Step 3: break in boots on shorter rucks, no more than 4-8 until they are nice and comfy. You’ll get some hotspots on your feet the first couple times. That’s normal. 

Step 4: continue to train your body and increase that time! 

I had this same issue. Now, the only part of me that hurts DURING a 12 mile ruck are my shins. And that’s only in the first mile or two. Arch pain isn’t something that just toughens up. You need the correct fitting soles and boots.
[gewh0up] (score 5, diepte 1 OP) Yeah that’s what I was thinking, and yeah I step heel to toe. And that’s what I thought but it’s never gotten better so I’ll take a trip tomorrow and get it checked out.
[gewi3k4] (score 4, diepte 3 OP) Okay, so things like rolling my feet on a lacrosse ball and that kinda thing? Or what do you recommend?
[gewheyb] (score 4, diepte 2) Yeah, I don’t fuck around with my feet. I got DQ’d from joining the Army initially because of real bad issues with Plantar Fasciitis, collapsed arches, etc. Listened to the docs, did the physics therapy and more then a decade later I’ve made it through several selection courses and foot issues are in the rear view mirror.
[gewhevc] (score 4, diepte 2) As other have said, take care of your body. You’re not a pussy for listening to your body and trying to get better.
[gewrbmy] (score 4, diepte 3 OP) Okay, I’ll get on that and yeah I enjoy rucking. I just don’t understand why my arches hurt so bad. And do you do short quick strides? Or longer strides? And thanks that’s awesome, I will get better it’s just a matter of finding out why I suck right now. Thanks
[gexqp57] (score 4, diepte 1) > Joe Rogan talks about it all the time and has had some great guests talk about it as well.

hey Jamie bring that up
[gewgsbv] (score 3, diepte 0) Better boots or insoles. If you go to a fancy shoe store they can fit you for insoles.
[gewwfyy] (score 3, diepte 3) Ah fuck this sounds like what I’m going through right now. Is it normal for it to happen in just 1 foot?

Basically I jumped into a 12 mile ruck March about a month ago after being hurt for a while. I could hardly stand the next day. Now the pain in my foot will come and go. Sometimes I can start a workout while it hurts like hell, then after 20 mins or so it’ll feel perfectly fine. Other times I’ll start a workout after it’s felt good for a week and it’ll start to hurt.

At first I thought it was a stress fracture but it feels too low in my foot for that.

Also u/DryTrumpin I’m curious if these symptoms sound familiar.

Edit: I should add that it hurts in my arch but on the outside of my foot.
[gewhsrm] (score 3, diepte 2) Hotspots are areas that are rubbing and will become a blister. Aka hot spot. Friction causes the blisters
[gewv3a2] (score 3, diepte 1) I can walk up to atleast 8 miles under a 15:00 pace. It simply uses different muscle groups. I do it specifically to train those groups so that between my shuffles on times rucks, I’m not “losing” as much time on the walk. 

This is not what’s screwing his feet up. Based on my own experience I would say plantar fasciitis. Oddly enough my feet hurt MORE using custom insoles but I found off the shelf inserts work great. I haven’t had serious foot pain from rucks in years that wasn’t caused by abnormally heavy weights or long distances. Sometimes the perfectly sized rocks can cause pinpoint pressure on the arches of my boot sole is flexible enough but otherwise, OTC inserts work best for me. Earlier poster is correct though, rolling out arches before and after rucks will go a long way in alleviating the pain.
[gexlfdy] (score 3, diepte 1 OP) This is one of the answers I was looking for, thank you and yeah I’ve been working on that but I’ll do it better now! I appreciate it
[geygqat] (score 2, diepte 4) You’ll learn to realize that proper warm up and recovery is crucial for longevity, especially in the army my dude.

Don’t be one of those guys that says you don’t need to stretch because you’re young. Do your body a favor now rather than later
[geypqvm] (score 2, diepte 5 OP) I always stretch. And I always warm up. I understand it’s verrrry important. But yeah I’m glad that I’m learning it now than later
[gey83hs] (score 2, diepte 5) Yeah reading these comments made me do a little more research, apparently it’s unlikely for me to get pain where I have it from Plantar. Yeah I should probably get it checked out, I just hate doctors. Anyway, thanks for the help.
[geybupg] (score 2, diepte 5) Honestly it doesn’t really hurt specifically in the morning, some days it just hurts some days it just doesn’t. But usually I can go long stretches of time without it hurting and if it does hurt it’s the day after a workout. The pain is also a little further up than that; I’d say below my metatarsal but above my heel. It’s also on the outside of my foot which, from the little bit of research these comments spurred me to do, doesn’t seem like that’s the common place for Plantar. Tbh I think it may be a different tendon/ligament down there.

In any case, I appreciate the concern and I should probably just see a doctor lol.
[gf0kzcw] (score 2, diepte 4) This could be cuboid syndrome or a stress fracture. I think I may have one of these issues or plantar fasciitis. I addressed it in my other post and it resolved itself after a few weeks of stretching, NSAIDs, and avoiding cardio, but who knows? It might come back. I hope not though...
[gf0km20] (score 2, diepte 2) So I just dealt with a bout of plantar fasciitis (maybe cuboid syndrome, but not too sure). It came on extremely rapidly, after one long, slow run. I was almost unable to walk or stand for most of the day. It was excruciating, to the point that I would collapse almost in tears just from standing up or trying to walk.

I did stretches for a few weeks, along with rolling my arch on a frozen water bottle twice a day followed by soaking my foot in nearly-scalding water and Epsom salt. I avoided all cardio and walked crooked to avoid putting pressure on the affected foot for 3 weeks, then walked a few miles on the weekends for 3 more weeks.

It got better because I recognized the issues quickly and immediately took steps to fix it. Oh, and 1-2,000mg of ibuprofen every day helped too (sorry liver).
[gewgz9n] (score 2, diepte 0) Run more. Rucking puts way more strain on your cardiovascular system. Get a solid base mileage of 30 to 40 miles a week. Start introducing weight progressively.

Id see a doctor about your arches hurting. Are your boots too small? Almost sounds like your foot is being compressed forward if you have to shuffle to stop the pain.
[gewkeq5] (score 2, diepte 1 OP) Right on,  that’s encouraging. Thanks for the help I appreciate it. Ans I’ll look into those insoles. And I think tomorrow I’ll go see a foot doc.
[gewvski] (score 2, diepte 0) Well, it isn’t a requirement to pass a ruck march, so just do what feels comfortable until you’re supposed to do a “record” ruck, then just go to sick hall the week before and get a 2-week dead man’s profile (you’ve already got the plantar fasciitis, now you just need a signature).

All jokes aside, take care of yourself. I had a drill sgt tell me to never run while carrying a ruck unless it’s life or death. Years later, my company was having us do ruck pt with 35% of our body weight, which for me was close to 74 lbs. There’s training, and then there’s flat out damaging your body on purpose. The only one who’s going to have to live their whole life with shot joints is you, not your NCOs telling you to do sprints with a ruck.
[gewx793] (score 2, diepte 0) Do you use aftermarket insoles? The brand you want is Superfeet. They come in bright neon colors, you want the orange ones if you can find them, green if you can’t.
[gewyxtl] (score 2, diepte 0) If you’re not in selection or some sort of meaningful competition don’t ignore the pain you have. The people telling you to suck it up are idiots, you only get one body and pain is a sign something is going wrong so you need to address it. Im not a professional but I’ve listened to professionals and have gone through the same pain.

1. Make sure you gradually increase the distance you are covering. I think the rule is is no more than a 10% increase each week, but I’m not sure so search it up. Your body needs time to acclimate.

2. You have to strengthen your feet. Run barefoot in the sand, run in tennis shoes with very little cushioning (google “minimalist running shoes” or get the vibram FiveFingers and make sure you work up to them so your body acclimates), alternate between boots and tennis shoes when rucking. Pay more attention to where you step when wearing tennis shoes.

3. The whole “this is your foot type and run type, here’s a shoe/insole” is marketing bs that treats the symptom from walking/running incorrectly rather than fixing the problem; there is one proper way to walk and run. Look up some stuff on YouTube and learn how to properly walk/ ruck/ run. Joe Rogan talks about it all the time and has had some great guests talk about it as well.

Good luck and I hope your feet get better.
[gexlku2] (score 2, diepte 1 OP) I agree, I’ll check out Joe Rogan and ha yeah I just ordered some barefoot shoes because I live in Minnesota so it’s too cold to run true barefoot. I appreciate the advice man.
[gexuxdr] (score 2, diepte 0) sure sounds like the start of planter facitis.

Old guy here.  I knew i had flat feet when i joined but didnt know why it was thing that folks with flat feet get screened out.  I learned later it might have something to do with folks with flat feet more often getting planter facitis.  I reget that the the guy next to me stepped forward when the dr at meps pointed our general direction at the flat foot screening. I should have. I knew he was pointing at me but the kid next to me seemed eager to have a reason to be rejected.

Take care of that shit now.  give them time to heal,  do the little things you can find to help them heal and stay away.  

at 52 i sometimes have days getting out of bed and walking to take a piss might as well be running a marathon.  slow and painful. 

take care of that shit now op.  it wont go away all on its own.
[gexwv55] (score 2, diepte 1 OP) Where in the shins is your pain? Look up shin splints, and then click images and it’ll show you where shin splints pain is associated at. Sounds kinda like shin splints to me.
[gex3d9p] (score 1, diepte 4) Take a barbell end, or kettlebell and literally mash your muscles with it.
[gewgafh] (score 1, diepte 0) So your feet are definitely not supposed to feel that way, I’d recommend you listen to your body and immediately stop rucking and go see a doctor before you make whatever is bad worse.
[gewgwhv] (score 1, diepte 1 OP) Alright good point.  I’ll make a trip tomorrow, thank you!
[gewhs0d] (score 1, diepte 3 OP) Sweet, any exercises you recommend?
[geyacqt] (score 1, diepte 4) You sound like its already developed, does it hurt worse in the morning, when you wake up? The pain is usually worse after exercises and after wakeup. The main identifying factor is the location of the pain, it should be on the bottom of the foot, at the front of the heel bone. This is a muscle that attaches the front portion of the base of your toes to the heel. It has a lot of pressure exerted on it and it typically needs to be warmed up, its why the first few steps in the morning will hurt the most and without cooldown stretches, will leave it throbbing after a workout. Its a fairly common problem, also called policeman heel, not to say the pain can't be really bad. It takes a few months to heal and you'll have good days and bad days. I'd recommend compression socks or one of those socks that hooks into itself while you sleep, they help a lot. Do stretches (the rear lunge, towel drills and a million others), get fitted insoles for your boots/shoes, I'd recommend taking something over the counter for the pain when you can't avoid exerting it.
[gf0lhxr] (score 1, diepte 5) Yeah I’m honestly hoping it was my initial guess if a stress fracture- just feels a little low for that, but I’ve fractured my feet before rucking so it wouldn’t be a first. Honestly, there are still good days and bad days as far as pain goes but the bad days don’t feel as bad as a few weeks ago. I’m hoping that’s a good sign.

Just sucks because this year has killed me health wise and I’m in pretty shit shape because of it, but I branched IN a couple days ago and all I want to do is get my 5mi time back to sub 40.
[gewh7tv] (score 1, diepte 1 OP) For this ruck I was wearing Tennis shoes because the boots weren’t working so I switched it up to see what changes. And the arches still hurt. And I’ll run more then, and okay will do.
[gewho35] (score 1, diepte 1 OP) Will do, and what are hotspots? And alright I’ll get that done then thanks!
(27 reacties met lagere score weggelaten)

