# Label-batch batch_0094

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
Schrijf het resultaat naar `batch_0094.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 48mmwq, 565qp2, 12iqh9o).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 48mmwq ===
SUBREDDIT: r/AdvancedRunning
DATUM: 2016-03-02  SCORE: 16  REACTIES: 89
TITEL: Winter of... /u/VincentClortho - March 2nd 2016
POST (source_id=post):
Hello again everyone. Another Wednesday interview. This time, /u/vincentclortho answers all. Like always, share your latest and greatest training, ask any questions you might have, or participate in general discussion. Join in on the fun!

* In an effort to combat the recent spam epidemic going across reddit as a whole, submissions are encouraged to be self post only. The spam filter is set to automatically take down any links but we can approve them manually. If you'd like to submit something, right now text post is the way to go. 

_______________________________________


**How/when did you start running?** 

> My love affair with running started six or seven years ago embarrassingly thanks to a saddle sore that I got from cycling. I had been an avid cyclist for around five years at that point and not being able to sit on a bicycle saddle was driving me crazy. During a walk with my dog, I must have just been boiling with pent up energy, I started running. It felt amazing, and I didn’t want to stop. It was runner’s knee that forced me back on a bike, as I was unfamiliar with the discipline needed to build up on running. A few years later work and life started making 4-5 hour training rides near impossible, and I became really frustrated with cycling. Running, with it’s 30 - 90 minute workouts, once again became ideal for me, and I’ve been much more a runner than a cyclist ever since.

**PRs?** 

> This year will be my first attempt at another distance besides 5K, so it’s unfortunately all I have. I just got a new PR the other day of 19:00 flat. I’ve got some other local trail race PRs that probably won’t mean much here.

**Favorite shoes to train or race in?** 

> The North Face Ultra Trail is my favorite all-arounder. The name implies that it’s trail specific but it really isn’t. The tread is pretty low profile and close together, so it feels equally at home on roads and hard packed trail. On the trails the small tight tread performs like velcro. On the road it’s flat profile and minimal midsole make it a very natural feeling shoe by allowing my foot to move and flex the way I feel it should. I definitely will race trails with this shoe but when it comes to road races I switch to a pair of Mizuno Wave Universe racing flats. This shoe is maybe a little too awesome for a guy at my speed but they definitely help. I wouldn’t have spent the extra money on these but a friend of mine won a contest against the owner of Running Warehouse, the loser had to hook up the winner. Since my friend wasn’t a runner he asked me what I wanted.

**Favorite weather to train or race in?** 

> By all accounts it’s not ideal (especially given the Olympic Marathon Trials this weekend), but I love hot weather, 70s and up. Running as close to naked as possible and feeling the sun on my back and neck is my happy place.

**Next Race?** 

> Go Green Saint Patrick’s 5K. I haven’t run it before but it goes around a lake in a park I love and falls in a time that fits into my schedule.

**Goals this year?** 

> I desperately want to break 19 minutes. I’m at the tail end of the competitive runners in my area and it’s driving me crazy. I tasted high overall placing last week and I want more.

**Proudest Accomplishment?** 

> I got third overall in a trail race last year that was slightly over 5K. It basically went straight up 800 feet and down. There were some fast people in the mix and I wasn’t sure what to expect out of myself since I’d never run those trails. It was a fierce race with a lot of back and forth, people right on my heels, passing others who went out too fast, and an epic high speed downhill battle to the finish. Super dramatic, action packed, and fun.

**Things you do outside of running?** 

> Cycling mostly, although that’s fading fast. It was such a big part of my life, and I work in the bicycle industry, it’s hard to give it up. I’m also an aspiring graphic designer/illustrator, so I work on that a lot. I’m kicking myself that I missed the opportunity to contribute to the ARTC singlets. Oh well, maybe next time.

**Things that interest you outside of running?** 

> Music and books are what I turn to a lot to round out my life. I played in rock bands for a lot of my youth, and I still am very interested in what people are able to do with sound. Currently I love the bedroom producers that seem to be the new guitar heros. Air, Menomena, Hippie Sabotage, Dan the Automator, Holy F**k. Books, I’m in primarily a sci-fi guy though I’ve been on a Raymond Carver kick for a bit now. I think I’ll have to change it up though cause, man that dude is depressing.

**Favorite subreddits?** 

> I’m pretty one track minded right now on Reddit and /r/AdvancedRunning is without question my go to. It along with /r/Running has given me so much insight into running and training. I’m pretty lazy otherwise and just rely on front page to tell me what’s interesting to look at. I don’t know why I still look at /r/WTF but I do.

**Origin of your username?** 

> Ghostbusters

___________________________________

**Race Report Summary**

* [Hyannis Half Marathon](https://www.reddit.com/r/AdvancedRunning/comments/48d2m6/race_report_hyannis_half_marathon_xpost_from/) - /u/c10layman


______________________________

**General Questions:**

1. [A good profile on Oklahoma State Runner Josh Thompson.](https://www.reddit.com/r/AdvancedRunning/comments/4813rl/meet_the_most_interesting_man_in_ncaa_running_hes/) Would you rather be able to break 4 in the mile, or dunk a basketball?

2. If you hadn't seen, Luke Puskedra's (recent 4th place in the Olympic Marathon Trials) daughter was diagnosed with cancer. You can reach out and help via the [GoFundMe site in the linked post.](https://www.reddit.com/r/AdvancedRunning/comments/47idly/professional_marathoner_luke_puskedras_daughter/) If you followed along, it seemed like every notable professional runner chipped in with words of encouragement and a donation of some kind. What is your favorite thing about the running community?

3. And the flip side, what is your least favorite thing about the running community? Anything you dislike about your fellow road warriors, track teammates, trail titans, cross country compatriots?

4. [This was a pretty thought provoking post](https://www.reddit.com/r/AdvancedRunning/comments/47n3zy/lack_of_minorities_in_distance_running_in_the/) from /u/sartelo. Do you think running has any more barriers of entry compared to other sports? What sets running apart in terms of popularity from the larger sports that other people participate in? 

5. Anything else you'd like to add?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d0ktng1] (score 12, diepte 0) 1.) I'd rather run a 1:35 half right now :). 

2.) Our running community here is similar. Recently, a lady who runs a lot of races and does triathlons was diagnosed with cancer. As soon as people found out (she shared on Facebook), we got to work arranging rides to her treatments and collecting money to buy her a massage gift certificate.

3.) I really hate it when people don't support the slower runners and back of the packers (BOPers). Everyone's a beginner at some point, I think races should have generous course limits (as generous as possible considering permits and staffing). I was recently at a local 15K with a 2 hour course limit that WAS NOT ADVERTISED and they closed the course on some runners. That really saddened me. I stuck around to see a few finish, but I think they could have had a longer limit, or at least advertised it so those runners could have signed up for the 5K instead.

On the flip side, I do not like the "fast shaming" that sometimes goes on. I respect anyone who gets out there, even if their goal is to complete a distance and don't care about the time. However, those runners should also respect that people at the front do hard work too. I don't think anyone in the front thinks someone who spends 6 hours running a marathon is taking away from their own achievements. Most of the speedsters are just... fast... and don't really have an attitude. I know several runners who tout over and over that they are slow, though. It gets old. 

4.) I think running in a rural area is much harder. When I used to live with my parents, I wanted to run the rural roads but people would always stop and ask if I needed a ride because no one there ran. Also, I was scared something could happen, and no one would know. Another obstacle in rural areas is the lack of a local running store, gym, or even a grocery store with healthy options. The county where my parents live does not have a running store, gym, or even a Walmart. They have a local "mom n pop" grocer and that's it. No running races. It's quite sad. 

5.) Not really but I love this thread each week! And congrats on the Hyannis half! I read the recap earlier this week.
[d0kteq2] (score 11, diepte 0) 1. Sub-4 without a doubt. Not even a question to me. As a HS runner, my life revolves around the distance races on the track and sub-4 is the culmination of track running, IMO.

2. Definitely just the general community. I know pretty much everyone who runs at my level from the surrounding high schools, and I'm good friends with quite a few. When we're racing, we're racing, but after a tough race we're bent over our knees together. There's a great sense of camaraderie and togetherness. I think it comes from that shared understanding of the challenge of training and racing.

3. The focus on marathoning. At this point I've got no desire to run one, and it's quite possible I never will. I love racing on the track, and I like short road races. After I graduate, I want to tackle a competitive 10k and eventually a 10-miler/half marathon, but right now I don't have plans for a marathon. I get that it's a tough distance, and I'm not opposed at all (I'd love to run a fast time, maybe it ends up being my niche), but I dislike the focus on it. Completing a marathon at >5hrs off of 20mpw shouldn't be seen as greater than running 80mpw to run 14's/15's in the 5k. Just my personal opinion.

4. I think that running in general is widely accessible (in terms of 5ks and fun runs and the like), but being competitive in hs/college depends so much on your location and socioeconomic status. Two high schools around me have fantastic distance running traditions, whereas my school has gone through three xc coaches in 4 years and four track coaches in 5 years, and no tradition at all. It's not really possible for me to attend those schools, but if my parents happened to live in that district I'd benefit from the coaching knowledge and multiple runners at and above my level. I know I'd be better if I had trained with one of those two schools for the past six years.

5. Wow. Feels like all my mini running rants came out just now! Onto a happier note - running is going well and track starts this coming Monday!!
[d0kve6m] (score 10, diepte 0) /u/VincentClortho, that's really cool you're reading Raymond Carver. I have a particular pet peeve that I'm not often able to express, which is that I don't think Murakami deserved to name his own book *What I Talk About When I Talk About Running* because it makes no sense in the context of Carver's book, and because in my opinion Carver is a much better writer. If you find him really depressing (which he absolutely is) but still like him, check out (if you haven't already) people like Tobias Wolff, George Saunders, or Stephanie Vaughn. Wolff's writing style is not quite as abbreviated as Carver's, but it's still in the same vein, and Saunders seems like an absurd extension of that. Vaughn is more verbose but is very wistful in a similar way. Oh! Denis Johnson, too. Very gritty, very matter-of-fact, really exciting short stories, though I'm not really a fan of the novel of his that I read.

1. Is that a real question?

2. The SINGLETS. I love mine.

3. File this under crazy but true: I often find people in races who are willing to completely blow by me during a race and actually cross a finish line in front of me. Anyone else have this experience? It's amazingly rude.

4. That was a great post that I'm glad generated good discussion. There is a definite lack of minorities in distance running. I have a lot of thoughts which mostly eventually reach back to institutional racism, but I'm trying to keep this Q&A light and breezy.

5. My work run club started up again this Monday. We had a great turnout for a 5k around a local lake--I hope it keeps up. OH AND edit: where is /u/pand4duck?!?
[d0ksn0b] (score 9, diepte 0) Well, someone just won the "origin of your username" contest...

1.  Break 4.  I don't think you can just naturally break 4, so it signifies work.  A lot of people can dunk just on natural talent, so it seems a little hollow to me.  Looks really fun though, probably more fun than running 4 laps balls out.  
2.  I think it is great that everyone is supportive.  
3.  On the flipside, I hate it when someone is an ass, gets called out, and then complains "but runners are supposed to be cool and supportive".  Stop being an ass and I'll be more supportive.  
4.  I think there are some huge socio-economic barriers to running, especially to competitive HS running which is the first step to competitive running.  To be really good, you have to sacrifice a lot of time to training.  This is a lot easier to do if you don't have to work a part time job to help feed your family.  Especially when the pay off is what - a shot at a quarter scholarship to a school you have to qualify for academically for anyways?  If you are going to play the athletic lottery, play for the big prizes.  So I think it is a lot easier for a typical suburban family to support a runner than a typical urban or rural family.  Running is pretty much a country club sport.
[d0ktyvh] (score 9, diepte 0) 1. 4 minute mile, no doubt. There's a lot more people that can dunk basketballs, so the 4 minute mile is the greater achievement. 

2. I like that the sport encourages comraderie. You can run in the same races as the best in the world. 99% of runners are not going to win the race, so you can connect with people while doing it. 

3. It's hard for some people to avoid elitism. Just look at letsrun. Too many people want to be the lord of their little kingdom and shit on anyone below them.

4. I think the only real barriers to entry are social/psychological. Too many people in minority communities see it as a "white" thing to do. Also, I suppose having free time is important for a sport that you need to spend hours at every week in order to improve. 

5. Ran my LT intervals in my new ARTC singlet. [Moooooose!](http://i.imgur.com/gbtOI4I.jpg)
[d0ku3hh] (score 9, diepte 0) 1. Not sure if you'll get anyone on here saying the second :P

2. The level of camaraderie among runners is actually something I don't see too often in other endeavors and I wonder if there's something about running that tends to bring that out (perhaps the shared camaraderie of a goal that also results in pushing yourself to relatively extreme levels physically/mentally?). I've run in various locations (each for at least a few months) and each time I've met some awesome people to train with, and it's also people I've generally stayed in touch with or wouldn't find it awkward to talk to even if its been a while. There are a number of people I've run with over the years who I know I could call up if I'm ever in their area (and vice versa) and we could go for a run/just pick up where we left off. I've actually been (quite literally, on a run) running into some people I hadn't seen in a while and it's been a reminder of how many people I've been lucky enough to meet over the years and how seamless it is to maintain that connection. 

3. I got to thinking about this because of one of the discussions we had on here recently, but I'm not a huge fan of how commercialized running has become. It's not just all the new running gear and fancy watches but also the expensive races where people have come to expect their finisher's medal, t-shirt, etc. It feels like just in the past few years the prices of races have gone up a lot, because of throwing in all these "goodies", just because they can, etc. It's nice that more people are getting into running but I definitely have a preference for the "back-to-basics" races where the prices are kept low and you're just there to run a fast time. I just have a hard time bringing myself to pay $30+ for a 5k race.

4. Piggy backing onto #3, I think this commercialization has definitely hurt lower socioeconomic classes when it comes to getting into running. While the actual barrier of entry isn't high in terms of not needing a lot of equipment, etc., there are of course other factors that go into play (some of which I highlighted in a reply to that post). With that said, I think running and maybe soccer might be two of the only sports where you see some of the developing countries do well in - I think that speaks to some level about the accessibility vs. other sports. I've actually met some runners in such countries, and what's interesting is while sports like tennis, swimming, etc. had more upper middle class/upper class people/white collar types (because accessibility to the pool, the courts, etc.), some of these runners were of the working class (i.e. blue collar types) (and not everyone spoke English unlike the other sports).
[d0kt0yz] (score 8, diepte 0) /u/VincentClortho have you read any Asimov? By far my favorite scifi author. Also I'm glad that I'm not the only person that loves running in hot weather.

1. I would rather be able to break 4. It's a more elite club, although it's not as impressive to the masses.

2. I like that professional runners will run with fans (although Merber never responded to my invitation when he was in Florida). There aren't many sports where the professional will practice with amateurs and I think that closeness between the elite and normal people is really cool.

3. I don't like the disconnect between average runners. It's strange to me how often when I'm running and I say hello or wave at another runner I get no response. 

4. I don't think running has many barriers, but the point of places to run really made sense to me. Unfortunately communities in the US are mostly segregated and it's sometimes dangerous to run in certain communities. Cycling has the same type of problems as running. If someone in a poor community saves up to buy a bike to train they have to worry more about someone stealing their bike or hurting them while they're out training. However, track clubs and school track/cross country helps to overcome these barriers.

5. Apparently the singlets were so cool that the mailman stole mine. My singlet has been out for delivery since Monday morning with no further updates posted. I had to contact the USPS and get them to open an investigation into what happened.
(84 reacties met lagere score weggelaten)

=== THREAD 565qp2 ===
SUBREDDIT: r/running
DATUM: 2016-10-06  SCORE: 202  REACTIES: 88
TITEL: One Year With Plantar Fasciitis
POST (source_id=post):
Hi /r/running,

For the past 12 months, I've been on an uphill battle again Plantar Fasciitis, but I'm finally back up and running. I decided to write about my experiences in the hope it being useful to someone in the future.

> **tl;dr: [This table](https://i.imgur.com/2aJnaJv.png) is a summary of what helped, what didn't help, what I believe made things worse, and what I didn't try at all. If there's one thing to take away when it comes to Plantar Fasciitis, it's that there is no golden ticket to fixing it. What worked for other people didn't always work for me, and what worked for me won't always work for others. Your doctor is probably the only person you should trust on this matter, and I'd advise consulting one with some relevant experience.**

07:55 AM on Thursday August 27th 2015 was the precise time my left foot gave up on me. Strava Flyby replays me hobbling to a halt at the beginning of what was supposed to be a gentle vacation jog through the countryside of southern Poland.

The reason for my abrupt halt was a stabbing pain underneath my left foot, as if I were repeatedly standing on a power plug or a Lego brick. I’d felt this once before, a week before my first Half-Marathon in February 2012. I was new to running at the time but knew a red flag when I saw one and took it as a sign that it was time to back off. On that occasion, I healed up fine after a couple of weeks and thought no more of it.

I presumed this would be much of the same. I’d use the remainder of my vacation to ramble rather than run and by the time I got home it would be business as usual. How wrong I was. Over the next 12 months, the stabbing pain would grow to be accompanied by throbbing, dull aches, muscle spasms, and through stupidity on my part, it would make it’s way from my left foot into my right foot. I'd uncover a wealth of information and contradictions on how to treat what I came to know as Plantar Fasciitis, an injury affecting one ligament amongst the intricate structure and biomechanics of the foot.

Through until this summer, I tried [many things](https://i.imgur.com/r3mGuRv.png) to get back to full mobility with limited success, before finding a combination of remedies which worked for me. This write-up aims to go over my build-up to the condition, the subsequent year of trials and tribulations, what specifically helped and didn't help, and where I go from here.

###The Higher You Climb...

In 2011 I weighed 219lbs and had partaken in no athletic endeavour since secondary school. Life was a grind of work, pub, sleep, repeat, with my closest involvement to sport being the ritual weekend pub crawls to Elland Road prior to Leeds United games. One October morning, I went all-in and called it quits on alcohol. A month later I joined a gym, another month later I started running, and by February 2012 I'd ran my first half-marathon around the punishing hills of Jerusalem.

Between then and August 2015, I built up a respectable fitness foundation and shed around 60lbs, getting my resting heart-rate down to a similar number and my BMI firmly where it belonged. I slowly reintroduced alcohol back into my diet with more moderation, usually as a celebratory reward or at Christmas time rather than any kind of weekly norm.

I had the time of my life travelling the world, from Middlesbrough to Macedonia and Newcastle to North Korea, just to run road races. When I reached my goals in running, I start cycling, then swimming, before combining all three disciplines in triathlon. I'd relish the opportunity to push my fitness to new levels under the guidance of the brilliant trainers at my gym and running club. I felt in the shape of my life and considered myself anything but injury prone.

###…The Harder You Fall

A month prior to my vacation in Poland, I completed the New York City triathlon and felt confident enough to progress towards Ironman. I duly signed up for my first 140.6 and drafted a 12 month training schedule.

Between registering for the Ironman and departing for Poland, I ran a slow and steady 21 KM. The aim of the run was to finish with enough energy to continue towards the full 42 KM somewhere down the line. The run itself felt fine, but afterwards, my left foot felt unusually sore. The feeling subsided a few days later and I wonder whether reducing my pace that evening engaged some new mechanics that my body wasn’t used to, setting the stage for injury. Although it could just be a red herring, it sticks in my mind because of it's proximity to Poland.

Vacation time ticked around and the [stunning Ojców national park](https://i.imgur.com/pwVDPD4.jpg) looked like a great place to get in some hill-work. The morning of my run was no different to any other: a few stretches whilst waiting for my watch to pick up GPS, and away into a steady pace. The pain struck hard. I remember reading once that if you feel a small niggle or discomfort, continue to run for 20 minutes to see whether it passes. There was no way I could run for 20 seconds, let alone 20 minutes.

You read a lot of advice about building up to running longer distances or faster paces but never anything about slowing down. I hope this story provides food for thought for anyone else considering doing the same thing.

###RICE Time

After returning home from Poland, I rested for a week or so but noticed little difference. Hobbling became the new walking and I began taking the bus to work in lieu of making the two mile round trip by foot.

Working a desk job in IT, I had plenty of opportunities to practice the commonly prescribed R.I.C.E. routine: Rest, Ice, Compression, Elevation. Work even started out as a welcome distraction from being unable to embark on my regular morning jogs, but not being able to kick off Sundays with a long-run became disheartening. On those days when I used to run, I would clock up around 30,000 steps per day. Now I was barely reaching 5,000. 

Time ticked by and to my horror, the scales began to tip in the wrong direction and my fitness began to diminish. Gym cardio such as the bike and rowing machine were too painful to train with, so I ramped up my swimming instead. I clocked up 156,481 metres in the pool by the end of 2015, but at no point did it come close to endorphins and DOMS of a good run or brick session.

As the weeks became months, I challenged my perception of the pain. Was this simply mental rather than physical? How could a foot injury last so long? I decided to try put mind over matter and started running again. I re-joined my running club for some functional strength training too.

After explaining my symptoms to the coach, she immediately recognised it as Plantar Fasciitis. Her tone was enough to tell me I should be worried, and she strongly recommended seeing a doctor. A few weeks passed with no improvement, but I persisted, continuing to run and attend the training sessions. “What was that thing you mentioned again? Plan… tar…?”, I asked with more intrigue.

###Ok Google. Seriously. How do I fix this?

Work became busier and life kept getting in the way of seeing a doctor. I at least had the sense to stop trying to run through the pain, and I turned to the internet to find out more. I was astonished to discover just how common Plantar Fasciitis is. I couldn't believe I'd never heard of it before. The sheer wealth of contradictions on how to recover from it told me that this wasn't going to be an easy journey: Ice or heat, barefoot or strong shoes, stretching or resting... the list went on and on.

I first read positive things about something called orthotics. Insoles for your shoes, they are shaped in a way which supposedly support the plantar, and £25 later I had my own pair. They felt terrible from the start. The arches pressed so hard into my feet that they felt as though they were doing more harm than good. I persevered, wanting to believe what I read online, but finally resigned on them as a waste of time. 

Christmas approached and I departed Sweden for England. With time to relax and unwind, I made it to a doctor. Although she agreed with my coach’s diagnosis, she was unimpressed that I’d tried to fix things by myself. Since I didn’t have a high foot arch to begin with, the orthotics had probably made things worse. What I ought to have been doing, she said, was applying ice to reduce the swelling and getting lots of rest.

Resting I was happy to continue on with, but the quantity of ice she recommended was far more than I'd been using so far. I picked up a big block ice wrap from a local chemist and got to work: 20 minutes several times per day. A few weeks went by with no results and Christmas morning had an air of gloom about it as I realised I wouldn’t be able to run my traditional time-trial around the hills of Northumberland.

Thoroughly fed up with the situation, and against all common sense, I decided it would be a good idea to try go for a jog. About five minutes in, I felt a familiar stabbing pain… in my other foot. I immediately knew I’d just introduced my right foot to the wonderful world of Plantar Fasciitis too.

###Hot & Cold

I saw out 2015 by not moving a great deal and taking public transport everywhere. By the time 2016 came around, with it came a trip to Spain. I’d registered to run the Torremolinos Half-Marathon almost a year earlier. Long given up the idea of being able to run 2 KM never mind 21 KM, I headed to Spain anyway for some sunshine and to cheer on the runners.

Rambling from resort to resort, I began to notice my feet were feeling much better! Sticking to Cerveza Sin Alcohol, it certainly wasn’t any alcohol numbing the pain. It was genuine relief. The more time went by, the better I felt, and I even managed to get out for a comfortable one mile jog along the beach-front. Could all that slow walking have helped? Was it placebo in the form of sunshine that brought happiness to my feet?

I think either could be true, because when I returned to the -17 C abyss that was Stockholm, the regular pains came straight back - worse than ever. Sleeping became difficult as I felt every heartbeat through the bottom of my feet and I deferred myself to a second doctor.

Doctor Two was an experience to forget. I explained my situation, what I'd tried and been told from my previous doctor, and he barely said a word the entire time. If there were ever an advert for not spending 200 SEK to get an appointment with a doctor in Sweden, this guy was it. In the end, he mumbled "steroid cream" and "12 months". My heart sank. 12 months on top of the 6 months I'd already struggled through was not what I wanted to hear. Steroid cream was something I was unimpressed about too, having read worrying studies about dangerous long term effects of cortisone.

I declined the doctors prescription and decided to refocus on my morning swims. I broke and re-broke PBs on mind numbingly long distances, but the weight barely shifted. I delved deeper into online communities and was shocked to find people who'd suffered with Plantar Fasciitis for far longer than what my doctors had predicted.

Around the same time, my partner - who was facing her own uphill struggle with Achilles tendinitis - spoke to a doctor who recommended calf raises as the best treatment to solve all lower limb ailments. She confirmed that he believed it would help Plantar Fasciitis too, so I gave it a try. After several weeks trying both bodyweight and weight assisted calf raises, neither made a blind bit of difference and it was back to the drawing board.

Through until this point, I'd mainly been wearing my running shoes in tune to the theory that they supported my feet well. As they began to wore out, I picked up a pair of strong Salomon trail shoes. The heel section and sole were extremely firm and my feet felt even more supported than the lightweight trainers I'd worn prior. Whilst it didn't feel like it at the time, I believe this would go on to become one key factor in my recovery.

###Summer Time

Spring soon came around and with it an opportunity to relocate from Stockholm to New York. I accepted and come June I made my way across the Atlantic, running gear and all. In my first month in New York, the weather was nothing short of glorious sunshine, and I ended up [walking over a half a million steps](https://i.imgur.com/cEY1tkf.png), or as Garmin Connect estimates, 250 miles. I began to notice something, or rather stop noticing something: My feet hurt less and less!

The more I walked, the better I felt. I realised that all that walking in the sunshine around Torremolinos couldn't have been a placebo. I joined the city's recreation centres and took part in early morning endurance swim competitions, and found my weight was going in the right direction for the first time in the best part of a year. My fitness was coming back too!

Around the same time, I read positive comments online about two things I hadn't yet tried: Firstly, calf stretching (both gastrocnemius and soleus) and rolling, and secondly, foot splints.

I searched Amazon for the highest reviewed foot splint and gave it a shot. Much in the same vein as the orthotics and ice packs, the foot splint was very uncomfortable and brought no relief. In contrast, after discovering the excruciating pain of rolling out one's calves on a foam roller, my legs felt stronger and my feet felt firmer and I did my best to keep it up.

With my confidence being restored and often clocking upwards of 25,000 steps per day, I decided to give the treadmill a try. One agonizingly slow 12 minute mile later, I hopped out of the gym and immediately gave my feet an ice cold shower. I felt as though I'd ran a marathon!

It was hard to believe that a year earlier I'd been pounding the streets of Manhattan in a triathlon, and here I was barely able to finish a pedestrian mile. But it felt amazing. I'd just ran without pain for the first time in almost a year, and as apprehensive I was about any aches that might follow, things felt good. I was on to something.

###Knowing when it's time to start running again

My feet certainly weren't 100% by this point. Although the pain in the plantar region specifically had subsided, first thing in the morning was a new kind of pain: pins-and-needles type tingling underneath the back of the heel. I read online that a tingling feeling in the heel was symptomatic of nerve damage. Having got this far, I tried not to worry and persisted with what was working: Stretches, foam rolling, and the long daily walks.

A few weeks passed by and thankfully the nerve pain subsided. I kept up my daily routine, starting my day with long-distance swims and walking at least 5 KM throughout the rest of the day, then added a short 1.5 mile jog once per week. Those runs were some of the hardest but most rewarding of my life. Barely being able to run a sub-10 minute mile after previously having a PB of almost half that was a big shock, but also one that I relished: Now I was getting to experience the wins of fitness levelling all over again :)

###Post-Injury

Since starting those short jogs, I've also began building up endurance on the gym bike, and I'm happy to say that I'm up to running five miles at a time. I even ran my first race of sorts, a fantastic American equivalent of the great Parkrun series called OpenRun, with the same comradery and community spirit as it's counterpart. It was an emotional reminder of what I'd been missing out on for the past 12 months.

My plan now is to continue to build up again slowly, reminding myself to continue the gastrocnemius/soleus stretches and foam rolling every day, and to not run before I can walk, figuratively speaking. I realise that's easier said than done and I'm already finding it a challenge. I pushed too hard a few days ago on a flat 5 KM out-and-back and felt a clear warning sign in my right foot, which is precisely the kind of signal I need to heed. However, after [clocking up five 5 KMs](https://i.imgur.com/NeHrpTo.png), my cardio at least feels like a world apart from that slow jog on the treadmill a month ago.

As a modest short term goal, I'd love to clock up 100 miles by the end of the year. Bearing in mind I'd only ran 9 miles before August alongside a total reboot of fitness, I'd be over the moon with that. Looking any further ahead might be tempting fate, so I'll let 2017 bring whatever it might bring.

To anyone reading this article who has Plantar Fasciitis: There were times throughout the past year when I thought I'd never be able to run again. I would read articles just like this one and try everything to get back to full fitness. The more I tried, the more disheartened I'd become when I'd wake up and go to sleep each day with the same pain. But as I hope I have shown, there is light at the end of the tunnel. Granted, it's a long tunnel and you might find your fix neither here nor even from your doctor, but you will figure it out, and *you will run again*.

If you have any questions or just fancy a chat on this subject, don't hesitate to comment or send me a message and I'd be more than happy to help however I can.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d8gljf9] (score 16, diepte 0) I've been going through a similar process. Insoles hurt more than they help because they change the way that I walk. Strassburg socks might be helping, or they might just be making it hard to sleep, I can't tell. Luckily, I can still run without pain, it's mostly afterwards that my plantar fasciitis strikes. It's ridiculously frustrating, especially since the time scale of healing is so slow that it's nearly impossible to tell what helps and what doesn't.
[d8gvxbb] (score 8, diepte 0) If you're having plantar fasciitis - please go see a physical therapist and find one that uses Graston! I treat plantar fasciitis all the time, and with the graston, joint mobilization, stretching, and other exercises, it does not need to last this long!
[d8gmgge] (score 6, diepte 0) I was out for 4 months with PF. Calf raises and rolling my foot seemed to work.

My biggest problem was ignoring the pain to start with, which made it far worse.
[d8gm0wy] (score 5, diepte 0) I got a shiatsu foot massager thing with the hot/cold modes for under $50. I've been massaging it everyday for a year and haven't had plantar since suffering from it all of last summer. I would get that morning pain. I've been running 40-50 mpw for a year with no issue. Foot massage and changing shoes is what got me past it.
[d8gidnk] (score 4, diepte 0) This is great, thanks for posting this.

I've recently had some PF. It was pretty painful. I threw away all my shoes and got new ones. Bought some Stability runners and rolled my foot every night. I also did the ice thing and wore my shoes all the time as well for support. I took about 2 weeks off from running and have started to slightly get back into it. Maybe 10mpw right now and my foot seems ok. Although my foot still does get sore, now it's towards the front of my foot while with the new shoes the ball of my foot and in my arch feels OK.

I'm fat too so that doesn't help. I'm already a slow runner and this has caused me to slow down even more to avoid the pain. 

Again, thanks for posting this it's nice to see all your thoughts on it and the chart thing was great.

I appreciate it.
(87 reacties met lagere score weggelaten)

=== THREAD 12iqh9o ===
SUBREDDIT: r/Military
DATUM: 2023-04-11  SCORE: 612  REACTIES: 80
TITEL: For every 1,000 American draftees in 1917, 443 were fit for service (44%) and 557 were rejected: 273 had bad feet/joints, 67 had bad eyes/ ears, 61 had Tuberculosis, 60 had VD, and 56 had heart/ blood conditions, and 40 were rejected for other reasons.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jfurvq2] (score 319, diepte 0) This is one of the reasons why I don't wig out as hard when those articles about how few Americans are fit for service come out.  The bar was very low for most of the 20th century (especially when it came to education...) and it was still like, only 40% pass rates for a world war when shit shovel operator was a viable MOS.
[jfux53g] (score 270, diepte 4) Oh I noticed the Air Force tag and just assumed you were unfamiliar with military service.  My bad.
[jfutgxs] (score 140, diepte 2) Your aptitude scores for infantry  are actually reasonably high, especially now as you're expected to be able to do a lot of physical shit with like 80+ lbs of gear on, and operate a fair amount of complex stuff like radios, weapons optics whatever.  Not rocket scientist stuff to be clear, but you have some standards.

In the World War era there were entire units dedicated to manual labor, or jobs in the Navy that amounted to "open this valve when chief yells at you!" levels of non-complexity.  When you have those kinds of "dig hole" tier jobs that need filling, your suitable applicant pool gets bigger.
[jfusjhb] (score 121, diepte 1) Oh, is being an infantryman not a viable MOS any longer?
[jfvc4by] (score 121, diepte 5) MEDIC!!!
[jfuw670] (score 101, diepte 3) It was a joke.  I was Air Force, so you all are dipshits to me.  JK… kinda.
[jfvcgj7] (score 84, diepte 0) WW1 and WW2 drafts were amazing snapshots of overall public health. By 1917 the drafted male was roughly the same height and weight of a Union soldier in the 1860s. By WW2 coming out of the Depression, the average US service member was 1/8 inch taller and ten pounds heavier.
[jfup8tp] (score 63, diepte 0) What was going on with people's feet back then? How high were them standards?
[jfv83a7] (score 62, diepte 5) HA!! fuckin GAT EEEEEMM
[jfutxx9] (score 48, diepte 1 OP) Standard were rather high for the time- and problems like flat feet affect 10% of people to this day- but the likelihood of a serious broken bone or joint injury was greater when most people were doing manual labor at the farm or factory and like TB and VD, the risk of not recovering fully from an injury or illness and following you the rest of your life was considerable.
[jfwh9ed] (score 46, diepte 6) I did eight years active duty, two deployments (Baghdad both times), two years stationed OCONUS (you guys drew some kind of hazard/shitty housing pay for visiting where I lived).  Got out, did the Guard thing, fought a fire, deployed to Syria and then did an additional boring ME rotation for a yearish (still got rocketed but it was a one-off)

I think I've earned the right to gently mock the USAF from time to time.
[jfvhsk8] (score 39, diepte 5) Fucking rah man 😂
[jfw4qj7] (score 38, diepte 5) Clear the net for the 9 line
[jfuyocv] (score 36, diepte 2) Yeah, but back then "only slightly inbred" and "suitable to shovel shit" were average qualified applicants.  When you automate the fuck out of ships, no longer need ditch diggers as a dedicated MOS, etc you run out of the low performance holes to stuff the dumb people.
[jfuvjhg] (score 27, diepte 0) What’s that statistic on the rich and powerful and their debilitating bone spurs?
[jfv36jj] (score 23, diepte 0) Let's remember the standards then we're 20/20 uncorrected vision. If you take that into account the numbers between then and now would be about the same.
[jfuwgn8] (score 21, diepte 1) A lot of them were subject to “down home” healthcare for most or all of their lives. That included a lot of “deal with it” for chronic problems that were painful but not life threatening.
[jfuvfzk] (score 21, diepte 2) A lot of infantry options do surprisingly well on aptitude tests despite the popular perception of being knuckle draggers. 

When I took the ASVAB my recruiter asked me what I wanted to do and when I said infantry he was like “Okay, but for real you can actually choose any MOS field. What do you want?”

I think I upset him.

Edit: It’s also sort of necessary with the amount of reports and technical tasks we’re expected to know and master. To include shit that technically falls under multiple other MOS’s that we have to figure out on our own when away from the flagpole.
[jfwaaf0] (score 18, diepte 5) Oh man that’s messed up ;-;
[jfw663u] (score 18, diepte 3) The infantry, at least in the Marine Corps, has a ton of dudes that are 80+ on the ASVAB. When I was a recruiter I would say the majority of the high scoring kids that I put in wanted infantry. My best guess as to the reason for this is that the smart kids aren’t joining the Marines because they don’t have other options, they’re joining because they want to be Marines and being an 03 is the most Marine thing you can do. The dudes with the 40s, 50s, and 60s on the asvab all seemed to want the technical jobs.
[jfwkfpt] (score 15, diepte 0) There's a reason that school nutrition was a thing in the 40s, 50s, and 60s.
[jfx78l2] (score 12, diepte 5) Got. Damn. You killed him 😂
[jfx81f1] (score 12, diepte 2) It was definitely a thing. Ever heard the song "Fortunate Son"?
[jfusdf0] (score 11, diepte 1) Did you see the shoes they had back then?  Not a ton of arch support with LOTS of walking.
[jfuwrcw] (score 11, diepte 2) Sounds to me like they'd be a right fit for service.
[jfx755n] (score 11, diepte 7) That was a solid burn. I clutched my wings in pain lol when I read that. I’m pretty sure Gen. LeMay felt that one 😂
[jfux1sp] (score 11, diepte 1) **44%** fit for service is a damn sight better than **23%** fit for service.
[jfv6vuo] (score 11, diepte 3) Yes but also people aren't disqualified for VD and Tuberculosis anymore, and after WWII the US revamped its entire social safety net for children specifically to increase qualified draftees. It's the actual reason we have a free lunch program. 

For modern qualification standards, it depends on if whatever clickbait article is talking about "based on current recruiting standards where tattoos are disqualifying" or "if there was a draft". Because if it's the latter, slightly inbred is still acceptable.
[jfvlb0n] (score 9, diepte 3) True.  But in 1917 people still envisioned entire Army Corps moving overland on the march for days on end.  Everyone was seen as needing to be able to not just walk but force march on a consistent basis.

The opening moves of WWI, before the trench warfare started showed the limitations of trying to essentially replicate Napoleon, only even faster.  The Battle of Tannenberg on the eastern front for example saw entire armies more or less fall apart from exhaustion and disorganization before they even made contact with the enemy, so hard were the generals driving the infantry to cover distances on foot that were just flat out unreasonable.  It stands to reason they were even more aggressive back then on rejecting people with potential issues with their feet.
[jfwq6d1] (score 9, diepte 0) What's the deal with flat feet and military service?
[jfvgobv] (score 8, diepte 2) Population was ~100 million, we're over 3x now so we can still field a big army. And for a war standards will be dropped. Doesn't matter if you're overweight if you'll be staying in the US flying drones.
[jfvdlnb] (score 8, diepte 1) The shock from those recruitment numbers were the impetus for a variety of public health measures at the time, from vaccinations to trying to curb youth malnutrition and alcohol consumption.
[jfve0pz] (score 7, diepte 1) Remember, this is before motorization.  If you werent cavalry or riding a train, your ass was walking into battle.
[jfwkmv4] (score 7, diepte 7) Got ‘em
[jfvxw3k] (score 7, diepte 3) They can also put people through a "fat camp" before going to basic. If the army needs people, they can get you fit pretty quickly.... the Army just doesn't need to right now.
[jfwht5w] (score 7, diepte 0) In 1917, my grandpa was rejected too. His trigger finger was missing. (No, he didn’t misplace it. Got cut off in an industrial accident.)
[jfw26hh] (score 6, diepte 2) Oh yea the Air Force hadn’t been formed yet.
[jfwlhq0] (score 6, diepte 5) In other words, that joke was above your asvab score lol
[jfv3sov] (score 6, diepte 3) Same. I had a 118 GT and went tanks. Guy at MEPs was doing everything he could to try to get me to change. Guess they were short in another field that month.
[jfvy77a] (score 6, diepte 4) Spades can be a complex game.
[jfxe1ts] (score 6, diepte 1) It makes you likelier to suffer injuries such as shin splints and knee/back damage. 

They just wanted to avoid that if possible. 

Even to this day, if you have bad enough flat feet, you may need a waiver.
[jfw9gk5] (score 5, diepte 4) Were you one of the dudes who hands out towels at the gym or one of the people who picks up the dfac trays after other people are done eating?
[jfvdnwh] (score 5, diepte 5) So that's why they got rid of the USMC tanks?  Y'all were too happy and it showed.
[jfwpcsg] (score 5, diepte 4) Idk all the MOS’s in the Marines, but as an Air Force CBRN guy, we do quite a bit of joint training with Army and Marines. In almost every course I’ve gone through, the Marines were some of the smartest CBRN dudes in the room when it came to field level tactics. 

They’re also usually the most fun to hang out with, which is worth its weight in gold when you’re all TDY to the middle of nowhere for two weeks.
[jfupdj8] (score 4, diepte 1) Same problem as now flat feet
[jfvhmb1] (score 4, diepte 2) To be fair in many modern war plan scenarios where you are cut off from logistics, spares, prep time, or bad weather, your ass is still walking into and out of the battle.
[jfvjqjc] (score 4, diepte 4) In a Navy recruiting station when they get a kid that could qualify for nuke training but has no interest in it.  Massive hard sell.
[jfw6n3m] (score 4, diepte 4) I got out before I got pinched for an SDA, but all my friends who ended up recruiting have said the same thing.

And it’s true for me too. I didn’t necessarily have a fallback plan in line already, but I wasn’t hurting for options either.
[jfw7lnj] (score 3, diepte 5) Smart move. Recruiting kills your soul.
[jfvm8c4] (score 3, diepte 3) ![gif](giphy|L3ut1TkDIqduYKM21D)
[jfweamk] (score 3, diepte 3) Also worth bringing up I'm assuming the 44% number is only Men.... with Women being allowed to join it does greatly increase recruitment pools. Even if Women don't join at the same rate as Men
[jfv93x7] (score 3, diepte 0) Things never change
[jfuwpn5] (score 2, diepte 1) My guess would be most people were working on their feet all day and not in office chairs.
[jfvmnfc] (score 2, diepte 3) I did the same. Then I just finished recruiting. The guys stuck on infantry are irritating because that's one of the first jobs to run out.
[jfvsifu] (score 2, diepte 3) I remember someone joking that mortars and artillery need the highest of the army.

It’s so they can count all the numbers while they’re playing cards, waiting for a call.
[jfxjj9m] (score 2, diepte 3) Infantry are either some of the smartest people I've met, or I'm literally not sure how they don't drown in the shower.
[jfvjks9] (score 2, diepte 2) ![gif](giphy|jDEonNWKorO1i)
[jfyiuzp] (score 2, diepte 3) I thought the DoD contracted out the mess hall duties to civilians.
[jfzilmb] (score 2, diepte 6) You know how text is, hard to judge tone etc...
[jfz1k86] (score 2, diepte 1) Spot on.  

I pulled out the physical exam/medical screen for draftees during the war.  If we had today's diagnostic equipment (as opposed to a flashlight, stethoscope, and BP gauge) the unqualified for medical would be higher than today.
[jfumww3] (score 1, diepte 0) Hi! This is our community moderation bot.

---

If this post fits the purpose of /r/Military, **UPVOTE** this comment!!

If this post does not fit the subreddit, **DOWNVOTE** This comment!

If this post breaks the rules, **DOWNVOTE** this comment and **REPORT** the post!
[jfv9ng0] (score 1, diepte 4) Tanks is a good job
[jfvdqfz] (score 1, diepte 6) Your not wrong 😂😂😂
[jfxzm83] (score 1, diepte 2) I think he's referring to troops assigned the care and feeding of livestock...
[jfyl80h] (score 1, diepte 4) We were discussing WW1/2
[jfym8a6] (score 1, diepte 5) Again, a joke.  Referring to the troops as livestock.  Man!  You guys really get target fixation when on a topic huh?
[jfxzghk] (score 1, diepte 4) Although many women did join as auxiliaries. They just wouldn’t be included in those statistics.
[jfykzgy] (score 1, diepte 1) Now it’s just mostly that we are fat, and fatness can be burned
[jfxxriw] (score 1, diepte 3) Didn’t that song come out 50 years ago?
[jfwhhr4] (score 0, diepte 7) As I was lol
[jfxum4a] (score 0, diepte 4) In the navy the same guy removes panels, works on hydraulics, changes tires, and puts panels back on. How many does it take in the airforce?
[jfyildw] (score 0, diepte 5) Wow, that must really suck when he has to do his week at the ship's glory hole too.  Just because one person HAS to do a lot of jobs does not mean that is good or best.  I'd rather have an expert do each task, thanks.
[jfyz4xs] (score 0, diepte 6) Lol, what a clown. How many people does it take to swab the spit out of your throat so you don't drown in your sleep?

Hope you never fly anywhere but the airforce because you are going to shit yourself when you learn how many things a civilian A&P does.
[jfzit37] (score 0, diepte 7) You must be a TON of fun at parties.  BTW, Air Force is two words.
[jfzom2p] (score 0, diepte 8) Says the dude correcting grammar that thinks knowing how to do two different tasks on an aircraft is too many and calling anyone not in the airforce a dipshit...

What a clown.
[jfwbg4k] (score -5, diepte 5) ![gif](giphy|FcuiZUneg1YRAu1lH2|downsized)
[jfwdla9] (score -11, diepte 1) Give it a rest man
[jfwdu53] (score -14, diepte 5) Coming from a weekend warrior?

