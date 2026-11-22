# Label-batch batch_0113

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
Schrijf het resultaat naar `batch_0113.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 7dtv2n, 1457odj, 31mv1v).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 7dtv2n ===
SUBREDDIT: r/xxfitness
DATUM: 2017-11-18  SCORE: 265  REACTIES: 134
TITEL: I Went From Sedentary, At Best, To Walking At Least 4.5 Miles Each Day. How Do I Keep My Feet From Trying To Blister So That I Can Keep This Up? I Have About 160lbs To Lose.
POST (source_id=post):
I was overweight for most of my life, became severely underweight...  Then started smoking marijuana and drinking extremely heavily (calories from munchies + calories from alcohol).  I went from 95lbs at 5'3" to 275lbs (current).

I have several health issues that are directly affected by my inactivity.  Major depression and anxiety/panic disorder are very obviously affected by this lack of activity.

After some recent events, something in my mind snapped.  Something that therapy failed to accomplish after several years.  I have been encouraged by numerous doctors of varying fields to loose weight, or to at least start getting exercise.  i woke up one morning after a poignant dream ready to hit the ground running.

I did.  Four days ago when panic attacks began getting worse than they have in about a year (I used to vomit dozens of time with each attack, lose my memory--this was now happening again after my longest/only period with minor attacks), I decided to take my dog to a local lake for a walk.

I unknowingly got lost on the nearly three mile trail and ended up walking a bit over 4.5 miles.  When I got home, I felt absolutely incredible and could actually sleep without being hammered.  I slept *through* the night without waking up for 3-4 hours.

So I did it again the next day, and after that.  Here we are today.  I've walked over 15 miles these last few days on these trails.  I noticed the first day that my feet were getting sore right behind my toes and were looking like blisters were forming.  They looked particularly bad last night, but I woke up, and it looks like nothing even happened.  They aren't even really sore like they have been.

**VV  Start Here If Too Much Text Above  VV**

How do I prevent blisters from forming so that I can keep this pace up?  I got new, thick, padded sports socks to try out.  My shoes are tennis shoes that I received as a Christmas gift several years ago but never wore because I had no need to.  They are in excellent condition.

Is there any other way I can prevent what I assume is a bit of sweat and a lot of rubbing/friction in that area?

**STATS** In case they are relevant or helpful:

* 25 years old
* 5'3"
* 270lbs

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dq0a6d6] (score 100, diepte 0) Examine your feet regularly for "hot spots," basically red areas that often feel warm to touch. This is are blister warning signs, but if you use and anti-blister product you can prevent a blister from forming. I personally prefer Second Skin sheets covered with tape, but you can also buy blister bandages that are a little easier to use.

Be careful with socks! Socks that add bulk can increase rubbing, and rubbing causes blisters. So just keep an eye on everything and check your feet if you notice any rubbing. Also avoid cotton socks because cotton holds moisture and that isn't fun for your feeties.

Your shoes will break down with wear and the fit can start to get a bit weird. Not something to worry about it they fit well right now, but it's something to keep in mind for the future.

Basically, just keep an eye on everything and don't worry too much. Good luck--it sounds like you're making a lot of great progress!
[dq0fabr] (score 45, diepte 4) I'm a nursing student & a mom and spend 12+ hours daily on my feet. Go to a good shoe store that seems aimed at "old people", ask for walking shoes. They'll fit you and suggest things like higher/lower arches, leather that'll stretch and wash easily, outdoor shoes with better traction (or whatever works better for the weather there). Give them all the info they can help. They'll also have special socks that work for long walks/outdoors/increased sweating etc. I buy a new pair of the exact same $140 shoes when my back starts bugging me or my heels start aching at the end of the day. No regrets. I used to have sore feet every day at night and now I could go even longer in those shoes. They're ugly but totally worth it. Best of luck!!!
[dq0az39] (score 40, diepte 1 OP) Ah!!!  Thank you so much!  You can tell I'm inexperienced here...  I didn't even know there were products available for things like this.  Whoops!  The more you know...  :)

I'm going to be asking for another pair for Christmas for when the time comes.  I figured that I will be needing a new pair due to thinner feet quite a bit before these are worn out from use.  Are there any pairs you suggest?  My parents would be elated to get them for me.  They've been begging for a Christmas list!

Thank you for the warning about socks!  There's my ignorance again.  :p  I thought that the additional fabric would help.  I'll add those to my list as well!

I *really* appreciate the encouragement.  This is something I've been wanting to do for years, but I'm extremely self-conscious.  I'm sure no one would see me jogging and think bad of it (unlike watching me at a fast food place or something), but, still...  Just an anxiety thing again, I suppose.  Plus, I'm assuming they're a bit too preoccupied to stop and point anyway.  Ha!
[dq0amy0] (score 38, diepte 0) 1. Avoid 100% cotton or cotton blend socks. You want synthetic or wool here. 
 
2. Check your local pharmacy for moleskin bandages and put them on your feet where you tend to blister. Regular bandaids can work too, the just don’t always stick as well for me.
 
3. There are specialty powders and lotions for avoiding blisters in the pharmacy aisle at Target. I’ve never used them, but a cheaper version that I have used is Vaseline. Your foot will feel icky and you’ll have to wash your socks, but you won’t blister.
 
4. Keep on going. If you keep taking good care of your feet, and maybe even take breaks as necessary to let them heal, they will eventually build a callus. Once you have the right amount of callus for your foot, they won’t hurt anymore and you won’t have to worry about blisters!
 

Congrats! I hope you stick to it!!!
[dq0hv6q] (score 30, diepte 5) After working in a restaurant and walking on hard cement floors all day, I learned that if I have two different pairs of good shoes and alternate them every couple days, my feet and back did not get nearly as sore as when I wore the same pair every day. I know buying two (Good) shoes at a time can get pricey, but just remember that then your shoes will last (essentially) twice as long and you will have more comfort!
[dq0alsz] (score 27, diepte 0) I absolutely love blister band-aids and go through them like crazy (I recently went from 280 to 170lbs in a year and a half, after the same snap realization moment you had - keep it up, you're amazing!!!). Definitely recommend them, especially if you have existing blisters - they suck all of the moisture out of the blister to help it heal while creating a padding so your shoes don't rub them further. Good luck on your journey!!
[dq0b5jo] (score 26, diepte 2) Also keep in mind that if you walk a lot your shoes will wear out.  For me i know when my lower back starts to hurt after awhile on my feet it means I need new shoes. As soon as I switch the pain goes away.
[dq0jviw] (score 22, diepte 1) I'll jump on this one as well to reinforce the sock comment. 

Invest in 3 pairs of double layer socks, ideally made of merino wool (most aren't allergic to merino and it has anti fungal properties). The two layers prevent blisters and the cooling of wool can't be beat along with the lack of stinky feet. 

They are not cheap ($20 per pair) but they are so worth it, I wear them for every run. My favourite brand is SmartWool and you can probably get them at REI or MEC. Go for the running ones, not the crew sock hiking ones unless you want them for that purpose too. I see some epic hikes in your future , once you get comfortable with city trails you will love the sense of accomplishment when you reach that view!
[dq0b9yw] (score 21, diepte 0) This is how I prevented forming blisters on long, grueling ruck marches in the military: put a thin layer of Vaseline on clean, dry feet. Put on panty hose (cut to make sock length) as a liner and then your socks over that. Made my feet blister proof.
[dq0le0i] (score 18, diepte 6) I second getting a second pair. A lot of people talk about shoes not drying out if they're used every day and how it breaks down shoes faster. Not sure if that's real science or broscience, but I do find my running shoes last longer when I rotate them.
[dq0b7tl] (score 18, diepte 1 OP) Thank you so much!  Can you explain the vaseline usage to me in more detail?  I don't mind if it feels gross--I'll be coming home to shower when I'm done anyway!

I intend to stick with it!  The way I have been feeling after these adventures is...  Pretty freaking amazing.  Way better than the way the drugs made me feel.  And without the guilt!  ;)
[dq0gzf0] (score 17, diepte 2) Basically the vaseline keeps the skin soft and supple so that it isn't as easily irritated by the friction. It's like lube, but for your foot. So I would put it on any of the hot spots another redditor mentioned just before you go out walking. 

Edited to add a side note about self care because it's changed my life and I am now a self care missionary: 
Maybe as you progress, you can set up rewards and self-care around nurturing your feet? It could start as a way of ensuring that you keep going---a nice soak for your feet with Epsom salts, some of those socks with aloe in them, nicely scented lotion---then blossom into a way of rewarding yourself for working hard. The kind of discipline that's involved in what you're doing is amazing (great job!)  but also really draining psychologically speaking. The best way to ensure that you have what you need to make the choices you want to make is to nourish your mind. The body needs calories to function but mind feeds on positive experiences. So give yourself as many positive experiences as you can with exercise and that, more than anything, will make it easier to keep going.
[dq0a6w8] (score 16, diepte 0) Good socks (I wear Balega and Injini), well fitting shoes, body glide, increase mileage slowly
[dq0dalz] (score 12, diepte 3 OP) Thanks!  I've been wondering how to tell.  I'm asking for a new pair of shoes for Christmas from my parents so that I'll have a pair when the time comes.  Any recommendations?
[dq0pmvr] (score 12, diepte 1 OP) Yay!  I'm *so* glad that people are finding this helpful.  I would love to tell you how I (finally) got to this point.  This is basically how it happened:

I steadily kept gaining weight and becoming more and more frustrated with myself.  For several years up until about a week ago I was so upset and frustrated with myself that, for many days, I didn't even get out of bed except to eat (which I also did in bed) or drink (usually alcohol).  For about 2 years now, my psychiatrists and therapists have been suggesting I exercise out for at least 30 minutes a day just for the mental health benefits.

I finally snapped a couple of days ago because I was getting 2-4 hours of sleep per 24 hours because I am out of work at the moment and was just sitting around my apartment all day.  A lack of sleep makes things infinitely worse for me.  I decided to go to a local lake and nature park that is, luckily for me, less than ten minutes from where I live.  I took my dog because I knew that he would enjoy it.

My goal was to only do a mile or two.  But I got lost on the trail (unknowingly) and ended up walking about 5 miles by the time I had somehow wandered back onto the right path and completed the loop back to the main park entrance.

I had been having panic attacks that morning.  For me, there is a kindling effect.  Once they start, they don't stop until I am drugged up out of my mind, and even then...  That's only about half of the time.  When I got back to my car and sat down to drink some water, I noticed this...  Feeling...  I was a bit sore (obviously), but...  There was this feeling in my head.  And this sort of body high that was as soothing physically as mentally.  I felt energized and lighter than air.  I was tired, but not mentally exhausted, like I usually am.  It was a cozy feeling.

I slept freaking amazingly that night.  No meds needed to get to sleep or maintain sleep, which is the first time in about 4 years that that has been the case.  Even more amazingly, I was no longer waking up having panic attacks.  My vivid, lucid, nightmarish dreams stopped suddenly as well.  They were all very pleasant.

I woke up and my first thought was, "I want to feel like that forever."  So I went back and did it again and felt the same, but even more so.  It felt even better.  I was less physically tired once finished, even after only doing it once previously, and my mind...  I don't know.  It felt normal?  I wasn't depressed, for one thing.  I was thinking about all of the things I wanted to get done, like overdue housework.  And I did them without much thought.  Usually, I have to psych myself up for a few days just to get a load of laundry washed, dried, and folded.  I slept well again, and decided to repeat.

Really, though, what was sparked in me was complete frustration, and realizing that I what I was doing previously was not getting me anywhere except deeper in the hole I had dug myself, and all of that negativity was just breeding more negativity.  I didn't care about courage or being brave.  I just wanted to make it stop, and would do anything.  Even something I (thought) I hated.

As I was walking in the middle of the woods, I had some time for introspection.  And, apparently, the endorphins were already working their magic.  I suddenly didn't care that people could look at me and be judgmental.  My thought process behind that was, "We all have to start from somewhere.  Maybe that girl that just ran by was me a year or two ago."  But you would never know just from looking at someone, right?

Also, it was an *excellent* excuse to binge-listen to music!  WOW!  I LOVE music and that made the time fly.  I thought I had been walking for maybe an hour and it had already been nearly three.  Yesterday, I tried it again without music, and it was significantly more difficult, even though I followed the same path as the day before.  I think the music (upbeat, steady beats) kept me moving and focused on things other than sore legs, the sweat, the time, and other people.  I actually just finished the loop again today, with music again this time, and it freaking FLEW by.

I am feeling incredible again now.  No anxious thoughts, no racing thoughts, feeling confident...  And I attribute that to the physiological effects of extended, challenging activity at least as much as my mind set.  I'm proud of what I've done already.  But, I feel more like that shift in mind set has resulted from the hormones that were way overdue to be released.  I have had no need to "reward" myself, because the feeling itself it so incredible that it is it's own reward.  It's just so completely different from how I used to feel all of the time--in every way.  And we can choose to feel like this with a little extra effort.  It's astonishing.

Anyway, *trust me...*  The difference is night and day already.  I feel an amazing sense of accomplishment and pride, which is a major deal for me.  I feel on top of the world.  I want to continue feeling that way, and it's an easy solution.  I didn't even have to pay to feel this way (as opposed to all of the expensive medications and whatnot I have been on before, thinking that it would be an "easy fix").  I'm sure it sounds daunting to you, as it did to me.  Hell, it even *lead to panic attacks* thinking about how out of shape I was and how it was affecting my health mentally and physically.  But when I finally realized that I have nothing to lose but the weight and gave it a go...  Yeah, it's just such a great feeling I don't know the words to describe it.  It totally beats the cannabis highs or the drunkenness.  And it doesn't hurt me either.  It just makes me healthier in every way.  :)

I hope that makes sense!  Feel free to ask any more questions you may have.  :)  Or, you can also PM me if you'd like!  Perhaps we could follow one another on My Fitness Pal or something like that to keep each other even more motivated?
[dq0fnp6] (score 11, diepte 1) This is a great idea. I came here to suggest [liner socks]( https://www.amazon.com/s/ref=nb_sb_ss_i_1_26?url=search-alias%3Daps&field-keywords=women%27s+hiking+liner+socks&sprefix=women%27s+hiking+liner+socks%2Caps%2C395&crid=30XUE2JKWH01A). This seems to accomplish the same thing. 

Many years ago on Outward Bound, liner socks were mandatory items to bring.
[dq0awg7] (score 10, diepte 0) I had this problem when I first started exercising. I bought some Wright-brand anti-blister socks that helped and put moleskin over blisters when they did form. I also made sure to be properly fitted for shoes.  It can make a world of difference!

I don’t know you, but I’m so proud of you for all the walking!  That’s great!  That plus a bit of diet adjustment and you’ll lose that weight for sure!  :) That’s how I did it and I’m down 99.4 lbs right now, about 45-50 left to go!
[dq0lspm] (score 10, diepte 0) So, I have tried ALL the tricks for blisters. I am extremely blister prone and I walked 1000 miles on the Pacific Crest Trail this summer, so I've become a blister pro.

Blisters form from a combination of moisture and rubbing. If you keep your feet dry, you've won half the battle. If you make sure your shoes fit well, you've won the other half.

The best socks I've ever owned are Darn Tough. Two pairs lasted me the full 1000 mile hike without any signs of wear. I won't ever buy another brand. Darn Tough is merino wool, so they're moisture wicking and extremely breathable. They have a lifetime guarantee and will replace your socks if they ever get a hole. I highly recommend them, though they are pricy, they are great investment. Smart Wool is another good brand, but they don't come with the lifetime guarantee. 

Now, for the second half of the equation - reducing friction. A good shoe fit is the most important thing. If you end up wanting new shoes, I  highly recommend a professional fitting from a store with a good return policy.

There are also tons of small adjustments you can make to your existing shoes. The heel lock lacing technique is a great way to avoid blisters, and some people find liner socks help their shoes feel better too. The shoes should feel snug all over, but not have any pressure points.

If you feel a hot spot forming, stop immediately and take care of it to prevent it from forming into a blister. I find that Moleskin foam and Leukotape are the best combo  (Leukotape is just a really sticky and elastic version of medical tape).

If you get blisters, it is best to rest and let them heal. If you have a minor one and do want to push through it,  I find that the Moleskin/Leukotape technique is the best way to handle it, but many people like to pop them. Threading is the best way to do this, and I can give you a run down if you're interested. 

That's the high level overview! Best of luck and enjoy it!
[dq0hy0l] (score 9, diepte 2) The advice about hot spots is really good, you can pretty much completely prevent blisters by paying attention to them! What I've always done for hiking and backpacking is put duct tape over hot spots. You don't need fancy blister products necessarily, you just need something that will adhere to your skin and prevent friction between sock/shoe and skin.
(115 reacties met lagere score weggelaten)

=== THREAD 1457odj ===
SUBREDDIT: r/weddingplanning
DATUM: 2023-06-09  SCORE: 141  REACTIES: 128
TITEL: How often did you/do you feel like you’re getting cold feet in the lead up to the wedding?
POST (source_id=post):
Every day since we got engaged 4 months ago, I’ve been feeling kind of off about our relationship. There’s literally nothing wrong, he’s a great guy and things are the same as they’ve always been. We don’t have any huge issues. But I’m still not happy for some reason. When I think about the wedding, I’m filled with dread (it’s like a deadline that keeps looming closer). When I think about the marriage, it feels sort of ho-hum, like “this will be pretty alright and I can live with it and be happy enough” but I don’t feel any kind of uber excitement or “wow, I get to spend the next 40 years with my person!!” happiness.

I didn’t feel this way before we got engaged and I actually thought things were pretty great, but I think being engaged has made me take stock of our relationship and start noticing how unhappy I am now/may have been for a while. But all my family and friends say that since the feelings are relatively new, this is just normal cold feet and I’ll feel better again after the wedding is over and I’m on the other side of things. I’m not so sure though, which is why I thought I’d ask—has the stress/anxiety over getting married made anyone else question their relationship, or am I correct in feeling something else might be off? For those of you who are already married, did things improve after the wedding when the pressure died down?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jnjhgjb] (score 221, diepte 0) This sounds a lot like how I felt with the first guy I was engaged to (a decade ago in my early 20s). “Like we were good enough, we didn’t fight, we’re cool to just hang out. But I don’t feel happy or excited. Sex feels like a chore. I’d rather hang out by myself than with him.  When I ended it, I literally told him I did see myself ending it and I’d rather it be now or in 10 years when kids are involved. When I thought about our future, I saw one of those miserable lives where I resented him. 

I am early 30s, married for 3 months now to a man I’ve been with for 4 years and I didn’t have those thoughts this time. I did have some points where I didn’t want to spend the time/energy/money on wedding planning, there were times when I thought that I wasn’t good enough for him (I am), but never any thoughts on kinda dreading the life with him. 

When I thought about our future I was filled with so much joy and excitement. Like I’d rather be with him on the couch just hanging out and chatting and listening to him talk than do most other things. The thought of not having him in my life brings me to tears. 

And now being married is even more fun and exciting than I was imagining as a fiancé. 

I will add: in our almost 5 years together we have dealt with job loss, career change, no money, no cars, buying a new car, moving, bringing a family member/roommate into our home, and then back up again stability and good salaries again. So it hasn’t been a walk in the park and our premarital counselor was shocked at how much we’d been through {during Covid too} and how much we genuinely liked and loved each other. 

My advice to you is to talk to your partner. The thing that has kept us connected and strong is our communication. We talk about the hard things with a pillow over our face sometimes, but we still talk. Tell him you are having some feelings of doubt and you want to work through them with him. 

Before all of that though, really sit down with your thoughts and organize them out. A wedding is terrifying. It’s SO much money. It’s family members meeting. It’s stress. It’s needing to look perfect for everyone.  It’s a LOT. Figure out if you are feeling like this towards him or the wedding process and go from there. But please talk to your partner. Your answer will be in that conversation.
[jnjkbc3] (score 174, diepte 0) Honestly, yes. Getting engaged made it feel "real" and that scared me.

I wrote a list of all the reasons I had decided to marry him on the whiteboard in my kitchen. 

And I'm 100% certain those reasons are still valid. Yep, it's going to be ho-hum some days, but so am I. I'd rather face life with him than without him. I can't imagine Sunday mornings without him. 

I'm going to do this. And remember that I've had "cold feet " about all the big decisions I've made that turned out to be the right thing.

That said, I worked through the feelings you describe BEFORE we got engaged ... I wouldn't write them off. Be 100% sure.
[jnjfk3l] (score 152, diepte 0) If I am honest with you, this sounds worrysome. I don't think it's "just normal cold feet", because it seems like it is more about not being happy with the partner than not being sure if you're ready for marriage.

In most cases, your gut feeling is right and the marriages that start off wonky end up in divorce - it is just a question of how many years and how many assets-to-divide later it happens.
[jnjzf88] (score 132, diepte 2) Until I read this reply, I was trying to think of ways the 2 of you can figure this out as a couple.

But your comments here are downright alarming.  I don't think it automatically means a break up, but it does mean a postponement of the engagement.  Then get pre marital counseling.

If you find a good one, you will end up knowing which way to go next.
[jnjfigr] (score 124, diepte 0) Honestly? Never - despite how stressful I find wedding planning, it’s the actual event planning that has me stressed. However, you say it’s a new feeling. Could you be feeling depressed, generally speaking? Are there are circumstances in life you might be projecting onto your relationship? Have you been able to spend quality time together as a couple? Either way, whether it’s external circumstances or your actual relationship, it’s definitely something worth unpacking now rather than later.
[jnjhmbt] (score 67, diepte 0) I sometimes had feelings of intensity - like, woah, this is a huge life step - but never had a single doubt about my husband or marriage or our life together. 

From what you’ve shared, it sounds like wedding stuff may be surfacing existing feelings of doubt over whether this is that person you want to spend the rest of your life with. When I’ve had feelings of dread in the past, that was often a sign I was making a choice that reflected someone else’s desires for my life and not my own. 

Please seek therapy asap! You deserve support in figuring out where to go from here.
[jnjxeb6] (score 63, diepte 1 OP) We’ve had a handful of conversations about the state of things, but I haven’t come away from them feeling any better. I made the point once about how I’d rather end things now on relatively good terms and still have time to move on and meet other people, rather than in 10 years when we’re in a bitter and expensive divorce, and he said he’d rather take the chance and hope things work out and deal with the divorce in 10 years if it comes to that…which is a difference of opinion that maybe shows we’re not super compatible. But I so appreciate you sharing this experience—it’s given me a lot to think about.
[jnjsb61] (score 61, diepte 0) I don’t think you’re going to find a one size fits all answer here. Case in point: my therapist had to constantly remind me that when I’m stressed I start looking for what’s wrong/what I did wrong. Which often leads to me labeling something good as a mistake. So when I get stressed about the wedding, I jump to “this is a sign the whole marriage is a bad idea.” But that’s not true and when I calm down enough to look at the facts, I can see that.

Meanwhile, other people who don’t have this response will find it easy to say “if your gut says no, it’s probably no.”

So think about who you are as a person. What have been some other times you felt similarly and how can you use that to inform your cold feet?
[jnkdkhv] (score 60, diepte 1) Reading your response I was like omg did I type this? I was engaged at 24, and dreaded every week that got me closer the wedding. He was like “we should send out save the dates soon…” and I found every excuse to wait because I knew deep down I couldn’t go through with it. Eventually I did end it and now at 30 I just got married and every week that led up to the wedding I got more excited! And I’m the same way. I would rather hang out on the couch with my husband than go out most days - he’s my best friend.
[jnjtlmv] (score 60, diepte 1) As a person with trauma and anxiety, I can relate to this. I’m reading the responses as “if you feel unsure, it’s a no”, but I’m unsure of literally everything and have a tendency to over analyze and self sabotage, so, I usually don’t follow my gut lol. If I ran every time my gut said run, I would have nothing and no one.  My only advice to OP is to talk to a professional about the root of it. Is it the person you’re marrying that’s making you feel blah or are your feelings based on something else. It’s worth working through before throwing away a whole person.
[jnks2bw] (score 53, diepte 1) I think this comment is underrated and the big takeaway here is it sounds like it’s part of how you approach decision making and change. If OP often feels nervous about big decisions in life and has hesitation, I would take it as more part of the process. If they normally approach change with passion and excitement, that’s more a cause for concern
[jnjnb9z] (score 53, diepte 0) I have had a few moments where I’ve been freaked out by how “final” this all is - weirdly, the scariest time was when I was doing my tax return of all things. I realized that this would be the last time, ever, in my life, that I could check the box that says I’m single. No matter what happens after we get married, I’ll never check that box again - I can check married, divorced or widowed, but never single. Do I particularly CARE about government forms? Not really. But it just sunk in the finality and seriousness of this decision and that’s when I got into my head with my standard anxieties of “who let ME have this responsibility” - but I also have that about driving a car, babysitting a friends infant, etc. 

I have had a sense of dread about the event of the wedding itself, and half joke suggest that we should have just eloped and it’s not too late to do that, but that’s more about my anxiety of being the center of the attention, literally the wedding being the only thing people want to talk with us about, and our families literally going off the rails with weird requests/demands for what this event will be (mostly from my future in-laws). Despite the dread I’m feeling about ongoing drama with the stupid rehearsal dinner with my future in-laws, I am SO excited to be married to my future husband.
[jnjgtiy] (score 51, diepte 0) I have been engaged twice. The first time it was to “the perfect guy”. Everyone told me how amazing he was and how I was so lucky. We were together for five years. When it came to wedding planning, I didn’t want to do anything. I kept putting things off. Thinking about planning make me feel anxious and sick. I powered through planning and ignored my feelings of dread. Two months before the wedding he told me he was having an affair with my friend and left me for her. 

I’m NOT telling you this because I think your partner is cheating. I’m telling you this because after my life fell apart, i got into therapy and focused on myself. I soon met my now husband and everything was so different. Sure we argue like any couple but things with him are just… magical. I was so excited to get engaged, absolutely thrilled to plan the wedding, and I am over the moon that I get to spend the rest of my life with him. 

Long story long, I never experienced any cold feet with my now husband. Everything just felt right. Listen to your gut. Get a Therapist jut for you. Work out what you need. Start journaling. Don’t ignore your feelings. 

I know this is hard. I’m so sorry you are going though this. I know it’s overwhelming.
[jnjjten] (score 45, diepte 1 OP) Your first paragraph is so spot on to what I’m experiencing. We’ve been dating 4 years, moved across the country together, adopted two pets, and my whole family says he’s wonderful for me…but I’ve been doing the same thing with planning and trying to avoid the prospect of getting married. I think I know deep down what I need to do, but I’ve needed the reassurance that other people have done this and come out the other side happy.
[jnl744h] (score 39, diepte 2) It sounds incompatible, imo. You're not fuck-yeah enthusiastic, and you both should be. Dating is where you 'see how things work out,' not after marriage. If you're not thrilled, move on.
[jnjk4ht] (score 30, diepte 2) It’s like night and day. You deserve a life that you aren’t questioning. 

I really recommend meeting with a therapist to help you sort your thoughts. Again, I’m so sorry
[jnjgk6m] (score 29, diepte 0) Have I had moments where I was nervous about the wedding - yes, but have I had moments where I was nervous about the MARRIAGE - no. I think it's important for you to take stock of whether or not the marriage is what you really want, forever is a long time to feel ho-hum.
[jnk6bm8] (score 27, diepte 1) I love the pillow over the face 🥰 I might try that!
[jnko4yb] (score 27, diepte 1) I went through with that first wedding where I thought I was happy enough, though at least in hindsight maybe mostly happy that I was setting up my future (I thought). We got divorced three years later and luckily that was a pretty chill process, legally speaking, but I still put us through a lot emotionally because I didn't really listen to my heart. 

"When I think about the marriage, it feels sort of ho-hum, like “this will be pretty alright and I can live with it and be happy enough” but I don’t feel any kind of uber excitement or “wow, I get to spend the next 40 years with my person!!” happiness."

My first wedding & marriage were that ho-hum feeling. The wedding I'm planning right now, that relationship is 100% the second one. I would not set a wedding date, OP. You don't have to break up immediately, but I would hold off on planning a wedding, and make some counseling dates instead - alone and as a couple.
[jnjs00r] (score 14, diepte 2) Hey-I wrote that other long comment-this was us too…

Started dating at 19, he was 23, moved to a new city a year later, adopted two cats, finished college, he got a good job, he was “perfect.” Didn’t matter that I cried myself to sleep , he was stable and “going to be a good dad!”

I ended it at the 5.5 year mark with half a wedding planned. I cried each time I had to start planning and was told it was because weddings were stressful. Lol 

This time I only cried because his parents are awful people and my amazing husband is hurting from it.
[jnkxs3k] (score 14, diepte 1) Yeah I was going to comment the same thing. With my first marriage, I had cold feet for various reason, but I ignored my gut and went through with it. Divorced 6 years later. 

With my current engagement, I have not had a single second thought or even a moment of cold feet. I think society normalizes/dismisses cold feet way too much. There's a reason you're having those feelings, and based on my own personal experiences, I really believe that if you're truly happy in a relationship, you don't get cold feet.
[jnjn9p4] (score 14, diepte 0) I have fleeting moments where I am nervous about being married. Marriage is a legally binding contract. It's a big deal. Being married will change you in ways you don't know so the unknown is scary. However when the moment of fear of the unknown passes and when I think of marriage with my fiance, I am excited. We have plans for build a house and have a garden. I dream of having coffee with him decades from now, looking out at our garden. We plan to travel. I have a list of places I want to go with him. I think of future times we will have with our families during the holidays and I'm excited. We make a good team. There is nothing about being married to him that feels "ho hum." I would figure out if you are anxious about a big life change and doing something you've never done before or if you are just not excited about the person.
[jnk7ozi] (score 14, diepte 1 OP) He’s a great guy on paper and in-person: good job, responsible, goes out of his way to have a good relationship with my family/friends, has never done anything to make me question his loyalty/commitment. He treats me really well and tries to do nice things for me to make me loved and we can spend time together and really enjoy ourselves. But it feels almost…juvenile in a sense? That’s probably not the right word to describe it, but I don’t think he’s really examined what he wants out of life and whether we are compatible in all ways that we should be. I think for him marriage just seemed like the next logical step and that since things have been fine for a while, we can just keep on coasting like we have been. That might be why this only started after we got engaged—the seriousness finally hit me, even if it hasn’t hit him. Thanks for this comment, it helped quite a bit.
[jnkp0de] (score 12, diepte 1) Yes, this. My therapist has pointed out that I have trouble with committing to a choice. I feel safest when I have all possibilities before me, because if something goes wrong, I can easily pivot. I also struggle with change. I knew some cold-feet feelings would probably come up with my wedding, and sometimes they do. But at the end of the day, I can’t really imagine life without my fiancé and I am very excited for our future together. So I think the feelings are just my brain doing it’s anxiety thing. 


Because of this, I agree strongly with the comment above: for some people, these feelings might be a red flag. For others, they might be expected. I strongly recommend working through these feelings with a therapist rather than Reddit.
[jnkpoed] (score 11, diepte 1) Same here. We'd been together 10 years when he proposed; I was already fully committed to living the rest of my life with him. The idea of marrying him is exciting, and nothing will fundamentally change.
[jnmf7ky] (score 11, diepte 2) My dad always told me if you're not sure about the relationship, don't get married. Marriage is a piece of paper and it won't fix anything. Dating is the easiest it will be so if you're unsure and things aren't going well, don't get married.
[jnl4ig1] (score 10, diepte 1) I got engaged, the first time, right out of high school. He was in the Navy and was based across the country from where we grew up. I knew he was going to propose and I wasn't excited about it at all. My family went with his parents to see him that summer and he proposed. I accepted the ring and we went home a few days later. I knew I didn't love him, that I didn't want to get married so young and I definitely didn't want to move across the country. I ended it when he came home for Christmas and people were shocked. A few years later I started dating a great guy who I had known for a few years. We fell hard and fast and when he proposed I was so excited to say yes! We've had ups and downs. Lots of losses, financial problems, and we moved far away from our hometown. 

If you're having feelings that this isn't right for you it's time to take a serious look at what you want in a relationship. A couples counselor would probably help you sort out your feelings so you can make the decision best for you.
[jnjsi3i] (score 10, diepte 1) I had similar “woah” feelings, not about my husband but rather the big deal that people make it out to be, that it’ll be SO hard and your first year will be awful etc etc. but deep down I was still confident in us. I had those both right after getting engaged, and in the last few days leading up (but that was also mingled with stress about everything going smoothly lol)
(152 reacties met lagere score weggelaten)

=== THREAD 31mv1v ===
SUBREDDIT: r/Fitness
DATUM: 2015-04-06  SCORE: 335  REACTIES: 126
TITEL: If you or someone you know has pain when exercising... tell them to check their shoes!
POST (source_id=post):
So, I'm posting this here because I've had a life changing experience in the past month - and I would like to pay it forward by sharing.  It is common knowledge that using the correct type of trainer you use while working out is essential, but that is not why I am here.  I think this is something overlooked more often, which is why I'm sharing(here is your "wall of text followed by at TL;DR at the end" alert).

I'd like to start off by saying that I am actively inclined - I enjoy running around and playing games and I like sports, but as I hit puberty that stopped.  Even though I was not a serious runner, when I ran, even when I walked, I would get serious pain shooting through my shins (they tell me it sounded like shin splints), or pain in my hips and lower back, and sometimes my feet would cramp.  

I assumed that, since my feet are as flat as paper and my ankles have always rolled in, there was just something structurally different that made it hard for me to enjoy moving.  I've tried arch supports, expensive orthotics, even with most supportive shoe I could find, no matter what, the pain was ever present. I accepted the fact that my working out would take a different form, and worked through the pain I knew would eventually come no matter what I did, and did my best from there.  This is how it has been my entire life - it is why I have never enjoyed fitness or the work to achieve it - I don't mind the sweat, and I love the burn, but the pain that came - like my bones would break if I put too much pressure - it ruined it for me.

With the beginning of a new desk job and the start of a sedentary lifestyle (waitress to desk job), I decided that it was time for me to get moving again, pain or no.  While I've never been the picture of physical fitness, maintaining a healthy weight has always been a priority for me.  A friend of mine told me about a local specialty store - they were for runners and other athletes - and told me to check them out.  "It might be the type of shoe, you know," she said.  "They watch you walk and they can help you find the best shoe for what you need." 

I headed over - the idea that they could help me after the doctors couldn't help and countless hours of research to figure out why I was the way I was and how to fix it kind of made me laugh, but if I was going to spend $100 on shoes, better to shop locally and support my community - and worst case, I deal with what I've always dealt with.

Let me tell you ladies and gents, it was the best $100 I've ever spent. And it wasn't the shoe he picked (though that in and of itself is wonderful) - for the first time since I was 13, he measured my foot.  But not like it had always been done- he measured it TWICE. 

First, without weight, as I had been taught my entire life - both feet reading a size 7. All my shoes fall within a half size of this, it has been this way for a decade. However, he pulled the apparatus off of the pedestal, put in on the floor, and had me stand up.

Folks, my foot, when sized along with my body weight, measured a *size 9*.  Two full sizes.  A HUGE jump.  I balked. The numbers didn't lie, but I was skeptical - seriously? Two sizes? No way.  But when I strapped on the shoes it felt like walking on clouds, and for the first time, when wearing on the pairs he chose, I walked without pain.  I jogged, without pain. *I SPRINTED, WITHOUT PAIN*.  I was sold. 

Since this event, for the first month in the past decade, I have been walking outside every day.  It started slow, but I hit the hour mark today, and I a  still without pain, still without needing breaks, still without downtime in between days I go out due to residual pain.  It has been glorious.  I hope in another month I can move from walking to jogging, and one day from jogging to running, because I have always wanted to run long distance.  The idea of seeing how far my feet can take me has always been out of my reach.

It is out of my reach no longer - the only thing that is holding me back now is how much work I'm willing to put in.

I sincerely hope that one day I'll be able to go trail running or do a 10k with my friends, but for now, I'm happy that I can take my dog for the walk that he deserves and I can do it without my legs paying for it after.

That is my story - and I hope to be able to join you folks as I build a new lifestyle that includes a pain-free journey to fitness and health!

*TL;DR: For my entire life, but especially after I became an adult, running and walking has always been painful. Went to a specialty shoe store that not only told me I needed a supportive shoe for my flat feet (which I already knew), but that my feet needed a shoe that was two sizes larger than what I was wearing. Since the purchase, my pain has ceased, I have walked for the sake of walking more often in the past month than I have in the past five years, and I am looking forward to feeling the burn of dem gainz rather than the burn of my shins threatening to break in half.  It is glorious.* 

*I hope my story inspires people who have pain to not give up - but rather do the same and see if all they needed was a different size shoe.*

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cq31abl] (score 65, diepte 0) Honestly i can  not emphasise what you said enough. As someone who works at a specialty running store, soo many people come in and buy the wrong shoe for them due to price or aethstetic. A good pair of shoes will last you 5 times the length of a crappy pair if not more. By spending the extra money you are saving yourself money in the long run and preventing foot and leg issues down the  line.  BUY PROPER SHOES EVERYONE
[cq31vuc] (score 17, diepte 1 OP) Not gonna lie - I was a bit nervous about the size 9.  My mother and my cousin were made fun of my family for having big feet (we're a shallow bunch) when they were younger... i was spared because I'm on the upper end of acceptable.

I stopped caring. I'm walking, I hope to be running, and if it means I have big feet, then my big feet are going to be the ones taking me places!
[cq32q9v] (score 15, diepte 0) I'm lucky enough to have solid feet, but I found this even with specific exercises. I squatted barefoot (which was OK) for about a year, but one Christmas, I got a new pair of sneakers. Seeing as they were new and comfy and I wasn't thinking about special gear at the time, I started squatting in them.

Huge mistake. I lost 2 reps off the end of my 3x5, progress totally stalled, and I developed knee pain. Like, immediately. I didn't even figure it out for 2 weeks, and when I took the shoes off, everything came back. Turns out that bit about stability under load is important. I switched to converses and eventually squat shoes, and life is good: I just got 400# for reps last week. 

So, yeah, take care of your feet. It's easy for them to be the cause of issues they don't seem related to.

(Also, I could never run until I got VFFs. Love those things, no pain.)
[cq31h1l] (score 14, diepte 0) I hurt my lower back in my mid 20s.  It would occasionally agitate me and feel like its getting really bad again.  2nd winter afterwards, my back was doing pretty good.   Spring time came, and I pulled out a light pair of shoes I didn't wear all winter.  Went to the mall and after about 5 minutes of walking I could feel it tweaking my lower back some.   Tossed them that day and never looked back.

Foot wear is very important for every day.  Not just working out.
[cq3nds8] (score 12, diepte 0) Shoes are extremely important for all levels of activity. The best brands will offer shoes that are best suited for a supinated foot type, neutral foot type or a pronated foot type. Personally I find Asics excel in being able to match your foot type, asics also offer a great heel fit. 
New Balance are also great in having different lines of shoes for different foot types. New Balance although do not lock the heel as well as Asics, they are great in having different lasts (shape of shoe) and offer different heel to toe drops (heel drop). Heel drops should be considered in which activity your doing, for instance in running, eg: rear foot, midfoot, or forefoot strikers. 
Lastly, have someone with experience measure your shoes. With a Brannock  device, it measures your foot length and your arch length. A patient may have a size 7 shoe, but there arch may be a size 9. (Sorry hard to explain briefly). It appears op may have this with his overpronated (pes planus) foot type. Source I'm a foot specialist
[cq34gba] (score 11, diepte 3 OP) I wiggle my toes in my shoes and they're so happy with all the room they have. It's wonderful!

And they can all laugh at me when I cross the finish line at a half marathon - that is my goal before 30!
[cq3lc7e] (score 9, diepte 0) Good solid advice. But seriously, how can anyone possibly wear shoes that are **two whole sizes** too small? How can you even fit your foot inside?
[cq33xzc] (score 7, diepte 2) I have worn a size 10 since I was 10 years old and just bought a pair of 11s that fit better with my inserts for my flat feet. It's all good :) You go girl!
[cq3hdrr] (score 6, diepte 1 OP) I might be a freak, but if I help even one other freak out, my job here has done.
[cq3grwm] (score 5, diepte 1 OP) The store I went to is called "fleet feet" - they specialize in running and walking shoes. They're more personable and knowledge than your local dicks or foot locker because they're in the business of supporting athleticism, rather than promoting a bottom line.

If you can't find a local store, try looking online to see if you can find an online service that can do evaluations and provide product suggestions.  My friend mentioned once something along the lines of brooks?  She says they provide that. 

It might not be the source of your problem, but if you don't know what the source is, the best way to uncover it is to leave no stone unturned. Good luck!
[cq3n353] (score 4, diepte 2) I work at a specialty running store and believe it or not the most common size shoe we sell is a 9!
[cq3eb2l] (score 4, diepte 2) The one and only
[cq3vn8o] (score 4, diepte 1) Another vote for VFFs. Had horrific knee pain and shin splints in regular running shoes. Couldn't run 2 miles without my knees swelling. Ran a 10k in VFFs, and never felt better.
[cq44tmt] (score 4, diepte 2) You ever run in sand? The sand is soft and takes away the force you put down. A similar thing happens when you squat with an athletic shoe like nike shox or even roshes. Also, those shoes oftentimes have a padded surface that doesn't always match the contours of your feet, so you might distribute your weight differently. Your feet are more perfect than you think at putting weight through the heels. Barefoot/chucks let you squat with a 100% flat surface (always deadlift like this)  squat shoes have a raised heel with hard plastic that doesn't compress and typically the soles are made of special material you can mold to your feet (I put mine in the oven for like 20 mins per instructions  no joke). The raised heel can improve leverages. 



Hope this helps.
[cq3d5ja] (score 3, diepte 1) I played high level soccer for most of my teenage years and always struggled with injuries. When I was 18, I got better footwear both on and off the field. I also invested in a pair of orthotics. Within a very short period, my injuries disappeared. I'm now four years injury-free, where before I was injured about every eight months. Footwear is so key. Problem is now I'm a sneakerhead (for casual-wear at least)....
[cq3uwcv] (score 3, diepte 3) If you try, you need to learn to run the way as "intended" by evolution, which isn't the heel-first stamping that running shoes runners do. [Our feet are perfectly designed to dampen the impact with our feet](http://phys.org/news183817654.html)
[cq3zdu3] (score 3, diepte 4) I've read articles like that before. I just don't think I'd be able to run without pain. I like running, I'm training for a 1/2 actually, but I have always had pain when I run. It slowly starts later in the run if I start getting used to running but it is always there. Shin splints, killer ankles, and sometimes a sore knee if I am trying too hard to combat the ankle pain.  I have very supportive shoes but I still over pronate far too much. A doctor once said I have amazing arches they just disappear when I walk. I don't think I'd be able to run with no support at all
[cq461h1] (score 3, diepte 3) The point is to strengthen your own body to support itself. Starting slow is the right way to do it - some people buy some thin, low shoes and run a 5k and then can't walk for the next 3 days. 

I have personally seen a big improvement in ankle and foot strength since getting some minimal shoes a few years ago. I still like some cushion, but less "support" is definitely helpful sometimes.
[cq31rh0] (score 3, diepte 0) As an Athletic Trainer that also holds Performance Enhancement Specialist cert I could not agree more. Where I work the most common issue is shoes. They usually are a captive audience and cannot buy shoes. We give [these](https://sofsole.com/product/3-4orthotic) out like candy to adress any that were initially told the wrong shoe to purchase.


Even if you dont buy from that specific store for whatever reason, they will usually still point you in the direction of the shoe type your need. Great post!


(quick side note, the link above is direct to the site, I have no referral link or anything, and I am in no way affiliated with them beyond my group spending obscene amounts of money per year on them.)
[cq3ddfh] (score 3, diepte 1) Vibrams five finger?
[cq369q3] (score 3, diepte 1 OP) The gentleman I worked with didn't tell me anything I didn't know as far as what I needed - I know I have flat feet, I know my ankles roll - but he DID do an excellent job selecting what would be best.  I would have never known that shoes come as supportive as the ones he chose for me (which secure everything, down to where my heel is positioned).  I think that it was that service that he provided that allowed me to understand what it was that I really needed - something that may or may not be able to found online (I honestly don't know).

Also the fact that I could ask him my questions in real time - and his consistent assurances that yes, this will be a good fit for you - it made such a difference.  And I couldn't be more thankful.
[cq37f62] (score 3, diepte 3 OP) I think a lot of people also use their trainers as a fashion statement... if you compare the shoes of my childhood to those of today, they've almost become a statement in and of themselves.  The Nike Air (or anything that is both streamlined an attractive) will get the marketing money because people want to wear them to look good, and not because they perform well.

For those who are actually using them for fitness, it is a conundrum, but I sincerely hope that they are smarter than I and recognize that the pain that comes with poor shoe support means they need a better shoe.  I know now what I wish I knew back then  - disabling pain means something is wrong.  You might not know WHAT is causing the pain, but as long as you're feeling debilitating pain, you need to seriously consider every aspect of your fitness regimen to reveal the cause... and put an end to it, even if it means understated gray sneakers like I have! :)

Thanks for the suggestion - when I put my miles on on this pair, I'll head over there and take a look!
[cq3eo4r] (score 3, diepte 0) Whats a specialty store? Like what is the names of them? I might need to check into that. I get Shin Splints constantly when running in cleats. I think that's mainly because before working out I was 135 lbs, now I put on alot of muscle weight and weight 160, and running just hurts my shins for the next couple of days. I took some time off let them completely heal but as soon as I run again they really hurt.
[cq3i7wf] (score 3, diepte 2) Excellent, thank you for the reply. I'll be looking for solutions.
[cq3lnnd] (score 3, diepte 0) [The Brannock Device] (https://youtu.be/e77-iGq2oyY) or shoe sizer can be your best friend! 

Measure both feet, one is always bigger than the other.
[cq3uu2p] (score 3, diepte 0) dont ever squat in athletic shoes. barefoot or squat shoes or chucks.
[cq3vzy3] (score 3, diepte 0) I'm just a bit confused Did your feet fit both a size 7 and a size 9?
[cq42gla] (score 3, diepte 1 OP) Real question - how did you get used to wearing them? I've had mine (plaster casts, and $300 is on target) for years and years but for the most part they have been in the back of a drawer, because my feet never were able to adapt.

Any hints would be suuuuper appreciated, as I'm looking to start cycling them into use as I start doing more!
[cq43zf4] (score 3, diepte 3 OP) Okay, regarding wall of text: did you read my post? I'm wall of text queen.  I also like to read, so...

I have gotten a metatarsal cushion, but it was attached to my foot, and it was a pain getting it changed every two weeks. However, it did help...  

I will look into cycling as my cardio until I can build some strength, though, as reading through, there were some suggestions to actually do exercises to build strength in the arch and muscles of the foot (I didn't even know this was possible).  Maybe you could benefit from this as well.

I must wear heels at work (I wish I could wear trainers), but I will wear my inserts more often.  Honestly, feet pain I can deal with (there's no pain like the crushing of your toes for a favorite shoe), but it's the travelling pain, like you described... and once it gets to my back, it tweaks an old injury, and I'm down for the count.  That has how it has been since I got injured, and it is the specific reason I stopped exercising.  Feet pain is one thing, but not being able to walk really sucks.

Thank you for your advice, and if you're open to it, I'd be happy to forward along anything I find about building arch strength!
[cq34vi4] (score 2, diepte 4) You can do it! I'm not allowed to run more than a 10k per my doctor, but a half marathon would be so cool!

I have two screws in each knee and he isn't thrilled with me running a 10k but he said no more than 7-8 miles because of the impact on my knees with the screws.
[cq45xi0] (score 2, diepte 3) Every shoe fits differently too! I have shoes from 8.5-11 that all fit the same.
[cq3sa1i] (score 2, diepte 2) My ankles would kill if I tried that
[cq4bvqn] (score 2, diepte 9) Ouch.  Soccer.  Eek.  I love watching it, but I'll not play it, I like my ankles and knees, thanks.

I wanted to type out a huge essay with diagrams about biomechanics and all that shit, but I don't have time, and you probably don't have time to read it, so I'll just make it short and blunt (your "military" flair suggests that you have thicker skin than most).

The fact is that all this business about "support" and "pronation" and all that is a bunch of nonsense meant to sell shoes.  People's feet get hurt because they've been wearing shoes all their life and the connective tissues and muscles in their feet (yes, muscles in your feet), ankle, and calves are weak.  Hell, most injuries to amateur runners happen because amateur runners as a group are by and large, weak, un-athletic, and myopically one-dimensional in their approach to fitness.

Hell, most chronic back pain in this country happens because most people are weak.  They spend most of their lives sitting down, with chairs doing the job that their butts and back muscles are supposed to do, those muscles atrophy, then people wonder why those muscles are weak and unable to do their jobs.

Strength training isn't a panacea, but so many people are so fucking weak that it might as well be.
(93 reacties met lagere score weggelaten)

