# Label-batch batch_0115

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
Schrijf het resultaat naar `batch_0115.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 5p0cgs, 1mqfm26, 1ibk8et).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 5p0cgs ===
SUBREDDIT: r/Fitness
DATUM: 2017-01-19  SCORE: 459  REACTIES: 110
TITEL: I thought putting together a Beginner's Equipment Guide might be helpful. Belts, wrist wraps, knee sleeves, and weightlifting shoes.
POST (source_id=post):
Lately I've noticed there's been a recent upswing in posts about equipment used for lifting and with that a lot of questions regarding on when to start using a piece of equipment, what the piece of equipment does exactly, or if it that piece of equipment is even necessary for ones goals. A lot of this is my opinion based on my experience so please take what I say with a grain of salt, I'll try and be objective where I can. 

Hopefully this can be a bit of a guide to newer lifters looking to improve their training through the use of equipment.

A bit of background on myself: I'm a powerlifter. I've done both equipped (multiply and singleply) and raw. I'm not the most knowledgeable, but I think I know a bit seeing as I've used and competed with almost every piece of equipment under the sun. I'll try and provide links to back up what I say and hopefully be as thorough and concise as I can.

#Belts

This one is fairly common and it was the first piece of equipment I bought.

*  **What do belts do exactly?**

First, I'll say what belts aren't intended as: safety implements. Using a belt will not mitigate your chance of injury, at least not by a significant degree. Belts are performance enhancers. They increase your intra-abdominal pressure and to put it simply, they allow you to lift more.

https://www.ncbi.nlm.nih.gov/pubmed/10619094

And contrary to common gym myths, EMG data shows that they might actually increase core activity.

* **Do I need to wear a belt?**

Nope, it's 100% personal preference. However, if you plan on competing or train primarily for strength I'd say that you're doing a disservice to yourself for not using one in the long run.

* **When do I need to start using one?**

There isn't some threshold you have to reach before you can use a belt. There are plenty of lifters I know that started off lifting with a belt and some that had 1000+ totals before they even touched one. However, it is a tool so there is a learning curve for some people. Learning how to properly brace ("push out" w/ valsalva technique) with a belt is different than bracing without one.

* **When should I wear one in training?**

Rule of thumb for me is the big three or other compound movements where intra-abdominal pressure will aid you in performing the lift. Some people don't like using a belt for certain lifts like the deadlift and bench. However, these are the most common instances where a belt is most likely to aid you. 


*  **Which belt is right for me? Where do I get a belt?**

Belts come in varying sizes and shapes. And again, most of this is preference. I think for the average person a standard powerlifting uniform width belt is good enough. However, if you're a smaller person with not a lot of torso real estate a tapered belt or a smaller uniform width belt will do as well.

[Inzer](http://www.inzernet.com/search_results_belts.asp?txtsearchParamTxt=&txtsearchParamCat=8&txtsearchParamType=ALL&txtsearchParamMan=ALL&txtsearchParamVen=ALL&txtFromSearch=fromSearch&iLevel=1) is fantastic and affordable for people in the US and Canada. They come in 10mm and 13mm thickness, double or single prong, lever, or ratchet. Honestly, 10mm and single prong is perfect. 10mm conforms to your body more easily and dual prongs don't do much in my opinion. Lever belts are popular too, but they lack for those who like to change tightness for different lifts.

Other resources for belts: EliteFTS, Wahlander (Europe), BestBelts, SBD, Titan, Rogue.

I paraphrased and borrowed some things from the [Strengtheory article](http://strengtheory.com/the-belt-bible/) on this for this section since Greg is a great resource for stuff like this as well.

#Weightlifting Shoes

I've seen a lot more posts about these as tools for squatting. For the uninitiated, weightlifting shoes are designed with usually a 3/4" inch heel of hard material. They provide a steady, stable base for weightlifting and reduce the dorsiflexion requirements for catching in either the snatch or the clean and jerk and reduce the flexion requirements for the hips. Basically, they help you stay upright when you're in the hole. 

https://www.ncbi.nlm.nih.gov/pubmed/27096286

Weightlifting shoes for squatting are a great tool, I use them myself. However, when introducing a new tool one must learn how to use it and what its purpose is in your training. 

For starters, being a high bar squatter does not necessitate the need for weightlifting shoes, nor does being a lowbar squatter nullify you from the benefits of a raised heel. In reality, high bar and low bar are really not very different and there are plenty of lifters of both varieties that use or do not use weightlifting shoes. 

I've seen a lot of people on here use their ankle flexibility as a limiting factor for their squat, but in reality the dorsiflexion requirements for a full squat (hip crease below parallel/top of the knee) is not all that drastic and often times there are things that may LOOK like poor ankle flexibility, [but are caused by other factors like weak quads or hip stability issues.](https://www.ncbi.nlm.nih.gov/pubmed/27096286)

This is where I put in a bit of my own personal opinion on the matter: I do not think beginners need weightlifting shoes right off the bat. I don't think they could hurt, but there are tons of things one can do in their training to try and fix and get better at the movement without necessarily sinking money and time into an implement that might not even help. Remember, training is a marathon and it's not plug and play. Experiment with things and find what makes you comfortable before deciding that you need something like weightlifting shoes. 

But, this is personal preference, if you can justify it certainly go ahead and experiment. Just know there are multiple solutions that don't involve equipment in this instance. 

[Wei-Rui](http://www.maxbarbell.com/collections/vendors?q=wei-rui) make a decent affordable weightlifting shoe if you're looking for a cheaper, but quality option. And even if you find that your technique is better (which is ultimately what matters) with flat soles, you can always use your heels to bench in to get that better arch!

#Knee Sleeves

These are tight fitting sleeves made of varying thickness neoprene or polyester-material.

Again, I must stress that these devices aren't intended to be used as safety devices. They're for comfort and performance. Knee sleeves aren't meant to be used as a safety device. You should consult your doctor before using these to squat in if you have preexisting conditions.

As far as I know there isn't much research on what exactly knee sleeves do in empirical terms and most people will have a different opinion about them. However, in my personal experience and the experience of other lifters I know knee sleeves keep joints "warm" and comfortable while squatting and likely produce some sort of elastic assistance in the bottom of a squat. 

These sleeves run the gamut from very thick, very tight SBD sleeves to looser fitting Rehband sleeves to very thin Hookgrip sleeves. Again, this is all preference. Some people dislike the tight thick SBDs and some people can't squat without them. It all depends on what you want out of the product. Top performance and elastic boost? SBD. Warmth and comfort? Rehband or Titan.

I firmly believe that trainees from beginner to advanced can benefit and use these. There's even some evidence that [knee sleeves bracing property helps trainees with proprioception](https://www.ncbi.nlm.nih.gov/pubmed/18469568). There's not a learning curve like with a belt or shoes. 

Each brand tend to have their own sizing charts so be mindful of that when purchasing, and measure accurately for a good fit. 

 
#Knee Wraps

EDIT: Decided to include these just to clarify what the main difference is between knee sleeves and knee wraps are for beginners. Knee wraps are 100% a performance booster. The idea is to wrap your knees tightly with tough elastic-fabric material to give yourself a boost at the bottom of a squat. The energy is stored as potential energy in the elastic as you descend in the squat and released as you start the concentric portion of the movement. 

Knee wrapping is very much a skill and can add some serious poundage to your lift. To many lifters, knee wrapping can be very uncomfortable if done correctly. My legs have turned blue from wrapping. 

I wouldn't recommend this equipment to beginners as it does change the groove of the lift and has a somewhat steeper learning curve as far as how to wrap and the technique used to squat in wraps. But, if you want to try it, go ahead! There are plenty of tutorials online on how to wrap knees correctly. [Chris Duffin did a thing with SuperTraining that's pretty informative](https://www.youtube.com/watch?v=p_MaCT0RsFo). As always, be careful and listen to your body!

https://www.ncbi.nlm.nih.gov/pubmed/22995993

#Wrist Wraps

These are elastic material wraps of varying lengths. Most people use these for pressing movements like the bench and OHP; however, I have seen people use them for deadlifts due to the constricting property's effect on grip. It's often common to use them while squatting for added wrist support.

The most common use is to prevent ones wrist from cocking back while benching or pressing and to aid the wrist joint (probably one of the most unstable joints in your body) in stability. Keeping your wrist straight is a more efficient way to bench and helps prevent cumulative strain on the joint.

Necessary? Not totally, but absolutely helpful even if strength isn't your main goal in training. 

Titan sells cheap, good quality wraps. As for size: again this totally preference, but the smallest option for most wraps is 12" and I can barely get that around my wrist once. I have fairly large wrists, but I'd find that most guys would be hard pressed to get that wrap tight. I would size up to 19.5" or 24". However, if you have smaller wrists the 12" might be perfect for you.

The goal with these is to wrap them TIGHT. I personally always wrap out and in a casting motion.

#Wrist Straps

I don't use these very often in my training, but plenty of strongmen, powerlifters, bodybuilders, and regular fitness enthusiasts do. 

These are straps that have a loop for your hand and wrist to fit into and a long excess that's meant to be wrapped tightly around the bar. This takes grip out as a factor for pulling exercises like deadlifts, shrugs, and rows. These are a great tool to dump more volume into your training, but reduce the wear and tear on your grip.

I often see people concerned that this training implement is a crutch and will cause your grip to lag. I'll say that one thing people should keep in mind with lifts like deadlifts and rows aren't performed to train your grip solely per se. If grip is a concern for you, do isolated grip training. 

Are these necessary? No, but they can be helpful when you feel that you're capable of more than what your grip is offering up.

#Conclusion

If you haven't noticed, most of these are entirely preferential and what works for one might not work for another. However, these devices should be used with the idea that they're used as a performance enhancer. Trying new things is what lifting and training is all about. As I said in the beginning, this is all very much backed up by my personal opinions so if anyone would like to call me out on something they disagree with go ahead. I just meant this to be an open guide from someone with experience on what equipment does. I know that it can be daunting when one thinks they have to purchase all this equipment just to lift.

I left out things like ~~knee wraps~~ and things like briefs (and obviously other powerlifting gear) because I didn't think that was equipment that most beginners would be using. However, if anyone would like to see a similar guide about knee wraps or other implements let me know.

#links

http://www.andersonpowerlifting.com/ (titan and SBD supplier) https://titansupport.com/ http://inzernet.com http://howmuchyabench.net (Mark Bell's equipment) http://elitefts.com

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dcngoax] (score 61, diepte 1 OP) how do you know how to pluck my strings so tenderly
[dcngnag] (score 48, diepte 0) But isn't this geared powerlifting? What if we're interested in raw lifting only? I don't want to have to have to train with a group.
[dcnljdy] (score 33, diepte 0) Maybe add that flat soled shoes are better if you squat wide. And that tights improve your deadlift by accentuating ur butt
[dcnf8ux] (score 22, diepte 0) Super informative - much appreciated!
[dcnjdr1] (score 19, diepte 2) I'm in your house
[dcniv7p] (score 17, diepte 1) the Spud belt is not IPF approved.


This is not a drawback, it's a selling point.
[dcnj6on] (score 10, diepte 2 OP) tfw bestbelts aren't either anymore
[dcnlf1p] (score 9, diepte 1) Levers are easier to put on and take off, but annoying when you have to adjust. Just pack a flathead screwdriver if you get one.
[dcnhx9u] (score 7, diepte 0) Donde esta my Spud Inc Deadlift belt, aka "The Only Belt You Ever Need," aka "The Belt That Gets Fat With You?"
[dcnsr37] (score 7, diepte 3) If you want a middle ground between the two check out a quick release belt.

You put it on like a prong but take it off like a lever, which is nice after a heavy set.
[dco98bg] (score 7, diepte 1) Tights only count if you pull sumo.
[dcnmr7g] (score 7, diepte 1 OP) This brings up a point I didn't even think of: I don't recommend leaving wraps or belts on in between sets. 

Your wraps should be tight enough that it's relatively uncomfortable to have on. And the same should be said about your belt as well. Always readjust before sets.
[dcnflzn] (score 6, diepte 1 OP) Thanks for reading! Glad I could help!
[dcns4lf] (score 6, diepte 1) SBDs. Nike Romaleos.
[dcnkhfv] (score 6, diepte 1) Are knee socks not enough?
[dcnpdn4] (score 6, diepte 2) Long pants work for me on deadlift days, except when I groggily think it's squat day and grab shorts to my eventual chagrin.
[dco4zfg] (score 6, diepte 2) Weighing in on this too. I have a lever and wish I got a prong. As convenient as it is to have a lever when I do need to change it I'm sitting on the floor for 5 minutes with a screwdriver getting extremely pissed off.
[dcnhsbg] (score 5, diepte 0) Nice write up dude. 

I agree with you that other gear isn't really appropriate for beginners, but it might be worth including a brief description of knee wraps just below knee sleeves because a lot of beginners have no clue that there's a distinction between the two. I frequently get asked about my "knee wraps" when I wear SBD sleeves at the commercial gym I train at. And I see confusion between the two on this sub all the time.
[dco08d3] (score 5, diepte 2) Metcons are good training shoes but they aren't weightlifting shoes. The heel isn't as high. OP, if you're looking for shoes that will help your squat, Nike Romaleos or Adidas Adipowers are what you need.
[dcocc7v] (score 5, diepte 3) I'll take 5 minutes of sitting on the floor every few months over getting damn near stuck every time you use a prong any day.
[dcni1js] (score 4, diepte 1 OP) I can do that!
[dcok6ol] (score 4, diepte 4 OP) They're good belts for sure. But, IPF is pay to play, my dude.
[dco5jsy] (score 4, diepte 4) Its interesting that you got downvoted for saying you don't need weightlifting shoes for your squat, and you have a 600lb squat.
[dco8zh0] (score 4, diepte 3 OP) Unless you're a weightlifter, one doesn't need weightlifting shoes to squat. I said this explicitly in the guide and gave reasons as to why using WL shoes were entirely preferential.
[dcnu2qz] (score 4, diepte 3) Wow this. Goodbye to the hair on my shinny shin shin
[dcoc6bm] (score 4, diepte 2) Now ill have you know that tights also bring out the dick when conventional pulling
[dcnoiu8] (score 4, diepte 0) Nice post! I'd like to hear your thoughts on elbow sleeves.
[dcnfnb1] (score 3, diepte 0) This is good stuff man.  Wanted to agree that the inzer 13 mm forever lever is a great belt.  Also for wraps Nordic lifting makes good cheap ones that work well in the gym.
[dcopur2] (score 3, diepte 3) I smell sitcom!
[dcnhwhf] (score 3, diepte 0) Nothing on Straps? I recently decided to pickup a pair of straps that double as wrist wraps and was amazed by the results they gave me. My heavy deadlift day is towards the end of the week at which point my grip strength is pretty exhausted so as much as I can grip the weight I'm pulling its burnt by the 2-3rd heavy rep. Last week strapless I pulled 112.5KG for 3 and was really disappointed as I felt I wasn't pushing myself at all but my grip was exhausted so I couldn't keep pushing, my first deadlift day with straps was yesterday and I pulled 115KG for 8 and I still had grip strength to do my drop sets with good form. If you're not training to compete raw I see no reason they can't be used given other grip work in your routine/program.
  
Edit: Also nice write up
[dcnkaec] (score 3, diepte 2) http://versagripps.com/versa-gripps
[dcohs1y] (score 3, diepte 3) Wait, seriously? Why? 

My Best is no different than any Inzer or Rogue belt I've seen.
[dcnipe0] (score 3, diepte 0) recommend any good sleeves and shoes?
[dco9sxj] (score 3, diepte 5) People who didn't even read the OP
[dcnjx3y] (score 3, diepte 0) Great post, particularly the section on weightlifting belts which I think is spot on.

Another piece of equipment I often recommend - even to beginners - are the RockGuards shin protectors. They're not necessary for everyone, but if you have the type of body where it's nearly impossible to deadlift with proper form without scraping and bloodying up your shins, these things are a godsend.
[dcnjzs6] (score 3, diepte 0) Thanks for the write-up. Can anyone recommend places to source gear, especially shoes, for Canada?
[dcnkas6] (score 3, diepte 1) amazon.ca
[dcocafj] (score 3, diepte 3) Yeah I guess it really emphasizes the hump the bar at lockout cue.
[dcocib6] (score 3, diepte 1) I have a set of EliteFTS heavies I wore the velcro out in... 4-5 years. I think that's an acceptable time frame for a new set of wraps. I only use them for my heavy sets and don't bother with them for warm-ups or anything under 300 really.
[dcnr3lx] (score 3, diepte 0) I also use my wrist wraps for low-bar squatting. I don't have great mobility so I like having some support to keep my wrists from getting beat up.
[dcnu2bu] (score 3, diepte 0) I'd also like to add you can go to an REI and buy a block of grip/climbing chalk for like $2. It usually lasts me like 2-3 months.
[dcob1wb] (score 2, diepte 1) I've used Nordic wraps/straps for the past 3 years and love them. I recommend them!
[dcnl5m4] (score 2, diepte 2) These http://www.rebelsport.com.au/Product/Sting-Power-Pro-Lifting-Straps/456002
[dcovauc] (score 2, diepte 1) People shit on straps all the time, but when you're lifting really heavy a weakening grip affects the form of your whole body. If you are working out every day your grip is going to be worn out when you do deadlifts. Personally I notice my form gets worse (rounding back/shoulders) at around 70% of my 1RM when using a double-overhand grip, and even with a mixed/hook grip it gets messy around 90%.

Straps allow you to continue to train deadlift heavy and use your grip every day for other movements. When attempting a max pull just cycle off heavy exercise every day so your forearms have a chance to rest and recover before you go for a max raw pull.
[dco240d] (score 2, diepte 3) You don't need weightlifting shoes.
[dco9vh1] (score 2, diepte 6) Yeah but did you do it for reps at ATG high bar literally naked no gear but squat shoes? I thought so
(76 reacties met lagere score weggelaten)

=== THREAD 1mqfm26 ===
SUBREDDIT: r/weddingplanning
DATUM: 2025-08-14  SCORE: 60  REACTIES: 98
TITEL: Cold feet vs wrong person. How do you know?
POST (source_id=post):
I’m having a serious life dilemma and I’m unable to come to a decision on what to do.


Been with my fiancee for 8 years. We’re both 30 so since we were 22. Have been living together for 6. 3 different states, Covid, life experiences - we’ve been through it all.


I proposed last year and after initial excitement I’ve been nothing but terrified. Day in and day out I’m questioning everything - if we’re right for each other. Over the 8 years we had one “break up” that lasted 2 days. But even then I was never questioning things like I am right now. Each vendor we lock down, each payment we send - the pit in my stomach grows more and more.


We’ve openly communicated about all this and for the last few months it’s just been us sort of going through the motions with nights of crying. I’m a pendulum going back and forth between let’s do it and this is a terrible mistake.


Few notable items - I have a history of backing down after making major life decisions, recently moved to the city where almost all my friends are single, this questioning has been going on for 6+ months now, I do often find myself fantasizing about single life. 


So I guess the questions are - How can I tell if this is just cold feet? How do I take sunk costs of the decision? Is this just grass is greener syndrome?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n8qh55a] (score 274, diepte 0) I’d suggest some personal + couple’s counseling to talk through your feelings. If you’re usually kind of flaky/non-committal/prone to panic over big decisions, it makes sense that that would come into play here and some therapy to work through that seems beneficial for this relationship and your life in general. It’s hard to know as a stranger if this is a you problem or a relationship problem, but I’d frankly pause wedding planning until you figure it out. Losing some deposits is ultimately a lot easier and cheaper than a divorce.
[n8qjw1d] (score 237, diepte 0) I don't know you or your FI, but in her place, after hearing what you've said, there would be no wedding, sunk costs be damned. The nights of crying would be a dealbreaker, too. It's not supposed to be this hard. 

From your point of view, I think you obviously need counseling, but it sounds like you aren't going to get the chance to delay the decision. From her POV, either you know her and your own mind by now or you don't. If you aren't sure, then you're making a decision.
[n8qyvhj] (score 185, diepte 1) this is kind of where I’m at….in her shoes, with a wedding to the man I love and have been with for 8 years fully planned and only 4 months away, and he’s seriously not sure about marrying me?? that says all I’d need to know. she deserves not to be someones sunk cost, or regret, or path of least resistance, she deserves to be someone’s, “I can’t believe I’m so lucky to marry this girl!!!”
[n8qhoxx] (score 83, diepte 0) Have you talked to a therapist? What are the actual compatibility issues? What do you want in a partner?

There is relationship OCD which can be constant thoughts about whether you’re with the right person. 

It helps me to recognize one partner won’t have everything. But I’ve been doing life with my partner day by day, and we’re happy. Are there things we wish eachother did differently? I’m sure. But we enjoy each other’s company, care for eachother deeply, and are good at “doing life” together.

This works for us. If what’s missing for you is some indefinable “spark”, I think you’ll be chasing that forever. Most couples therapists advise that sparks fade, what endures is the deep compassion and caring.

Just one girl’s opinion.
[n8qjumx] (score 72, diepte 2) I’d book your therapy appointment for next week. Start sending out some emails to potential therapists today. Psychologytoday.com has some filters and good profiles to review, or you could try a telehealth platform like BetterHelp.

The only solution here is to take action now… and you’ve been trying to figure this out on your own, you need a professional.
[n8qqv8y] (score 62, diepte 2) That's understandable but you're 30. Your friends are all going to partner up soon if they haven't already. If you want kids and meet women around your age, your next timeline is just going to be advanced a lot faster than it is now. You're reaching the point in your life where for many your circle starts to turn inward more and you focus on your nuclear family while still keeping up and having friends. 

I think you might want to consider some therapy to talk these things out if you just have a history of thinking the grass is greener on the other side of the fence.
[n8r296f] (score 51, diepte 4) 4 months is enough time to figure out if this is the right decision; if you see a therapist every week for the next month, you’ll have a pretty solid answer by September.

No amount of money, time, expenses, travel, headache, are worth getting married because you felt like you had to. It’s okay if it is over in the end.
[n8qlbsn] (score 49, diepte 0) so, I knew my fiance was “the one” early on, years ago. fantasized about marrying him for years. and yet now that the time has come, it is oddly panic inducing. (I struggle with anxiety, in general). it’s such a big step on so many levels! and when we get married, my path is more or less chosen, it’s like the end of day dreams or “what ifs”….like where we live, where we plan to retire to (his home country). they’re all great plans, of course, but it’s a weird sense of finality getting married. I wonder if you’re feeling some of that, too. “if I get married, this is my life. whereas if I stay single, so many possibilities are open…”

all that to say, I totally understand cold feet, even if you love someone and ultimately do want to marry them.

and don’t romanticize the single life too much. :) 

i think you could really benefit from talking this all out with a therapist…you seem to ask the right questions…is it dissatisfaction with my life or the relationship? they can help guide you in the right direction.
[n8qnmb4] (score 42, diepte 2) > Am I projecting my dissatisfaction on the relationship


This is what I'm guessing reading your comment. What else are you dissatisfied with? Work, the place you live, wishing you'd had more adventures?


An important thing to remember is that marriage is not the end of fun. You can still travel, still party, still go back to school, still have all manner of new experiences. You don't suddenly have to start playing house and being boring and old.
[n8qjs4k] (score 30, diepte 0) Sorry you’re going through this. I can’t give you an answer, but what I can say with confidence is I’ve never once, not for a single moment, questioned my decision to marry my fiancé. Since we’ve gotten engaged, the excitement and anticipation has only grown stronger. I never had moments of doubt or fantasize about being single. 

It sounds like you should put a pause on the wedding planning for the time behind and not put any more deposits down so you can get to the root of these thoughts, ideally through therapy 

Wish I could offer some more advice than that, but it’s hard without knowing your personalities and your relationship. Sending you hugs
[n8qrg95] (score 30, diepte 2) It honestly sounds like you feel lukewarm at best about your fiance.
[n8qm2si] (score 29, diepte 0) What about single life do you fantasize?
[n8rrxad] (score 27, diepte 4) If your fear of ending up alone is what is holding you back from ending it, you should end it. You stay with a person because you love them and can't imagine a life without *them*, not because you're worried about never finding anybody else to settle down with. 


From all your responses, you really do seem lukewarm at best about your partner. You keep mentioning the different things you want and the different paths you could take. Not a single thing about what excites you about a path with her, or what about your relationship is fulfilling.
[n8qq7ip] (score 27, diepte 0) I didn’t have any doubts or cold feet and would just say “when you know you know”. Sounds like at least postponement and therapy are needed
[n8r13eh] (score 26, diepte 4) Do you think if you were single you’d actually pursue what it takes to live in New Zealand for a year and follow through with it?
[n8qy2rh] (score 25, diepte 4) I know you said your fiancée doesn’t want to live abroad but if you imagine she was open to it - would you still want to do those things on your own or would you be thrilled to have her with you? Basically if you could change the things in your life that you’re bored with and go do those adventures, would you want her there with you or do you only envision them on your own?
[n8r0ap1] (score 23, diepte 2) Exactly.
[n8rkhvt] (score 22, diepte 3) >At 30+, most of what's out there is people who were too unstable to pair off in their 20s.

Lol, what?? "Pairing off" with someone in your 20s is not an indicator of any type of stability.
[n8s8uh9] (score 21, diepte 4) THIS is the comment that hit you the hardest? Please just call off the wedding.
[n8r0uz9] (score 20, diepte 4) This sounds just sounds like fantasizing. If you really wanted to do that, you would have by now. Your brain is just screaming MayDay now that you’re taking some big steps.

I’d get excited about what dreams you can explore together and think about tackling challenges together

For example: I love where my fiance and I live (my hometown, Nashville), but he misses his home in Santa Cruz terribly. He told me tearfully one night years ago that the only thing he worries about with our relationship is staying in Nashville forever. I told him we could move to his home town for a bit too, I don’t want him to be unhappy! Santa Cruz is too expensive for us long term, but I’d be happy to make some sacrifices to move. We go after our dreams together.

Living abroad is a bigger fish to fry. He would like that, I wouldn’t (not as long as my parents are alive), and we prioritize international travel to continue expanding our horizons. I’m more of a Florida Beach and chill girl, but I’ll brave the hectic streets of Japan with him.

Another perspective. Hope the discussion here helps you! Married life isn’t the end. For me; it’s securing my lifetime adventure buddy.
[n8rou0f] (score 20, diepte 4) Ok I have to jump in on this one. I married at 24 and was divorced at 28. Everything was right on paper — he was smart, kind, had a good job, same values, treated me well. But I was bored af (though I didn’t realize that’s what it was until quite a while later). I was also dealing with depression, which clouded my emotions and allowed me to convince myself it was a me problem rather than an us problem… I was still living a good and fairly exciting life, but I always felt weighted down. Looking back I realize a lot was because he wasn’t excited to make the adventures with me — it felt almost like a chore he humored to “keep me happy” so I’d stay. 

I had doubts leading up to the marriage. I could tell I wasn’t excited about things, but had no other point of reference — he was my first serious boyfriend, college sweethearts. I tried talking to my parents about it, but they had a pretty conservative take on relationships, and to them “good on paper” was good enough. I also realize now that I was trying to change myself to fit the type of relationship I wanted. Well, first I tried encouraging him to grow to what I needed in a partner. He claimed he wanted the same, but never actually reached for it — he was just afraid I would walk away so told me what he thought I wanted to hear. I really did try to communicate my concerns, but I took him at his word rather than his actions. Eventually (after the wedding) I gave up trying to get him to follow through and tried to shrink myself to fit (which of course also very much did not work). Eventually I gave up trying to change either of us and the relationship was intolerable and not at all a dynamic I could live with. 

I haven’t done all the adventuring I would’ve liked since the divorce (finances and personal health played a lot into that), but I was able to eventually find a partner who actually wanted the same kinds of adventure I do. The dating landscape in my 30s sucked, and I took a long time putting in work to know myself better, but I’m now about to marry the kind of man I never thought could possibly exist. I get nervous about getting married, I think because I know how it CAN end, but when I think about HIM I have zero doubts in my mind. He has 4 young kids so we’re not moving abroad anytime soon, but travel and adventure is a big thing for both of us and we prioritize it together. Life doesn’t HAVE to be one thing or the other. You DO have to find someone who prioritizes the same things in life, though. 

Yes, sparks can fade (though you can also be deliberate to keep them alive — it’s work but it’s possible). But if you’re not EXCITED for a life with her, be kind and let her go. That’s my biggest regret in my first marriage: letting things go as long as they did, which caused even more pain for more people when it eventually ended (again, depression made everything cloudy and … slow). 

What you need to figure out is if you two can live a life you love together or not. Do not settle. And honestly, don’t get married if you still have all these questions in your mind. Maybe you can work them out in couples counseling in the four months you have left… strangers on the internet can’t tell you that. But if you’re getting an ultimatum (which is honestly fair after 8 years), still aren’t SURE, and don’t have time to work things out together, walk away. It’ll hurt now, but it’s a kindness to both you and her in the long run. 

I will also say… starting over at 30 certainly may limit your options. If settling down and having a family is your top priority, then you should disregard this entire comment. But from a number of your replies I feel like you’re wanting more outside of that. Bear in mind you may have to pick one — adventures abroad or a sure shot at a wife and kids. One big question I asked myself, though: would I rather be alone forever (I really didn’t want that) and 100% true to myself, or shrink myself to fit into a safe relationship? For me I realized I couldn’t live with the latter so I took the former. I probably won’t get children of my own, but I’ve certainly found one hell of a life I love.
[n8r7239] (score 20, diepte 0) Go on to social media, and type in “fearful avoidant attachment”. See if anything rings true for you. You said you have a history of doing this with big decisions. This is a you thing, not a partner thing.
[n8qqqlt] (score 18, diepte 2) It sounds like you’ve already decided you don’t want to go through with it? there are tons of new experiences you can have with your current partner. Travel, take a random class together, start going on dates, pick up new hobbies. Have you thought about things yall could do? Or are you thinking of new experiences with someone else? Same for meeting people. Join a sports rec team, or a new gym, or whatever hobbies you have. Unless by people you mean, dating new women to see what else is out there. Just a few differences on frame of thought. There’s no right or wrong answers here! Just bc you’ve been together for 8 years doesn’t mean you have to go through with it. Better to learn now she’s not the one than having to get a divorce. Having lots of single friends is also an influence. I’m assuming if they were all married, you might be feeling like a 5th wheel. Nobody is going to tell you what to do - just make sure you really imagine your life without your Fiance in it anymore and let those feelings marinate.
[n8rn8nc] (score 17, diepte 1) Bro she has waited 8 years. If he’s postponing, she’s gonna dip.
[n8snkqy] (score 17, diepte 4) Can't believe people upvoted that crazy-ass comment. Also the general vibe of "you should stay with her so you don't end up alone" is so wildly unfair to the bride. She deserves better
[n8rrkdl] (score 17, diepte 2) Oh fuck off dude.
[n8si9ed] (score 15, diepte 4) I’m a Kiwi born and bred, for gods sake take the rose coloured glasses off. We’re in a recession here and have massive unemployment, you will not get a job. Stay where you are and work on your issues like an adult instead of running away with your head in the sand.
[n8qrkik] (score 12, diepte 2) That’s not silly at all to me, I’ve lived all over the world and loved every minute of it! It’s changed me in so many beautiful ways. I always encourage people to do it! i guess my next question is, what would you do if you didn’t get married? Would you move to France? Change careers? Go to grad school? Are those just fantasies or are those real options?
[n8slj2t] (score 11, diepte 1) >I’ve never once, not for a single moment, questioned my decision to marry my fiancé.

I sometimes question it and I don't think it's something wrong to sometimes question your decisions. I'm questioning most of my decisions in life. That said, I've never felt anxious due to it - it's always a quick thought "am I making the right decision" and then right after that "yeah, what else could you possibly want?". So I totally get getting anxious and questioning yourself, but constantly and without a clear answer? Definitely a problem.
[n8qu2ev] (score 11, diepte 4) Right of course, your life’s not over in any sense. My wife and I are early thirties too and we still see our friends all the time, travel when we want, and do what we want because we don’t have kids yet. 

But definitely our social dynamics have changed a lot. Most of our friends are in serious relationships and getting engaged, are already engaged, or are married by now. Our single friends struggle a lot and some of those in new relationships are just moving pretty fast. Definitely have transitioned from spending most of our time in our 20s with our friends to just us and thinking about children soon.
[n8qpx8g] (score 11, diepte 0) I called off a wedding in my late 20’s. The feeling I had was that it just didn’t fit right. Like, it felt like we were puzzle pieces that could not interlock. We could maybe fit a bit if you shoved the pieces but it wasn’t a smooth fit when it’s the right piece. Maybe that’s very woo woo but it’s almost how it physically felt. 

I had this gut feeling. I knew we could make each other happy for a few years but ultimately we wouldn’t last. It was one of the hardest decisions I ever made. I kept telling myself that it’s better to be an ex-fiancé than an ex-wife. That really helped me keep perspective on my decision.
[n8qktvy] (score 10, diepte 0) Agree with other advice that therapy and postponing the wedding seem smart for now. I didn't question a single second when my fiancé asked me to marry him. I know people are different and everyone has relationships that work for them, but I don't think it should be this hard. And you've acknowledged this in other comments, but it isn't fair to keep your fiancé waiting due to your uncertainty either. Good luck to you both, I hope you each get a happy ending in whatever way that looks like!
[n8qzyxh] (score 9, diepte 0) This isn't cold feet. I tried to call off my wedding when I had those feelings, and our pastor convinced me it was cold feet. I got divorced after 3 years.
(78 reacties met lagere score weggelaten)

=== THREAD 1ibk8et ===
SUBREDDIT: r/Mommit
DATUM: 2025-01-27  SCORE: 1761  REACTIES: 96
TITEL: Breaking my foot was the only way my husband understood the mental load (10/10 do not recommend)
POST (source_id=post):
I want to share my story about the mental load and how my husband finally understood what I’d been carrying all this time.

Seven weeks after my second daughter was born, my brother (my only sibling) passed away unexpectedly. It broke me. My husband stepped up for a couple of weeks, but soon, I was back to carrying everything—our kids’ routines, the house, the mental juggling act—because I didn’t want my grief to disrupt their lives.

Then, when my youngest was 4 months old, I broke my foot and needed surgery. I was completely out of commission for weeks, doped up on pain meds, unable to do anything. My husband had no choice but to take over.

That’s when it hit him. He came to me one day and said, “I’m so sorry—I had no idea.” For the first time, he truly got it. Since then, he’s been so much better about sharing the load. We still slip into old patterns sometimes, but he’s not the same man he was before.

The truth is, even when they think they understand, they often don’t—because they’ve never had to carry it. Sometimes it takes stepping into the role fully for them to really see it.

Anyone else have a turning point like this with your partner? What helped them finally understand?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m9j2b6y] (score 1599, diepte 0) First off, I am so sorry about your foot! But I'm glad he had a wake-up moment! 

Mine was a few years ago, the first time we had three kids in three different schools. Of course there were two back-to-school nights on the same night, so we had to split duty. I went with the high schooler, he went with the elementary schooler. 

Well, not thinking, he put his own personal email address down on the teacher's paperwork and the "Parent Contact List." Suddenly, he's getting every school email. The behavior reminders. The special spirit days. The homework packets. The field trip information. The class parent asking for donations for every holiday event. The request for volunteers. And on and on. He asked them to change the email to mine, but no one ever did it. 

"This is nuts!!" he cried. "Who could be expected to keep track of all this?!" 

"ME!" I snapped right back. "I'm usually keeping track of it for ALL THREE OF THEM!" 

He went completely silent. Holy shit, it was amazing watching the realization dawn.
[m9j954k] (score 671, diepte 1) The fact that his first reaction was to try to dump it all back onto you 🤬
[m9j138b] (score 451, diepte 0) Just chiming in to say, "I didn't want my grief to disrupt their lives." .... wow. That hit home. I could never put it into words but you did. I had started a new job, had a son that just turned one, a daughter that just graduated high school,  took in my autistic brother,  sold my house, bought a new house and cleaned and sold my moms. I didn't grieve her for almost 2 yrs because I couldn't stop going.  You finally put it into words 7 yrs later.  Thank you.  I'm so glad you are getting a partner you so much deserve and I'm sorry it took a broken foot for him to realize.
[m9j2l7e] (score 287, diepte 0) Can you describe the exact events that made you break your foot? Needing to replicate it so maybe mine gets his head out of his 🍑
[m9j9qqj] (score 244, diepte 0) Haha when we had our 1st baby we were living in a new city with no close family or friends. I was the stay-at-home parent and he would work his job, and then want to work out for an hour, and then play his video games at night. At one point I lost my shit and yelled, “if we got a divorce I would get every other weekend off!”  I think that was a major wake up call  and from then on we divided our me time equally.
[m9j8ygp] (score 223, diepte 1 OP) I was actually managing a burning pizza, calming a screaming toddler, and trying to prepare a bottle. I turned too hard, slipped on a melted ice cube, and boom. My husband was out of town and I had to call an ambulance. I also got a lisfranc injury which is like this crazy rare injury. It was spectacular.
[m9jf780] (score 222, diepte 2) For what it's worth, I actually asked him to do this. It was a weird year where he was getting all the emails for one kid, and I was getting all the emails for the other two.
[m9k46u7] (score 188, diepte 1) I love it didn’t get changed, I like to think there’s some PTA mom laughing to herself refusing to change it like “oh no you don’t, you’re in this now! It’s your turn for a bit!”
[m9jm7le] (score 181, diepte 3) Yeah, that would be wonky. We have a family email account that we use for schools, sports, signing into school apps, etc. We both get the emails. Because I'm the SAHP, I do the bulk of follow-up but it's there in case something happens or if he has time to tackle it.
[m9jwus4] (score 137, diepte 0) I broke my ankle. My husband lost his shit because he was tired of it. After that our relationship was never the same. But he didnt step up. He slowly backed away. We are getting a divorce now.
[m9k0tse] (score 123, diepte 0) So…kiiiind of? I had postpartum preeclampsia so I was in the hospital for 4 days. My husband was home with our 3 year old and 2 week old and took care of them round the clock, and visited me once a day in the afternoon. 

The thing is, he stilll kinda brings it up like he’s the expert on our baby because of the skills he learned those days, like “oh yeah when she gets fussy like that you just need to XYZ”

The thing that bugs me a little is, she was still in her newborn sleepiness so she basically slept all day. Yes, he did the night shift and I’m thankful, but he can’t really compare her then to how she is now, 4 months later. Also, he got takeout every day and didn’t worry about cooking, and he had friends who helped look after our toddler for a couple hours each day. So it just isn’t the same as being a sahm day in and day out, ya know?
[m9jkqr8] (score 85, diepte 0) Sadly, the turning point never came. We are in the process of divorce because I’m already a single married mom…
[m9j6cr7] (score 84, diepte 1 OP) Wow that is a whole lot on your plate while also momming. I hope things have slowed down a bit for you 💕
[m9jr9ph] (score 80, diepte 0) A few months ago, I crashed medically. I had been warning my partner (and dad to our kids) that it was going to happen if I kept going at the pace I was, and continued to be responsible for everything (I have a few chronic Illnesses) nothing changed, and what I predicted would happen did. 

I was so bad he had to take leave for work, because I couldnt be left alone with our kids while I recovered. It's been months, and he's finally starting to grasp the mental and physical load I carried. And I know it's only the surface of it, because so much had to be neglected in the face of all of this. 

I'm sad it took this. And I'm sad it took your breaking your foot for it to click with yours as well.
[m9jzhrf] (score 70, diepte 2) The melted ice cube made me cackle. I'm so sorry 😞
[m9juxn0] (score 68, diepte 0) I have almost the exact same story - except it was my ankle. After week 1 of being laid up, he realized how much I did every day. He declared that we needed a house cleaner and he would pay for it. Two and a half years later, we still have a house cleaner and he does so much better about dishes and laundry. 10/10 would not recommend getting into an accident to get your husband to realize how much work you do!
[m9je3ii] (score 64, diepte 0) I recommend more moms fake a death-sick was that starts on a Friday and doesn’t end until it’s time for their “partner” to go back to work on Monday. Be 1000% incapacitated, unable to do anything but moan piteously and not able to answer any questions. Or just outright leave for a weekend.
[m9k5w7p] (score 61, diepte 0) Ours was me going back to work on weekends, I left before little one was awake and back just in time to help with dinner. He’s telling me he’s exhausted and needs to go lay down, I look dead at him and say “if this were tomorrow you wouldn’t be off work for another hour and a half, and I’d be making dinner and then helping little one to bed, and up again with him early” he just got this slow realizing in his face, he genuinely hadn’t realized all that I did. What really helped was continuing to work weekends days, and leaving laundry for him, dinner to be made, and he’s just really stepped up and we’re much more 50/50 now. He really is a great guy it’s just hard to understand if you’ve never done it!
[m9j510h] (score 56, diepte 1) Oh how I wish to be a fly on your wall at that moment! I hope it got better for you.
[m9j6vrt] (score 52, diepte 1 OP) Hahaha this is awesome. It’s amazing that it took that long for it to happen. You’ve been carrying this load for a long time 😊
[m9k1jaq] (score 51, diepte 2) I've learned I deserve better. And my standards are higher now.
[m9j7lc6] (score 48, diepte 2) They have.  I just wish I had the outside perspective at the time to tell myself it's ok to fall apart.  It's ok to envelope myself in the grief of losing my mom and my best friend.  It was a tidal wave when it finally came.  I'm sorry to hear about your brother.
[m9kiz82] (score 47, diepte 1) 4 days? 🙄 that’s nothing in the newborn days lol it went by so fast.
[m9ixlj5] (score 46, diepte 0) I’m so sorry about your foot but really glad you are recovering and have an (almost equal) spouse!
[m9kx7hn] (score 46, diepte 2) I read that as Lisa Frank Injury LMAO
[m9k07v8] (score 38, diepte 1) That's horrifying. I'm sorry that happened to you.
[m9k613b] (score 35, diepte 1) That is a good kick in the ass.
[m9l0qks] (score 34, diepte 0) Brb going to break my foot
[m9nroql] (score 33, diepte 5) You're welcome! This kind of thing only works if the other partner *wants* to be looped in. But it's a really lovely moment when my husband texts me from a meeting he's bored in and says "ordered X item for Spirit Day next week" and I'm like cool one less thing. 

We also sign up for utilities, streaming services, and stuff with this account. If something were to happen to one of us or we just aren't around, there's no delay in getting logged in or passwords reset. It has a lot of value.
[m9j89px] (score 31, diepte 3 OP) That’s what they say, avoiding it is not really making it go away, just delaying it. Sometimes we have to delay it due to life circumstances. It sounds like this was your experience and eventually it had to be dealt with. It’s shocking to me how little to no information is available for resources for moms who are grieving. I actually didn’t really find any information that was useful.
[m9k1fj0] (score 30, diepte 4) That's a really good idea!
[m9kjfs0] (score 30, diepte 1) I'm fucking furious for you that you WARNED him and he still didn't listen!!!
[m9jurvt] (score 27, diepte 0) My partner became the stay at home parent for 3 months when my first was a baby and I first went back to work. He was such a better partner and coparent after that, and was always home on time from work. Was a game changer
[m9k3jvt] (score 25, diepte 2) This is too relatable. I’m sorry this happened to you!!
[m9ls8dw] (score 24, diepte 3) Ditto. Rainbow injury with dolphins
[m9k4j3s] (score 24, diepte 1) No leaving is better, to a cabin in the woods where all you can hear is birds for 3 days, highly recommend!!
[m9k75mn] (score 24, diepte 0) I got hit with covid really bad in the fall. I couldn’t get out of bed unless it was to drag myself to the bathroom. My husband got a crash course in my daily life with a three year old. Even then it didn’t cover the chaos of it all. I was still left with a mountain of laundry and actually grocery shopping (not just super easy/ junk food meals they lived off of). But he made an agreement that every weekend I get until 2-3 in the afternoon to myself. I sleep in, catch up on shows, just relax. It’s improved my mental health majorly
[m9k7hm2] (score 21, diepte 1) My husband would call his mom. She an angel and lives close by. He’ll never get it
[m9l85kb] (score 20, diepte 1) We lost our dad 2 years ago. 3 weeks before he died my sister was diagnosed with stage 4 cancer. She made it through, but had no time to grieve our dad. 

It is only now, after being cancer free, not having to have surgeries or chemo all the time that her mind can grieve.
[m9l37my] (score 18, diepte 0) Sorry to hear about your foot. It seems for men they have to really go through it to understand it. Otherwise it’s in one ear and out the other. 

My husband’s realization happened when he had no work for the summer. We have three kids two twin 4 year olds and a three month old (at that time). He had to figure it out while I went back to work from maternity leave. They aren’t in school yet so previously I’d been working part time and handling mostly everything. The doctor appointments, the nap time, figuring out lunch, cleaning, dealing with the emotions, crying, sibling fights, groceries, laundry etc until I got home. He’d never understood my frustration, tiredness, and just being overwhelmed by it all. Then the day came where he apologized as well and said he didn’t realize the mental load and energy it takes.

I never thought I’d see the day. It was honestly a relief. Not perfect like you said but now the load is shared.
[m9l15aj] (score 17, diepte 1) Every Christmas break for the last 4 years I inexplicably pass out for 4 days starting around the 27th.  Managing to occasionally surface for food and water.  This past year it happened again and my husband of 25 years finally realized I was handling ALL the prep for the entire event while working.  And that this year the addition of the first grandchild created a whole new bunch of issues and that my system was literally shutting down.  He's been fantastic after that now that he's realized I just can't do it all anymore.  I finally got a "I don't know how you do it!" from him.
[m9jxypc] (score 17, diepte 0) I am so sorry about your brother, it must have been so hard to put your grief aside… my father passed away 9 days after my son was born. It broke me as well and I still wonder how I didn’t get PPD. My mind was battling 2 strong emotions, the joy of finally having my baby and the grief of losing my dad.

I did my best to take care of my family and myself, but I am fortunate to have a partner that was there for me and took on most of the work. He truly was my rock and still is almost 2 years later. 

All of this to say: I understand you and I am sorry it took you breaking your foot for your husband to finally get it. I hope for you that it’s not just a “2 week” thing and that he steps up for good.
[m9m51jp] (score 16, diepte 1) Haha, reminds me of my husband - he was very involved with out newborn, because he had 2 months of paternity leave. After that he went back to work. But he was convinced that his strategies that worked for an 8 week old would work for an 8 *month* old. He got stuck in the newborn mode and was always trying to feed it put to sleep an agitated toddler at some point 😂
[m9kqhan] (score 15, diepte 1) I wish it would be the case. My preschool sends us both emails. We both have the app they use to communicate events and reminders. And it's a freaking preschool so there's not a ton of stuff going on, but he does an exceptional job of ignoring all of those communications and does nothing unless I specifically tell him to. On one hand I appreciate that he does do things when I ask, but it's really a chore to ask and reminder and ask again.
[m9krcam] (score 15, diepte 2) Omg, a couple years ago I was about to walk down the stairs with arms full of bagged groceries. I took the first step down the stairs when one of the bags snapped, completely throwing off my balance and I fell all the way down the stairs and landed on my foot. The doctors thought I had a lisfranc injury and I was in a walking cast with crutches for a couple weeks. After a couple more rounds of imaging they decided it wasn’t a lisfranc but wild seeing that you had one! Sorry you went through that.
[m9l4nsg] (score 13, diepte 1) I created a shared email account for all school communications. I told him I was no longer the only person responsible for the emails.
[m9l0flu] (score 13, diepte 1) I'm so sorry.  That's a heck of a way to found out what type of person he is.
[m9l90wu] (score 12, diepte 3 OP) I still don’t know how to pronounce it tbh
[m9l6bnd] (score 12, diepte 1) Ugh I caught the stomach bug with a 3 month old and my partner kept bringing him to me because he wouldn’t stop crying. I told him to pull out the frozen milk for a bottle because I couldn’t nurse him but according to him the baby wouldn’t take it. Between throwing up I’m was nursing/laying with the baby. I ended up having to go to the er. Guess who got sick as soon as we got home AND got to lock themselves in the bedroom for a couple of days to get better.
[m9n4sgi] (score 11, diepte 4) This so brilliant, my kids are only in prek and kindergarten but I’m going to do this!
[m9l9rwk] (score 11, diepte 1 OP) Yeah I will say, his best day is nothing like my worst with them. Although I do believe he tries, a lot slips through the cracks. I try to give him some slack because the things that are easy for me take a lot of effort for him to do. He’s also exhausted. But it does suck that it takes us being literally unable to function for them to understand. Let me know if you find an easier way
[m9kndm1] (score 11, diepte 0) I’m so sorry about your foot and I hope it’s healing well. Unfortunately my story is much like yours, but my husband still never fully embraced what my job was. I needed surgery back in April and I was out for 2 weeks; at that point my son only had two days of EI appointments per week but I canceled them so my husband didn’t need to go to them. 

After the first week he apologized not realizing how difficult it was to watch him and manage the household, but again he had it easier since kiddo was home all day. 

Now though I think my husband would have a heart attack doing all of the running around I do monday through friday for my son’s EI appointments. There’s a total of 10 appointments per week now, and I still do all of the food shopping, cleaning, dishes, getting laundry together, and cooking.
[m9l9808] (score 10, diepte 1 OP) It’s a lot to handle and some just can step up and do what they need to. There are days I question myself tbh. It’s definitely an eye opener realizing that you really can’t take care of both kids without help. Sorry you’re going through that.
[m9labuu] (score 10, diepte 1 OP) Yes that moment of clarity they get.
[m9l1dio] (score 9, diepte 1) Hope things get better for you 🙏🏼 you deserve better and happy you are finally getting rid of the dead weight.
[m9kn3es] (score 9, diepte 0) I had to go to the hospital for postpartum preeclampsia a month in and my husband took over full care the entire weekend. It changed him fundamentally too, although he was always a caring dad, I think the experience of doing it fully was an intense one.
(54 reacties met lagere score weggelaten)

