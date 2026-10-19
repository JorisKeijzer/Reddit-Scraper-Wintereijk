# Label-batch batch_0001

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
Schrijf het resultaat naar `batch_0001.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 1n60nrj, 1n7cssb, 1n6vkpe, 1n5sldu, 1n61wlw).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1n60nrj ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-01  SCORE: 67  REACTIES: 85
TITEL: WEAR THE BOOT
POST (source_id=post):
I just wanted everyone to know that the doctors will trick you. I finally got my doctor to admit that the best thing is to wear the boot. I had debilitating pain but after 2 weeks of consecutively wearing the boot my pain has gone down significantly. WEAR THE BOOT

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbwrqc3] (score 40, diepte 0) What boot are you referring to?
[nbwnuaa] (score 22, diepte 0) Wearing a good night splint really helps too, I still wear mine to relieve morning pain

https://preview.redd.it/e4194cswdmmf1.jpeg?width=960&format=pjpg&auto=webp&s=1db9ff4f9f1ed9056c4f67a066a5b1a014278191
[nbwvh4i] (score 18, diepte 1) I second this question.
[nbwn2ys] (score 16, diepte 0) I agree but I couldn’t tolerate a boot so my doctor put me in a cast for 3 weeks and it did the trick, no more pain
[nbwmlq5] (score 15, diepte 1 OP) As much as possible
[nbwqeyt] (score 15, diepte 0) I know the boot gets a bad rap in this sub but it’s the one true difference maker for me. Day one it brought pain from 8 to 3. From there I had to continue with strength exercises and stretches but without the boot I wasn’t getting anywhere. I’m actually back to running again because of the boot.
[nbwn6k2] (score 14, diepte 1) I only ever wore mine in the evenings, maybe a few hours. Watching TV, in bed, whatever just to get the time in. Eventually I could tolerate it long enough to try and sleep with it. But, it absolutely helped things for me. I’m not back to running, and you definitely have to rehab. But, it stopped the pain and got me to a point where there aren’t any flare ups while I am working back up to running.
[nbwlpr6] (score 12, diepte 0) Do you wear it 24/7?
[nbwoo52] (score 10, diepte 0) I wondered about that. I was going to buy one on Amazon and wear it because my podiatrist is for shit. Ortho will do Tenex and PRP when and if I need it. Physical therapy made it worse (scraping and needling). Massage helped the rest of my body, exercises are good but not making a difference. Acupuncture was no help unfortunately. Boot here I come.
[nbyd7qe] (score 9, diepte 1) It’s insane that nobody has answered this.
[nbx92uv] (score 8, diepte 0) What boot?
[nbxbarh] (score 8, diepte 0) Can you please add a photo of the boot?  I was only given a night splint
[nbwnybc] (score 7, diepte 0) https://preview.redd.it/scy09as0emmf1.jpeg?width=960&format=pjpg&auto=webp&s=1c536d8197a6af938b15f08fb6896aa66546fe80
[nbzotqu] (score 7, diepte 1) Seriously, which boot are you talking about?
[nbxbal2] (score 6, diepte 0) Are you referring to the night splint or a boot you wear all day? 

Tip for the night splint.  My toes were also getting numb.  My PT told me to criss-cross the 2 straps over the toes rather than buckling them across.  Worked like a charm.
[nbz1lm6] (score 5, diepte 1) And where to get boot?
[nbx5vjx] (score 5, diepte 0) Night boot for the win!!   Not the most comfortable for sleeping and I needed to work up to a full 8hrs but a few months in the boot finally provided relief after 18months of pain.   

It’s clunky and uncomfortable and sometimes my foot would go numb BUT it works!!!
[nbyfmkk] (score 5, diepte 1) It’s a hard walking boot that keeps your ankle at 90 degrees.
[nbwtcyn] (score 4, diepte 0) Boot definitely helps. 1+ year sufferer and helped me finally get over it although suggest wearing an offset lift on the other foot/shoe to avoid sciatica, hip, back problems.
[nbxxvmb] (score 4, diepte 0) What boot?
[nbz1us5] (score 4, diepte 0) What boot?! Link!
[nbzg8bs] (score 4, diepte 1) It comes from the podiatrist office

https://preview.redd.it/xx36pp7cypmf1.jpeg?width=3024&format=pjpg&auto=webp&s=2a6777d022ae88ac5e0c998d87b8e2f756eeb162
[nbyalmg] (score 3, diepte 2) I had a bad case and took 4 weeks off. The boot, icing, stretching and strength training daily were all key to getting right. I did all this before without the boot and I didn’t get anywhere. Had to scale my running volume back at first but made it back to 25-30 mpw.
[nbwqfo6] (score 3, diepte 0) hard agree.
[nbzbtfa] (score 3, diepte 2) Following
[nbwvuds] (score 3, diepte 0) Yes, but it’s a risk reward decision. There is a point at which the pain is so much that your recovery will be very long and painful without it. However with it will come significant muscle atrophy in a short space of time plus it may trigger tendonitis due to reduced foot use, both considerations to weigh against the pain and mobility impacts.

These are the reasons I opted for crutches rather than a boot. Wondering now whether I might have healed better and faster had I gone into a boot straightaway.

Sliding doors!
[nbwxzth] (score 3, diepte 0) For those who sleep on their belly try hanging your foot off the bed when you sleep. It helped keep my foot in a better position than having it on the bed which would keep it in that pointed position. 

Had similar results doing this as wearing a boot. I try to get a lot of steps in and haven’t really had flare ups since I started doing this. Before doing this if I didn’t wear the splint/boot my foot would not be in a great spot in the morning.
[nbxrdn5] (score 3, diepte 1) Years ago I saw a mattress that had a deep crevasse near the end of the bed to stick you feet in when you slept on your stomach.
[nbxmte5] (score 3, diepte 1) It doesnt have to be very tight. It just needs to keep your foot more flat
[nbxihc1] (score 3, diepte 0) What is the exact boot?
[nbxm906] (score 3, diepte 0) THIS IS WHAT I SAY ON EVERY POST!! The only thing that has worked for me. I still wear it even when pain is gone.
[nbztu6z] (score 3, diepte 0) I wore my boot for two weeks, even though my doc said it was overkill and unnecessary.

It was the ONLY thing that helped me start to get better. A year later, and I'm still doing well. WHY DO DOCTORS DO THIS????
[ncwxk6d] (score 2, diepte 1) Hello, 
I don’t  wear the boot at night. I just pull them off in the middle of the night. I did try scraping and I got no relief from doing that. I figured out the PRP is the only relief that I get. I get PRP every 6 months. I go in for the procedure, then reschedule for my next injection once I’m done. So far I have done four PRPs. I feel like it has worked well for me. I just got my 4th injection on friday.
[nbxct5y] (score 2, diepte 1) How long did it take to get back to running ??
[nc21xnk] (score 2, diepte 3) following
[onhrtpg] (score 2, diepte 3) Thanks so much! Really appreciate it
[nbwtf54] (score 2, diepte 0) I was pain free from PF and sprained my ankle which required a boot (air cast) for 3 weeks.  It brought back my PF in full force.  Months of PT got it back under control but I believe the boot cause the flare up.
[nbycsks] (score 2, diepte 2) I WANT THIS
[nbxmpzl] (score 2, diepte 1) Been in mine for 10 months and I sleep better with it on then when I dont have it on now
[nbxln70] (score 2, diepte 0) I’m guessing it’s the boot you get from a podiatrist.
[nbxm42k] (score 2, diepte 0) I found the hard side boot worked way better than the soft. I wore it to bed every night for at least a month or two. This along with stretching and wearing shoes all the time helped heal mine quick.
[nc11g9z] (score 2, diepte 1) Are you referring to a walking boot, or a night brace?
[nbxwdki] (score 2, diepte 0) I hated the ski boot. But it did do the job. Over the years I've had stints of having to wear it. Finally I'm pain free. Wear the ugly ski boot to bed. Do iiiit.
[nbzxwze] (score 2, diepte 3) You can use a brace for that.  You don't have to sleep in that big, heavy boot.  The point of the boot is to keep pressure off your pf so it can heal.  There is no pressure when you are sleeping,  but I can understand wearing a brace to hold the foot and ankle at 90 degrees.


Just curious.   Did you wear a shoe inside the boot?
[nc0tsns] (score 2, diepte 5) Where did u get it?
[nbyevet] (score 2, diepte 0) Night splints for the win!
[nbzswlv] (score 2, diepte 0) Did you wear your shoe inside the boot?
[ne0hgp9] (score 2, diepte 2) Sure! I got it on Amazon and it’s called a Plantar Fasciitis Night Splint Sock. I think several companies distribute them but the one that I got it from is called Cezuvr-–US
[oi0g8o3] (score 1, diepte 2) Hi this is an old post but if you have time to answer, how long did you wear the boot for and did you have ongoing positive results?
[oi0js2j] (score 1, diepte 3) I wore mine initially maybe 30-45 minutes at a time or until it just became uncomfortable. Eventually I got to where I could sleep most of the night with it on. Overall, it was maybe 1.5 months (6 weeks’ish) of trying to consistently be using it. The recovery is a process. I had to take the time to let things not just start to feel better but really recover without re-injuring by getting too anxious. My mistake had been to get ahead of myself relative to where the injury really was in the recovery process. It has to heal sufficiently before putting any real strain on it again with exercise or rehab.
[nc1jxo3] (score 1, diepte 1) I have a lot of questions about scraping and massage because how is it really doing much good to massage the fat pad of your foot? I am dubious any massage is getting through it to the tendon.
[nc3auvk] (score 1, diepte 2) My structural body works just asked chat gtp and it was contraindicated. Actually taping is helping me a good bit so not sure I need the boot
[nc7i4os] (score 1, diepte 2) I have found that on my bad days, when I can’t even stand up, a massage helps my feet relax enough so I can walk. 

Pressing with my finger knuckles (and some lotion) I work up and down my entire foot in the direction of the tendons. I try to hit up the sides of my foot and the calves as well. This all helps with immediate relief. 

However, as nice as massaging is, stretching has been the most helpful thing for me to keep PF from coming back. I also keep a racketball under my desk to roll around on when I’m on my computer.
[nbygjwo] (score 1, diepte 3) Thank you for that …. I’ll keep that in mind.
🙏🙏
[oa98hky] (score 1, diepte 3) Did you do stretching and strength training while wearing the boot or once you were done with the boot. My doctor is saying only 2 weeks, but is that enough time?
[nglk27n] (score 1, diepte 1) Hi! Would you mind sharing which boot you've been wearing? I'm having trouble sifting through all the options on Amazon. Thanks so much!
[nc29j4x] (score 1, diepte 1) Not OP but I asked my podiatrist today and he said it’s a cam boot
[nfuucza] (score 1, diepte 1) Amazon - 
United Ortho Plantar Fasciitis Adjustable Leg Support
[onej7tr] (score 1, diepte 1) Hi sorry this is an old comment but if you see this could you post a link to the moon boot offset lift?
[ongfo1q] (score 1, diepte 2) https://preview.redd.it/r8nip3mr2x2h1.jpeg?width=1170&format=pjpg&auto=webp&s=32fca342b0f2081049f0c9f7f5b010a9091027c6

  
Of course. This is just one example.
[nbwwpmy] (score 1, diepte 1) Yes, seen this happen to others before plus picking up tendonitis as a consolation prize
[nbx87ed] (score 1, diepte 2) I’m supposed to get a boot for a randomly swollen ankle but I already have PF and tendonitis
[nbwxtzz] (score 1, diepte 0) Yep. The boot helped me so much.
[nc4iwrh] (score 1, diepte 3) Because I sleep at night
[nbxdq6x] (score 1, diepte 0) The boot sucks and can be cumbersome but it works! Between the boot and intense friction massage, I'm able to manage mine very well.
[nbzzhcy] (score 1, diepte 2) I mean, they call them night braces. You can’t really walk around in them. This is one of the top recommended treatments for plantar fasciitis, wear a night brace when you sleep.
[nc02nim] (score 1, diepte 4) Same thing 😂
[nc0dj3e] (score 1, diepte 6) Yes, hard-side night boot/brace is what I wore to bed. Compared to the soft-side night brace, I recovered from PF in 2 months opposed to 6-8 months before. I swear by it. Worked great for me.  

There's no point in arguing how people treat themselves. This issue is different for every person. Just because one thing worked for you, it may not work for others.  This isn't really a debate subreddit.  😂
[nc4iqhl] (score 1, diepte 2) The night brace
[nbxr42g] (score 1, diepte 0) Why are they tricking you?  Why did they “admit” it?
[nbxry55] (score 1, diepte 0) Boot is horrible for my foot.
[nbzuaol] (score 1, diepte 1) Why wear it to bed?  The point of it is to keep pressure off the pf so it can heal.  When you are sleeping,  you are not putting pressure on it.
[nbzvnse] (score 1, diepte 2) Holding your ankle at 90 degrees keeps the tendon in a stretched position. This reduces the stress of stretching under stress when first steps are made in the morning.
[nc0c8ox] (score 1, diepte 4) https://preview.redd.it/z2hh7bxc4rmf1.jpeg?width=960&format=pjpg&auto=webp&s=d0178d64e87f578acaa995fe957f36c63fab07c1

This is what I use at night, lite weight and cool
[nc0vda3] (score 1, diepte 6) Got this one on eBay, used a hairdryer to mold it for a perfect fit, very comfortable. On road trips I usually get a flair up and I wear it inside my shoes and it really helps
[ncybtg8] (score 1, diepte 2) Thanks for responding!!
[nbyaawi] (score 1, diepte 0) Did it. Mainly just hurt other parts of my body since it messed with my walking so much. It did take away a lot of the pain in the booted foot but it came back
[nbyfh0i] (score 1, diepte 0) Boot worked for me as well….
[nbyk970] (score 1, diepte 0) I wanted one and my doctor wouldn’t give it to me, only the shot
[nbzgfnq] (score 1, diepte 1) I tried to post a picture, but it won’t allow it
(43 reacties met lagere score weggelaten)

=== THREAD 1n7cssb ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-03  SCORE: 43  REACTIES: 52
TITEL: I hate how plantar fasciitis seems to be permanent once you developed it
POST (source_id=post):
[removed]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc6ltqt] (score 17, diepte 0) >I hate how plantar fasciitis seems to be permanent once you developed it

I had it for seven years. When I finally lost weight, it completely went away.
[nc6o00v] (score 15, diepte 1 OP) I am 6’0” and 150 pounds, so I don’t exactly have any weight to lose
[nc6h2l3] (score 11, diepte 0) there is surgery.
[nc6ok6z] (score 11, diepte 2) Is you are in the untied states it’s going to cost your whole deductible for the year. 

Until you get an mri no telling what’s really going on and talking to your doctor.

In my case I got a partial facia fasciotomy.(this is main thing if just planter facilities, a bone spur removed(this caused mine to not heal that tour my facia next to it. It was huge. Also a tarsal tunnel release. I was born with flat feet making PF bad and needing the tarsal tunnel putting pressure on the nerve.

I am only 10 weeks post surgery it still hurts but in a different way, but not as bad as previously.

People talk about “waves” mine never went away for 3 years. That’s why I did surgery.

I did prp shots, all the stretches, stoped waking the dog even could not even imagine trying to run, all the straightening exercises, and even put myself in a boot for a month. None of it worked and it was constantly hurting even when not walking just miserable pain all the time. Decided could not live like that anymore and got surgery
[nc6np7c] (score 10, diepte 0) Losing weight and strengthening my calves helped a lot.
[nc749bt] (score 8, diepte 0) It goes away when you address the root cause and stop just managing symptoms. Find a PT who understands that and can take you through the process to identify the culprit.
[nc6pgpq] (score 7, diepte 2) Then I'd definitely talk to a podiatrist. While every case is different, there are a LOT of studies that show a majority of PF cases are linked to being overweight, and losing weight is what worked for myself.
[nc6nxxd] (score 6, diepte 1 OP) It’s dangerous and isn’t a guarantee of fixing it.
[nc6uwim] (score 6, diepte 2) like every single hip and knee replacement.
[nc6z6dz] (score 6, diepte 0) Mine is completely gone. You need to figure out the cause of the PF. Mine was right calves. Strengthening the posterior chain through kettlebell swings helped tremendously. I also got some zero drop shoes - Altra Lone Peak and started wearing them around town. These strengthen your feet. I now have zero pain. I walk barefoot on my hardwood floors all the time. The insoles are just a bandaid and don’t address the issue.
[nc74apl] (score 5, diepte 4) >What was your weight and what did you drop down to?

I am 6ft tall, and when my PF was at its all time worst, I was at my all time heaviest of 213 pounds. I've averaged between 180-185 pounds for the majority of my adult life, and when I dropped down to 187 pounds, my feet started to feel better.
[nc7z0pb] (score 4, diepte 2) I can't speak to the cost, since it's been years since I've had mine, but I had bilateral plantar fascia release surgery in 2021 (for one foot) and 2022 (for the other foot), and I can confirm it's what finally got rid of the PF I'd been dealing with for years. I got the surgery, then did physical therapy for a year or so after, and my feet are finally back to pretty much the same level of functionality that they were prior to developing PF, with the exception of being a little more sensitive to what shoes I'm wearing (e.g. if I wear bad shoes my feet get more sore more quickly).

Surgery wasn't an immediate fix, but after a year of recovery and physical therapy following the surgery, it did finally fix it.
[nc72oa0] (score 3, diepte 3) What was your weight and what did you drop down to? I have already lost around 10kg but I'm still carrying a bit of excess body fat so I could lean down by another 8 and be fairly shredded... As long as it cures this BS
[nc7e87x] (score 3, diepte 5) We're quite similar I dropped from 218 to 197. My target is around 182. You've given me some hope!
[nc8eoyg] (score 3, diepte 8) I've read posts where people drop 10 pounds and it significantly helps the PF. 

Ten pounds shouldn't be too difficult to drop. My fiance is 5'6" and when I gained excess weight, she did too, and she was going through menopause also. Her normal weight is 118-120, but she got up to 143 by July 2023 (my bad eating habits rubbed off on her). When I decided to clean up my diet, she did also. Now, her weight is around 118. Like myself, she did not increase or decrease her exercise whatsoever.
[nccuo68] (score 3, diepte 4) > losing weight will put a less of pressure on your PF.

One million percent accurate, plain and simple.
[nc6nsx5] (score 3, diepte 0) Sorry to hear that. Tough to manage don’t I know it. But this isn’t the typical PF experience. 

May I ask, how were you diagnosed and what PT did you follow, with whom and for how long?
[nc7ogin] (score 3, diepte 0) I had a procedure called radiofrequency coblation five weeks ago (one more week in a boot) after an MRI revealed tears in the plantar fascia and severe inflammation and scar tissue. I'm hopeful that this will do the trick. No amount of stretching, orthotics, proper shoes, or night splints were going to do it for me--it was too far gone.   This procedure scrapes the scar tissue and creates tiny puncture wounds that tell your body to get back in there and fix the problem. No Advil (ibuprofen) at all so that your body's natural process does not get disrupted. So far so good but I'm still in a boot so I can't say for sure yet. I will keep everyone updated.
[nc6j3wo] (score 2, diepte 1) How much it cost? And what it addresses? Like in detail.., If you have an idea..
[nc89qza] (score 2, diepte 3) Nailed it perfectly. I can understand what you were feeling in that transition period. I fell the same. Like it affects a lot of aspect of life. We begin to think that why us and it fuck us up. Plus I am going through a recover period in hsv too.. so it sometimes get grim.
[nc8roix] (score 2, diepte 3) Keep us informed on how you are doing please. I am same way but has not yet decided on surgery.
[nc8y8yl] (score 2, diepte 4) Happy to!

So for background, I developed PF in early 2020. Prior to surgery I had genuinely tried everything there was to try. I did PT, a bunch of different shoes and inserts, custom orthotics, night splints, stretches, icing, heat, boots, compression socks, LOTS of rest (I went from fairly active to sedentary because of PF), steroid injections, shockwave therapy, etc. None of it worked. I only ever had PF, no other issues like bone spurs or anything like that, but it was incredibly fucking stubborn.

So finally, after a few years I was given the go ahead by my podiatrist to get surgery. I got one foot done in 2021 and the other done in 2022. I believe it was an open plantar fasciotomy for both. I wore a boot to immobilize the foot afterwards, no putting weight on it for a while, then gradually transitioned to shoes. Then I started PT, which I think was crucial in conjunction with the surgery. I did PT until early 2024, then stopped.

At present, I'd say I'm back to 90% functioning. I can take walks and be fairly active without having to worry about whether my feet can handle it. This is in contrast to when my PF was at its worst, when I couldn't even stand without pain - I couldn't even do basic chores like grocery shopping either, it was really bad. I'm honestly grateful every day that I  can be active again.

In terms of maintaining functionality, I'm way more cautious of not overdoing it with my feet. If they're sore after a long day of walking, I don't push it. I also avoid going barefoot whenever possible. Oofos are my go-to for wearing around the house. I always wear supportive shoes - no more hiking for hours in $2 flip flops with no arch support, which is what caused the whole mess in the first place lol.

To completely level with you, surgery is probably going to be expensive if you're in the United States, but I can't remember what the exact cost was since it was a while ago. But if you can do it, and if nothing else you've tried has worked, I personally think it's worth it. It's just important to keep in mind that you aren't going to see improvement right away. It took a couple years after my surgery before I saw marked improvement, so just hang in there. Also, ask your podiatrist about a PT regimen to aid in recovery - I really think that was crucial for me being able to get the most out of my surgery.

Also, remember that this is just my two cents - other people have had the same surgery and not all of them have gotten the same results. Everyone is different. I can only offer my recommendation based on my own experience. But my thought on it is that if you've tried everything else, and nothing has worked, surgery is worth pursuing.
[nc9c94s] (score 2, diepte 5) Thank you ! Yes exactly in same boat same years of suffering.  Except that I have very good arch !  It sucks the light out of our lives for sure.
[nc7f6m6] (score 2, diepte 6) [There](https://www.tcfootandankle.com/blog/another-reason-to-lose-some-weight-it-improves-your-plantar-fasciitis-pain) are [plenty](https://www.bmj.com/content/353/bmj.i2175/rr-0) of [studies](https://www.newtampapain.net/blog/the-link-between-your-weight-and-plantar-fasciitis) that [show](https://plantarfasciitis.co.uk/blog/obesity-is-a-well-known-risk-factor-for-plantar-fasciitis/) the relation between PF and excess weight. How tall are you? Also, great job on losing 21 pounds!
[nc6zpch] (score 2, diepte 2) Might be worth looking at that diagnosis again. Sharp stabbing pain could be other things.

How long were you doing the physio and how were the calf raises progressed in terms of load?
[nc9fofx] (score 2, diepte 1) This is your golden answer.

I didn't fix mine until I saw a second PT, there is hope OP as much as it doesn't feel like it at the moment.
[nc835mg] (score 2, diepte 0) I suffered from it for decades especially as a basketball player. What helped me recently is wearing inserts that have high arch support during games. I saw a huge improvement in my energy output due to less pain. Also, using a Theragun on the bottom of my foot before and after games has been a huge help in pain management. 

Overall, the inserts are a must.
[nc89k7z] (score 2, diepte 0) I have cut surgery and dropped weight. This has helped it. I have been pain-free for 2 months now after being in excruciating pain for 5 years.
[nc9xymd] (score 1, diepte 3) thanks for downvoting me , americanos.

love,  

 Canada
[nc7ipui] (score 1, diepte 1) Doesn’t always help. I had surgery on one foot and it still has PF after healing.
[nc8bzju] (score 1, diepte 7) Do you think 10lbs makes a difference? I’m not overweight but was heading that way .. was always 5ft 8 135-140 and then I gained 10 lbs in menopause and got pf
[nc8exra] (score 1, diepte 9) Thanks
[nc8fqm3] (score 1, diepte 10) No problem. I wish you the best.
[nc98zz1] (score 1, diepte 8) Consider how many steps you take in a day then take your weight double it and imagine that weight going through the fascia with each of those steps. 

Now reduce your body weight by 10 pounds and apply the same principle. Do you see how this might be or help given your fascia is weakened by micro tears and cannot bear as much load as when you were healthy?

The effect is from the reduced cumulative load not from the amount you’ve lost although it should be obvious that if this were to work for you, the more you lose the better.
[nc8w220] (score 1, diepte 3) Yes, losing weight makes sense.. trying for it.. 
As logic say that losing weight will put a less of pressure on your PF.
[nc9dgyx] (score 1, diepte 2) Shockwave therapy made mine go away and red light and NIR is keeping it away
[nc6o6xa] (score 1, diepte 1 OP) My podiatrist just diagnosed me when I said I had a sharp stabbing pain in my foot. My PT did hip exercises, calf stretches and raises, picking up marbles with my toes, and other typical plantar fasciitis exercises. It didn’t help at all
[nc6uzz6] (score 1, diepte 2) Get an mri and try cortisone shots.
[nc709i9] (score 1, diepte 4) Helped me for an entire decade until a bone spur got a bit bigger. Did you try it?
[nc717a8] (score 1, diepte 5 OP) I did, and the foot still hurts. It also feels much weaker, and that worries me more
[nc74n2q] (score 1, diepte 3) >Might be worth looking at that diagnosis again. Sharp stabbing pain could be other things.

Seconded.
[nc8djo3] (score 1, diepte 2) You need to figure out the cause of the plantar fasciitis. In my case, it was high arches in my feet. The physical therapist made me a set of custom orthotic insoles, which completely fixed the problem. I have been free of plantar fasciitis for three years now.
[nc74wm6] (score 1, diepte 0) same - I can get it mostly healed but then even a tiny deviation from my pt and time consuming stretches and shoes causes it to come back with a vengeance. It's just so unforgiving. I want to be done with this.
[nc777b2] (score 1, diepte 0) I had full PF release in early May and nothing has changed. Still in pain same as day one. I’m just living with it. Once you accept you’ll have this forever it’s easier to deal with.
[nc7nvuo] (score 1, diepte 0) It comes back when you stop the exercises because you have to continue doing exercises to continue having strength.
[nc7wzmm] (score 1, diepte 0) I had my pain for 2 years and it felt like this, then I got the right shoes and did the exercises and I’ve not had it come back for a year or so, maybe longer… long enough to loose track. I no longer do the exercises, but I am extraordinarily active. Alls this to say is you might not know what will lead you to relief. When I had it mine needed a proper break and wearing hookas for relief in the beginning worked for me, something seemed to heal and I was able then to do the exercises. Now the Hookas are deeply uncomfortable for me to wear. I wouldn’t get the cortisone shot or surgery if you’re an active person, my brother and my mother both got it and it came back worse, though if you’re desperate, it seems the results are varied. The exercises are probably good to do forever. And why not? They could also be fun :) ok I hated them too, but they helped and once I could feel them helping I became more encouraged. I used to do certain ones I needed to walk in the morning, but then I’d set a timer and sprinkle less serious ones throughout my day, walking, waiting in line at the grocery store, sometimes on  the dance floor.  

And I just went on a hike and I thought it was being triggered and I got scared, but somehow I literally walked right through it in a mile or so. 2 days post hike and 25 miles later we’re good! (Probably not the best idea for you rn but again, just want to encourage you, healing may look a an unexpected way) good luck!
[nc8n7ki] (score 1, diepte 0) This is not a super helpful answer, but it is possible. I had it for about a year when I was obese and then it kind of just went away on its while I was still obese. No change in weight or exercise.
[nc8sdee] (score 1, diepte 0) Has not much to do with weight in my case I am only 125 , 5.5. 6 years into this. Comes and goes every 2 years . It’s a nightmare
[nc975ba] (score 1, diepte 0) I have it for the third time, but it was 8 years between the last episode and now. I’m not sure how I got over it, but I did do calf stretches 8 years ago. This time I’m not seeing improvement with the stretches, so I’m focusing more on my feet, toe exercises, heels and toes up and down while seated, and things like that. I’m in my 70s now and intense stretching seems to make the pain worse.
[nc6zdqs] (score 0, diepte 3 OP) Cortisone shots just mask the pain
[nc6o0qv] (score -9, diepte 2) cost? are you kidding?

=== THREAD 1n6vkpe ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-02  SCORE: 27  REACTIES: 40
TITEL: Oofos Slides Caused My Mom to Break her Leg!!!
POST (source_id=post):
Has anyone else experienced this? 

My Mom got a couple of pairs of Oofos shoes on recommendation of her doctor. The tennis shoes and work shoes were fine, but she got a pair of slides as well.

She found them extremely slippery when wet, not on the ground, but her foot on the inside of the shoe. We were at the pool a lot this summer and she uses her hose in her yard for landscaping and whenever she got them wet she noticed they were very slippery, and she almost fell a couple times. 

Then the other day she was walking out to her garage to close the door cause it had started raining and her foot slipped THROUGH the slide. She was falling and tried to catch herself with her other leg and her knee bent backward and she broke her bone. The slide ended up around her calf and she had to cut it off. 

My question is, has anyone had anything like this happen for these shoes. Or even a near miss? She is very upset, she works as a server so now not only is she out $50 for the shoes, she is also losing on 6 weeks of work.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc2zybg] (score 33, diepte 0) I once sweated in my slides and found them slippery so I don’t wear them when wet.
[nc301kv] (score 11, diepte 0) I’m so sorry your mom had that terrible experience. What a horrible and painful ordeal! I am astonished that I didn’t have the same exact experience because I did find Oofos to be super slippery. Combined with our heinously slick front porch tiles, they’re a recipe for disaster and I’ve hydroplaned across the porch on several occasions. I eventually stopped wearing them anywhere but indoors.
[nc30pke] (score 10, diepte 1 OP) I wish she had made that choice. I think it was one of those things where she was just gonna be quick, and figured it would be fine since the garage was only, like, 10 steps away. Thanks
[nc30ib5] (score 7, diepte 0) Yup, wore them to a hot springs once and that happened.
[nc3187j] (score 7, diepte 0) Weren’t they too big? My feet hardly fit through the slide. They are slippery at the pool though but I literally can not wear anything else or barefoot or flats. So every step is very careful. Same with Hoka slides and anything plastic. Those slip even worse, but it’s super weird the slide itself expanded like that
[nc327zg] (score 4, diepte 1 OP) Thanks for chiming in! It's scary, I feel so bad for her!
[nc32mdf] (score 4, diepte 1 OP) I don't think so, she went and had them fitted in person. But maybe? They weren't obviously big, like there wasnt a gap between the top of her foot and the strap, they just stretched and her skin squished through because of the force of the fall.
[nc31dk0] (score 4, diepte 0) No. Wear them all the time. But not in wet situations. They are slides, they are going to be slippery. Crocs are the same.
[nc31wv4] (score 3, diepte 1 OP) I think she was wearing them less, but just slipped them on for convenience for a quick trip. 😔 Hindsight is 20/20 I suppose. I suppose they could have been house shoes. My mom bought them for yard work and stuff, but she takes her shoes off at the door usually
[nc38dhr] (score 3, diepte 0) Wore them to soak my feet in a creek after a hike. Feet went right through the slides.
[nc3e6yr] (score 3, diepte 0) All the time!  They are a death trap when wet!
[nc32trv] (score 2, diepte 1 OP) She's had crocs for years with no issues. I think cause they are more enclosed. Definitely the choice she will be making in future. Thanks for your input!
[nc3pkiy] (score 2, diepte 0) Oofos are terrible for feet. I often slip on them because they are cut too sharp in the front and I always trip on them. Because the sharp bit bends under my foot
[nc3rbp6] (score 2, diepte 0) Yep... they're plastic shoes... but not water socks or something. They are slippery if they get wet inside.   
I have a pair I wear mostly around the house. I find them easy to trip on because they're so wide and huge.
[nc3xecn] (score 2, diepte 0) I can’t wear after showering, because of the material and slipperiness. Sorry to hear and hope she gets better soon.
[nc3xmq8] (score 2, diepte 0) I don't wear mine anymore because I didn't feel stable walking in them - I'm so sorry this happened to your mom
[nc486xf] (score 2, diepte 0) Yes i first noticed it when I took them to the beach! What a mistake! They were slippery as hell and my feet kept going through them.  

Sometimes ill wash the car in them and i should really stop doing that

They are amazing sandal but a death trap when wet. You could really get injured like your mother did.

Hell ive had it at times where they aren’t actually wet and they will bend my ankle
[nc4sa6k] (score 2, diepte 0) Not slippery but I’ve had a few close calls when I take a step and the slide somehow gets stuck on the floor and I almost find myself taking a major fall. Scary. Hope your Mom gets better soon.
[nc522rm] (score 2, diepte 0) I fell out of a boat and broke the part that goes thru next to the big toe. Not only painful but also expensive..
[nc9b5m1] (score 2, diepte 0) I read several reviews where people said they were slippery and they couldn’t continue wearing them. That’s horrible and I’m very sorry about your mom.
[nc9bbb1] (score 2, diepte 0) I’ll stick with my vionics flip flops.
[nc4swtz] (score 1, diepte 2) So weird. If that’s a thing, then they’re quite unsafe and should use stronger material! Or post a warning about water. Very concerning
[nc52gvj] (score 1, diepte 1) That happened to me. I bought slides too big and got my feet wet and almost killed myself. I instead bought Hoka flip-flops and I feel much safer. But dry feet feel more snug in slides.
[nc36szh] (score 1, diepte 2) Yes, maybe because of the strap. I definitely see the issue. I’m sorry that happened. It sounds painful.
[nc35n7d] (score 1, diepte 0) Oh wow, that's awful! But yes, they are VERY slippery when wet. When I hose my feet off after coming in from the beach, I have to walk very gingerly into the garage. I do love how they make my feet feel, but yes, keeping your feet dry in them is definitely safer.
[nc3b22c] (score 1, diepte 0) I have the flip flops and WATCH OUT if your feet get wet.
I'm a large man so I've definitely had some close calls with exactly what happened to your mom!
[nc3hsqy] (score 1, diepte 0) Very slippery and I was worried I had a stress fracture on the top of my foot from the slip ons being so tight. Never again
[nc3ky5e] (score 1, diepte 0) So sorry this happened… I just wore the their slides, they actually fixed my heels but then gave me knee issues lol so…
[nc3m9xj] (score 1, diepte 0) Holy crap ! I hope she heals quickly. I noticed my slides get slippery when wet too. Also, I wear Oofos loafers at work and the sole has minimal traction and wear down to a smooth surface after a few months. If I walk on wet pavement I have to be cautious because I feel my feet slipping. I’ve always loved Oofos for the comfort but now I’m considering ditching them.
[ncaizfg] (score 1, diepte 1) The same thing has happened to me over and over again, especially within the last couple years. I’ve worn Oofos for several years, the quality just keeps declining. I have several pr of slides and they are very slippery. Yes, the front is cut so they often bend underneath the shoe causing a tripping hazard. Recently ordered the sport mule in a final sale (previously had 2 pr of the same mule) and they arrived defective. The right heel back was shorter than the left and wouldn’t stay up like the left heel. Contacted them immediately. I should know if they’re defective since I’ve already owned 2 pr of the same shoe. They refused to allow an exchange or refund since they were final sale. It’s my third pr, I should know a defect in the shoe! Zero customer service! And try to leave a negative review on their website, they make leaving a review very difficult. I’m never ordering their shoes again. Frankly, I’ve had much better results with Hoka and Brooks and they’re safer, too! Bye bye Oofos.
[nc3uuoh] (score 1, diepte 0) I’m so sorry! To be fair, my non-oofos slides (adidas) are super slippery when wet, so I’m not sure if it’s necessarily a oofos thing.
[nc3vwe2] (score 1, diepte 0) Yes, you absolutely cannot wear them wet.there should be a warning on them. I wore them on damp grass and about lost it.
[nc41nul] (score 1, diepte 0) Honestly, I can see this happening. I have had times where I’ve been walking in them and felt one or the other slip ever so slightly. So sorry this happened to her!!
[nc42vhu] (score 1, diepte 0) Yeah I got out of the shower and didn’t dry my feet well enough and they slipped on to the sides and I almost fell over. Please have her be careful or opt for different slippers.
[ncaj8zc] (score 1, diepte 1) Yes, you are right!
[nc4hhbu] (score 1, diepte 0) They aren’t safe when wet
[nc4nvms] (score 1, diepte 0) yea they are SO slick.  That is a pretty major downside, I am going to start saying that since I recommend them a lot.
[nc4o67b] (score 1, diepte 0) Babygirl Lisaaaaa
[nc4pkoq] (score 1, diepte 0) I wear them when I’m camping so I can easily slip them on/off if I need to step out of the camper for a minute.  I also wear them at the beach.  I love them.
[nc52g9w] (score 1, diepte 0) Damn. Nearly the same thing (short of the break) happened to me when I got my Amazon cloud slides wet and tried to walk up a hill. It’s just the material when wet.
[ncdwrhs] (score 1, diepte 0) Yeah, they are definitely super slippery when wet. I have nearly sprained an ankle a few times using them as shower shoes. I’m so sorry that happened to her. 😞
[ncdzhnp] (score 1, diepte 1) Also, I have recently switched to Ininji socks that have the individual toes (there are other brands as well), and that is helping my bunion immensely and furthering my journey to help my feet be more healthy.
[ncgmqtw] (score 1, diepte 0) Oh yeah definitely avoid water, their oofoam is water resistant which makes water glide off the surface. I rarely wear them to pools if it’s very wet there
[ncmiuyt] (score 1, diepte 0) I don't like these shoes. They feel very unnatural on the feet. And apparently also terrible for traction. Sorry for your mom's broken leg.
And she might also be out for more than six weeks because first the bone has to heal, and then she has to rehabilitate muscles and everything
[ncnpnd3] (score 1, diepte 0) Oh definitely... I had to have my small toe amputated last October and I've had a lot of foot issues from being in the boot so long. One of them being some issues around my achilles.

 The pt recommended oofos slides while I'm at home to take the pressure off of that area... Since my one foot is short a small toe, it's not as wide and moves around a bit...

 Fast forward to taking the pups out on a rainy night and that slide had completely turned 90 degrees on that foot... They are slick. Thank goodness I didn't fall. Sorry to hear about your mom.
[nd4a3a0] (score 1, diepte 0) My feet are super narrow, so slides never fit me.
[nenbigh] (score 1, diepte 0) Same thing happened to me maybe 20 years ago with a pair of Crocs flip flops. Walking really fast out my front door onto the porch, stepped in a wet spot from having watered flower pots minutes prior, I fell forward while my foot got flipped under when the flip flop got stuck between wood slats. Ended up with foot surgery to reattach the tendons I tore. I don’t wear slides ever, but do wear Oofos thongs, carefully. Hope Mom’s OK.
[nqtwb0h] (score 1, diepte 0) I find them to be slippery on the inside, so I just wear socks with them
[oexp0lr] (score 1, diepte 0) I wear mine only bc they were expensive. I’ve tripped several times when the toe folds under. Stupid piece of molded rubber for big money. Never again.

=== THREAD 1n5sldu ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-01  SCORE: 8  REACTIES: 36
TITEL: What shoes are we wearing
POST (source_id=post):
Whats everyone wearing? I have some powerstep sandles, vionic sneakers. Looking for other suggestions.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbuvtjv] (score 4, diepte 0) Birkenstocks soft soles, and Altras. Birkenstock half-foot inserts for the work boots.
[nbvnxw2] (score 3, diepte 2) Too soft is a real thing. I needed a firmer supportive sole
[nbvvtjh] (score 3, diepte 3) I hear you on that.  I tried the Oofos slides and they feel good for a moment, then not so good.  Birkenstock insoles in Topo runners has been the best for me.  The Topo Phantom 3 have the right balance of support and cush.    I am not a runner, but the reviews from runners is what made me want to give them a try.  I have tried Hokas and a few different Altras.  One Altra seemed to be way too soft and made the foot pain worse. I can do the zero drop Altra trail shoe with the Birkenstock insoles.
[nbv0p3a] (score 3, diepte 0) Xeros out and about and Vibram 5 fingers at home. I start hurting even in Topo and Altra. I go back to the podiatrist in a week and am dreading it. The doctor wanted me in ultra cushy Brooks Ghost. I don't like going against doctor's orders, but my heel hates cushion for some reason.
[nbval76] (score 3, diepte 0) lately i’m doing well with nike air max + super feet inserts and oofoos slides in the house.
[nbvf24u] (score 3, diepte 0) Altra Torins.
[nbvpkai] (score 3, diepte 0) New balance anything fresh foam
[nbvq5qr] (score 3, diepte 0) Oofos slides
Brooke's Glycerin
[nbvj9jy] (score 2, diepte 1) I am on the same boat, but will add Topo Phantom 3 for walking and around town errands.  Chacos have a softer footbed sandal, and one that is too soft for me.  The mid softness give my arch the support it needs and also gives my heel some cushion.
[nc14ia0] (score 2, diepte 2) Yes! Loovveee the Topo phantom 3s 😍
[nbuzt8i] (score 2, diepte 0) Which Vionic sneakers?
[nbv7f9l] (score 2, diepte 0) Kuru Ridge Motion


https://www.kurufootwear.com/products/womens-ridge-motion-bluehaze-orangespice
[nbveh0i] (score 2, diepte 0) I’m based in Switzerland, so Kuru, Joya, Birkenstock, and Kybun. Kuru is surprisingly good, and way less expensive than Joya or Kybun. So I’ll just stick to it, the only thing though is the width of the shoe. I need a bit wider than what’s available. The slipper is excellent, I’m loving it. Kybun is super soft, and bouncy, it’s really great, but very expensive. I would love to transition into a barefoot shoe, but I keep on reinjuring myself, so I’m very careful with this.
[nbvmznt] (score 2, diepte 0) Currently: Mizuno wave rider 10. Other faves: Asics Kayano 14s (my absolute faves), Puma RS-X (also great). Timberlands during winter. Hoka recovery slides indoors always. I have custom orthopedic insoles, a dynamic type that allows me to use the muscles in my feet (as opposed to insoles where your feet are kinda just stuck like in a mould).
[nbvrqjp] (score 2, diepte 0) The thing that worked amazingly for me was using PF insoles. I was very anti using them initially and at first they felt so weird but now if I don't wear them my PF comes back and my feet feel naked 🤣 

To answer your question though, new balance 860 or 1080 casual wear, teva hurricanes (holidays), altra lone peaks (hiking), vans ultra range (hiking). I do have very wide feet so that does limit my options tbf
[nbvwibp] (score 2, diepte 0) DANSKO clogs fixed me. Then I lost weight, and that really helped.
[nc09juk] (score 2, diepte 0) Birkenstocks and Hoka Gaviota 5
[nc1l66k] (score 2, diepte 0) Brooks Ghost Max with orthotics.
[nbwee0e] (score 1, diepte 4) I’ll have to try the Topos out, I’m about to be in the market. I got a minimal padded Altra for that exact reason, kinda felt like my foot was sliding off the normal ones. But even then they were still a lil too squish. So that sounds like it might be the perfect solution
[nbwt081] (score 1, diepte 5) https://runrepeat.com/topo-athletic-phantom-3

https://believeintherun.com/shoe-reviews/topo-athletic-phantom-3-review/
[nbxr5gc] (score 1, diepte 6) One more shoe for you to consider.  The Danner trail shoe.
[nbvffws] (score 1, diepte 0) Kuru Flex
[nbvg7r4] (score 1, diepte 0) Vivobarefoot for training and walking and Topo Athletic for running.
[nbvjqrp] (score 1, diepte 0) Hoka Bondi with my custom insoles
[nbvp7sh] (score 1, diepte 0) FitFlop tennis shoes. My new obsession.
[nc778ty] (score 1, diepte 1) Do you mean the Rally model? I see no tennis shoe.
[nc82iqs] (score 1, diepte 2) Should have said sneakers. I wear the SUPER-Q Knit Slip-On Laced Sneakers.
[nc8bxvp] (score 1, diepte 3) Looks interesting but the men's options are very limited compared to the women's
[nc8qwzw] (score 1, diepte 4) Well that’s a bummer. They’ve really helped me.
[nbvqw8g] (score 1, diepte 0) Birks sandals, oofos slides and brooks shoes .. nothing can beat Birks
[nbvujf9] (score 1, diepte 0) Altra, Lems, Xero for me. Altras for walking/running athletically, Xeros for the gym and either Xeros or Lems in the office and for casual wear, depending on how I’m feeling that day.
[nbvy970] (score 1, diepte 0) Altra Paradigm  and Torin for activities 

Oofos recovery slides for home
[nbw78bh] (score 1, diepte 0) Asics
[nbw8666] (score 1, diepte 0) Custom orthotics plus brooks adrenaline
[nbwe0uv] (score 1, diepte 0) Topo Phantom 3 for walking and running, Brooks Ghost Max 2 and Hoka Clifton for work, and Hoka recovery slides to wear around the house
[nbwimge] (score 1, diepte 0) Kuru tennis shoes and archies flipflops
[nbwluhv] (score 1, diepte 0) Brookes Adrenaline GT with Vionic Athletic Inserts. Seems to help me.
[nbwr8xm] (score 1, diepte 0) Bare feet at home. This podcast where they were saying how it's important to build muscle in the feet. And if you wear shoes all the time, the muscles atrophy similar to how if your arm is in a cast the whole time. The podcast is diary of a ceo and google "foot expert" for that particular episode. I also wore a boot at night for about 3 weeks and after 6 months of pain, my PF is mostly gone.
[nbwzng5] (score 1, diepte 0) https://preview.redd.it/4x06ir8hpmmf1.jpeg?width=2268&format=pjpg&auto=webp&s=72a2d3a776a7ccf22730c6cd42aff4d8e6dea792
[nbwzztv] (score 1, diepte 0) Brooks adrenaline gts 24

Oofos slides

Blundstone work boots with insoles
[nc3pbz9] (score 1, diepte 0) Hoka  Bondi 9
[nc6nkve] (score 1, diepte 0) I wear oofos slides around the house. I’m thinking of getting a pair for out and about. They are pricey though but to good. 

I just got some hoka arahi 8 sneakers and are loving them. They’re good for flat feet
[nccgu0i] (score 1, diepte 0) Orthofeet are working for me.

=== THREAD 1n61wlw ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-01  SCORE: 21  REACTIES: 31
TITEL: Will I ever be barefoot again?
POST (source_id=post):
I miss being barefoot around the house and garden. I’m so sick on the sicky foamy sounding oofo’s. Were any of you able to return to a barefoot life?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbwxcaz] (score 9, diepte 0) Yes
[nbxyh84] (score 7, diepte 2) I’m about 12 weeks in and I go barefoot every now and then in the house which at first I never thought I would get to do again. I have switched to all hokas and brooks with insoles from lucky feet when I go out and I do daily stretches I learned from physical therapy. Ookas around the house. This has been a time consuming and expensive recovery but I have really committed because it was agony at first.
[nbxhjgw] (score 6, diepte 0) Yes, as hard as it might be to believe. I am over 2 yrs in and there was a point that I wouldn’t dare be barefoot around the house whether carpeted or not. Now I can walk barefoot without any of the strained sensations or pain that I used to have. The switch from that protective mindset I developed for so long to being carefree is amazing. It can happen, you just need to give your foot time to heal and you need to deliberately strengthen consistently.
[nbwydcz] (score 5, diepte 1 OP) Tell me howww
[nbwy99c] (score 5, diepte 0) I feel the same way, my feet have been messed up for almost two years and even when they have gotten better again, it's always gotten worse again. So I think I'm just stuck with painful feet.
[nc6awv5] (score 5, diepte 3) Same thing happened to me. I saw everyone raving about Hoka Bondi. Wore them 2 days inside and thought yea these are great. Wore them in one store and both feet hurt so bad within 20 minutes I had to leave. I have a different pair of Hokas and they're fine. I like Brooks Ghost Max right now.
[nbxp4ib] (score 3, diepte 1) I’m in a similar situation finally. It’s giving me hope even just being able to walk around barefoot for a few minutes… baby steps!
[nc2uv6e] (score 3, diepte 2) Yes, congratulations. That’s how it starts. I remember when I was forced to be on hard floors in socks whilst visiting cos no shoes were allowed in the house. That’s when I realised the flare ups were not happening as I expected. And hopefully if you continue looking after your feet progress should continue.
[nby4w9a] (score 3, diepte 0) I have had PF 10 years ago cause by running in barefoot shoes. My feet healed without any intervention except wearing over the counter insoles.  

Have been going barefoot every summer without issues, except for this year. 

I think running barefoot on Asphalt might not be a great idea.
[nc1693b] (score 2, diepte 2) Taping helps.
[nbwyetn] (score 2, diepte 1 OP) I feel the same way. Like this is forever 😭
[nbx24pf] (score 2, diepte 2) Go a get fitted insoles. I've managed to walk 10 miles in the last three days. Yes my feet are a bit sore as I've over done it, but so much easier than the last few months
[nc4lr9i] (score 2, diepte 1) It’s been two years for me too. I’m good most of the time.. as long as I’m in expensive ass sneakers
[nc66if5] (score 2, diepte 2) So, I found some hokas that felt good when I wore them indoors. I decided to keep them, wore them out and my feet hurt! I'm still trying to figure out if there is a break in period for some shoes, because they felt like clouds around the house.
[nbx081g] (score 2, diepte 1 OP) 😭😭😭
[nbx1edt] (score 2, diepte 0) My pain stemmed from my job. I was on my feet all day on concrete or driving a standing forklift, using my feet to help balance. Within a month of starting an office job my pain was gone
[nbxljbd] (score 2, diepte 0) I don’t know. My foot seems to have recovered one year later I’m pain free! But my foot is still uncomfortable barefoot or sock foot it still wants that support. Plus, I think that walking barefoot or sock foot was part of what caused it so I don’t want to get back in the habit.
[nbxv3ib] (score 2, diepte 0) Yes
[nbyek8u] (score 2, diepte 0) Don’t think I’ll ever be able to return to barefoot life 😕
[nc1sluk] (score 2, diepte 1) What kind of insoles
[nbyya00] (score 2, diepte 0) I can sometimes go barefoot in my home but I dont want to chance it right now. I have more good days than bad days right now. 

I could not deal with the Oofoos so I wear Waysoft slippers off Amazon. Padded and soft and cushiony.  I'm about 1 year from my realizing I had PF. I did PT 1x a week for 8 months this past year and I still wear orthotic insoles in my shoes everyday that im out. I wear Joomra sandals when I'm out and about if I'm not wearing shoes. I find that very padded as well, which helps.

My podiatrist gave me a list of shoes to wear that are not zero-drop so ive been wearing Altras Paradigm 7s for the past year. Its time for me to get a new set. I thought Kurus were my brand but once I put in the orthotic insoles, they didn't fit right anymore. 

At PT, they measured my feet from day 1 to the last day and it showed significant degree change showing that I had trained my feet to not hang out low as much. I dont wear a boot or a sling. I cant sleep with those things on me unfortunately. I do use a 'calf wooden stretch' which looks like a slack board?, as well as a balance board from time to time. 

Wishing you the best! PF is a broad journey known to many but an individualistic journey 😪 no one size fit all.
[nbzc7c6] (score 2, diepte 0) I am now able again to walk barefoot. Still taking it calmy in my walks. Measuring everything so that the pain doesn't return. Making my feet stronger every day, but slowly. I am still scared of overpassing my limit


I highly recommend you to make your feet stronger: toe yoga once  a day, heel raises... And start walking barefoot 1-2 mins Frist week... And increasing. 


The way for recovery is in the strength


Good luck on your way!!?
[nc0gqrp] (score 2, diepte 0) My method of healing (everyone is different) was through strengthening and complete rest rather than cushioning. Barefoot shoes have been my salvation. I found a way of springing from the ball of my foot in my most hurt foot in order to take a step rather than pushing from a heel toe order of operations, and that graduated me to where I am today (barefoot all the time). I actually find it hard to find cushioning shoes that allow me to feel the control I need to feel safe as I continue to strengthen my way back to normal. I wear correct toes and do balance training. I will never take the strength to walk for granted ever again, I walk every day except when I need a rest day.
[ncaymle] (score 2, diepte 0) I wear these!!

https://www.amazon.com/dp/B07KQN7WM4?ref_=icdp_ba_mweb_mb_pd_bap_m_grid_rp_0_1_ec_pr_ppx_yo2_mob_b_ts_rp_1_gf&clientRefMarker=pd_bap_m_grid_rp_0_1_ec_pr_ppx_yo2_mob_b_ts_rp_1_gf&heartsTeamIdentifier=buyagain&psc=1&heartDisabled=false&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D

Very close to being barefoot!
[ncv85j4] (score 1, diepte 2) Which sneakers , if you don’t mind ??
[ncyovwx] (score 1, diepte 3) Hokas
[nbx0648] (score 1, diepte 0) Yes! When you’re sleeping!🤣
[nby2s5c] (score 1, diepte 1 OP) Well I’m a stay at home mom so yes, feet all day. But not sure I want to quit 🥲
[nc0h9c4] (score 1, diepte 2) Consider a knee scooter or other mobility device so you don’t make it worse on flare up days 🤍
[nbxkrv7] (score 1, diepte 0) I can walk around for very short periods without shoes. I wear crocs inside pretty much 24/7, or tennis shoes for longer periods of activity. I’m mostly recovered, but my barefoot life is pretty much over.
[nbyw8ji] (score 1, diepte 0) After 10 miserable months I finally found what will alleviate my pain. 
Here’s what helps me - good fitting shoes with GOOD insoles ALL the time. During my recovery I didn’t walk without my good shoes and insoles for even a minute. 
-Toe strengthening. 
-Calf stretching ad museum.
-Reducing inflammatories in my diet like alcohol (boo) and sugar (also boo).
If I had a long day on my feet I would try to limit my standing etc. the next day. (Wasn’t always possible)
[nbzx4xv] (score 1, diepte 0) No, should always have a shoe on
[nc0nka5] (score 1, diepte 0) I feel your pain! I hate hate hate wearing shoes in the house and I just have no idea what to get in terms of slippers or slides or whatever. My feet just want to be free!
[nc12sxk] (score 1, diepte 0) Barefoot is the worst with PF
[nc1d25s] (score 1, diepte 0) Yes! After 1.8 years of agonising pain- I am able to walk a few steps these days barefeet!

I was taking allopathy meds but switching to ayurvedic meds worked like magic- quite literally.

Plus stretching helped.
[nc80l5t] (score 1, diepte 0) Hey, they give you meds based on your specific body condition- so if you’re having the same pain as me the meds can be quite different. 

I don’t think you should take them based on a stranger’s advice on Reddit but I take singhnaad guggulu twice a day and at night I apply maha vish garbh oil- if you use it please take proper precautions as advised by the shopkeeper/doctor as it contains traces of poison

Took me 10 days to see a difference.

Almost 2 months in, I have MAJOR improvement and I had zero faith in ayurvedic medicines before this.
[ncaamv0] (score 1, diepte 0) I switched to the barefoot lifestyle for an entire year. I ran in "barefoot" shoes or unshod, walked around in barefoot shoes (or unshod) and that was the only thing I changed in my life that led me to get PF.  The foot doctor said during the healing process, NEVER go barefoot.  

It's been a couple of years now since I last had it (ended up getting it in both feet over a 2 year span) but I've not gone back to 100% barefoot. I will walk around barefoot sometimes, but I mainly try to wear shoes. I wear birkenstocks or other shoes.  Shoes that don't have a ton of support, I'll notice that familar pain in my heal creep in when I'm in them too long or on my feet too long.  

Since barefoot is what got the PF started for me, I'm very hesitant to go back to it.  It was fun, especially running barefoot, but I never want to experience PF again if I can prevent it!

