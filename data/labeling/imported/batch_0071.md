# Label-batch batch_0071

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
Schrijf het resultaat naar `batch_0071.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1bdde64, 1k3vcrl, 1la455z).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1bdde64 ===
SUBREDDIT: r/Teachers
DATUM: 2024-03-13  SCORE: 3417  REACTIES: 452
TITEL: Can we PLEASE collectively agree that babying them isn’t helping and we need to hold their feet to the fire to address whatever is going on?
POST (source_id=post):
Sooo many teachers saying “I even make it SO easy for them, and they still fail”. At least at my school, that’s due in big part to the fact that no one ever makes them do anything. The problem is 30% them being slower with less foundational knowledge than we’re used to, and 70% that they have no reason to give a fuck (again, this is MY school, I know not everyone will relate but I also know my situation is common). They need to feel some pressure again. 

Like, late assignments should be zeroes and stay zeroes unless they have a family emergency. Tests should only sometimes have study guides and shouldn’t be open note every time. Assignments that don’t show competence do not earn passing grades (I know a lot of people have their hands tied with this one but those of us who can fail nonparticipants should). Students should have work to take home sometimes because all the in-class work time is spent doing fuck-all so we might as well teach more skills and do more activities with the 5 out of every 30 who do give a shit. The work should be appropriately challenging and designed with the students who DO try in mind, not the ones who don’t. Focus on the ones who care, because this focus on the ones who don’t is giving them control, and hurting the education of the ones who try. If they’re going to make up the 15% of competent adults in society, shouldn’t they at least be well-educated? Kids have always just stooped below whatever bar is set. Why are we setting the bar an inch off the floor? 

PLEASE can we stop fighting this situation by making everything easy. It’s hurting them more. And us.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kulufxi] (score 987, diepte 0) Teachers do agree.


Preaching to the Choir here.


Admin controls the non-renewals. They set the priorities.
[kulvhlt] (score 391, diepte 0) Completely agree with you. But society doesn’t want that. Parents will just bulldoze right over you. Can’t make our precious babies earn anything.

Side note: I just got blamed for a kids poor mental health because I gave him a 50% on each of his late assignments. He feels bad about himself because I gave him a bad grade, not because he does little to nothing in class.
[kuly2vf] (score 310, diepte 0) We are not allowed to give a zero at all in our district. 50% is the lowest grade we can give, even if they turn in nothing we cannot give less than 50%.
I have taught from adults to now pk-3rd so I have a wide range of experience. 
My adult students were reading at a 9th grade level.
My high school students were an average of 6th grade reading level.
Now we are trying everything to get our littles reading on level. I’m so tired of the “Pandemic learning loss” excuse. Most of my students now were not even school age. That excuse is worn the fuck out. 
Parents don’t give a shit as long as they don’t have to deal with them for a few hours (I’ve been told they are my problem at school and not to call back before the parent hung up on me.)
Middle school was the worst, but that was during the pandemic. Our state opened schools way too early so they lost one semester. One semester and Louisiana is using the pandemic excuse for a system that has been riddled with good old boys that have no business in management of any kind, much less the important jobs that decide what teachers can do.
[kum1s97] (score 251, diepte 1) >We are not allowed to give a zero at all in our district. 50% is the lowest grade we can give, even if they turn in nothing we cannot give less than 50%.

As a university faculty member, this is utter insanity to me. Like batshit, off-the-walls, call-a-padded-wagon-and-get-thee-to-Arkum-Asylum criminality-level insane. But hearing from those in primary and secondary ed about these kinds of district-level policies starts to explain more of the kind of behavior we're seeing in tertiary ed. 

My institution - and increasingly many others - has a grade of L that we can give; it is a failing grade that denotes the failure is because the student did not complete at least 50% of the work. It affects GPA like an F, but lets us create a permanent record that the student effectively just did nothing.
[kum54kl] (score 208, diepte 0) When you wait for the slowest runner to catch up, everyone else figures out pretty quickly that they don't have to run, either.
[kum45ab] (score 203, diepte 1) admin, the bloodsucking parasites on the educations system
[kumoqpa] (score 180, diepte 3) Teacher of 17 years here. Last year, went into admin (still kept a couple of classes)... Was fired within a year for being too harsh (made accurate predictions of grades, demanded kids work etc).

Just accepted a new position as principal. Have insisted that I have at least one class and have made clear that placating parents will not be the aim, reaching kids will.

...taking bets now how long I last.
[kulyh4y] (score 160, diepte 1) I was blamed by a dad for sending a student to therapy during online Covid school. She never went to a Zoom meeting, didn't respond to my supportive "Don't forget to turn in X" emails or had any kind of contact with me. What put her in therapy? Me putting in 0's for her not turning in work.
[kulvm6s] (score 133, diepte 0) My admin will tank your evals if you have more than 15% fail rate. They say that you can't be teaching well if so many kids are failing. So the standard is lower. And then the kids fail to meet it. So it's lowered. And so on and so on. 

There's no actual failing at my school, so my students often don't even know what's considered an F. I had a kid on the last report card ask "Is a 48 bad?" because they'd had a 40 something in math last year and still moved up. They just didn't know that their math teacher was on her way out and refused to budge. 

We just got a new ELA teacher who is...gasp...taking off points for things like egregious spelling errors and refusal to put quotations in quotation marks. They all hate her for it because we aren't really allowed to, so none of the other teachers do.
[kumd9dd] (score 126, diepte 2) The state, not the site admin or even the district admin create these policies. Someone at the state level says it would be more equitable if students get suspended less or don’t get F’s, then shit rolls down hill and consequences go away because schools are graded by their suspensions, and the bar hits the floor because everyone must succeed and it’s the schools fault in all cases, not the community or the family.
[kume1r9] (score 124, diepte 1) The problem is that the slowest runner isn’t even trying to run. They didn’t even show up to the race and we all still need to wait for them.
[kuly4h2] (score 115, diepte 0) TBF (and I hate defending admin) to do this, current admins and super's heads would be on the chopping block. 

  
"Class of 2027 has 54% pass rate, down from 96%" headlines will ruin all their careers.
[kum5cpb] (score 108, diepte 1) If my kids aren’t doing the work and aren’t participating, fail them. Please, fail them. Passing them does me and them zero favors. I’m seeing I’m in the minority of parents, but earned always feels better than given. I also need to know what they aren’t understanding. I tell my kids if you really tried, did the work, and still failed then we have a comprehension issue and I can’t be mad about that. If you messed around, didn’t do your work, and failed, we have a “you” issue and we’re about to have a “come to Jesus” chat. If the whole class tries and failed, we have a teaching/test/understanding issue. Kids need to fail. It’s a part of learning. We are doing them a great disservice by not letting them learn to fail.
[kum738n] (score 104, diepte 2) "L" for laziness. On record. Beautiful.
[kum006b] (score 84, diepte 0) Yeah, no can do. If they fail my class, they just go into credit recovery where they learn nothing, cheat, and go into the world unprepared and uneducated. 

I have been more proactive about immediate social consequences (checking work and grading it in front of them as they complete it), giving zeroes for copy/paste and for missing work, but some supports have to be put in place because I'd much rather have a kid pass my class and learn some life skills and science than fuck around in "online school" or credit recovery and learn nothing.
[kum3kkq] (score 79, diepte 0) Lol, I just joined a new school a couple weeks ago, and the students are getting on each other for this. 

A kid today was grumbling about his grade and another one went "Bro! She's right there! Talk to her if you think there's a problem."

Then another one told me that I didn't grade her notebook correctly (I had a ta do it) and I told her to send me an email with proof for a grade change. She said she wasn't going to do that, so a different kid said, "Then that's the grade you GET."

I love my intervention classes. The students are very real.
[kum299u] (score 70, diepte 1) Doesn't sound like much of a bad thing, honestly. Their jobs aren't to appease parents, their jobs are to educate children and/or facilitate a learning environment for them. They're not doing their jobs now, so let's get some folks that'll tell parents to shut up and raise their goddamn kids in their places.
[kumubki] (score 66, diepte 4) I hope you make it far. This shit is out of control.
[kumfg0j] (score 65, diepte 2) Highly recommend checking out the recent controversial and quiet shuttering of Columbia University's reading and writing program, along with other top university ed schools/teacher prep programs. You will find the source of these Arkum Asylum education policies that sound utopian on paper, but inflict disproportionate harm upon low/working class schools and communities.
[kum103q] (score 65, diepte 0) Man I’d love to. 

My principal has explicitly told us we’re fired if more than 10% fail. Take a high school class of 30 (small end). 3 idiots fuck off and do nothing and get zeros, there’s my 10% right there. I’m out of a job and my mortgage doesn’t get paid and my daughter doesn’t get fed if I don’t just put 70s in for the half that know this system and play the fuck out of it
[kulwzfg] (score 64, diepte 2) I personally would prefer my admin to not hate me.


I make it easy to pass, but I expect work. I still end up failing 40% of my kids because they do nothing. 


Expectations from the district need to raise if you want teachers to raise theirs. Right now my district only cares about test scores and absolutely nothing else.
[kumrdbh] (score 61, diepte 2) Fun fact: I actually coach track and we have a kid like this on our team. I'm not actually sure why he's still on the team, but he walks during training, cuts corners, and once even had his parents pick him up in the middle of a road run without telling anyone.

He's been a bad influence on a few of the new kids, but most quickly figured it out and just ignore him. We all always wait for the slowest runner, but not for him. Even today, some kids pushed for our slowest runner to be on the relay team over this kid. 

In the classroom, I've actually found this is true, too. Most of my on-level kids are really dismissive towards peers who do no work and put their heads down. I just wish more of them had that attitude.

&#x200B;

I
[kumcbx9] (score 56, diepte 1) Why are parents given priority? Sorry, public school was not designed for parents but society. Everyone in a town pays property taxes to fund schools whether they currently have a student or not.
[kumptyr] (score 52, diepte 3) The states set the pace that the parents demand.

And frankly, school systems have too many protective policies in place that the reality of what actually goes on in schools is a complete mystery to the majority of people who could vote for change.

The only time bad stuff gets leaked is when it's convenient for some politician to push for charter schools because "hurrdurr, public schools are broken!" 

Right now, voters are in the grip of a ridiculous "Gentle Parenting++" movement that folds together letting kids do whatever the fuck they want, anti-vax rhetoric, and happy fairytales about how you can save them all by just "giving them more attention." I'm honestly shocked people haven't been demanding that schools just do away with strict grade levels and just fully commit to unschooling all together.

And they get that way because all they ever hear about are the "studies" proving how these things are SO successful.  They didn't see the real results.
[kumcmfq] (score 50, diepte 1) I teach at a community college. My students want to transfer to a 4-year. I have standards and I maintain them, in part because I need 4-
Years to continue to accept students from my school. 

I do not and will not lower my standards to accommodate students' poor k-12 education and/or their lack of effort. There are many reasons, but the primary one is doing so would not be fair to my students.
[kum1oh6] (score 44, diepte 1) At my school this is a district level thing - any teacher with more than 10% of students earning D's and F's is supposed to self reflect and figure out what they can do to help students achieve the standards. We also have a board approved 50% min. for middle/high school.  I have 8th graders who cannot and do not care to spell correctly.  I've been teaching 25+ years and will probably retire earlier than I expected due to the student apathy and the system that lets them do nothing and still pass.
[kum9ha3] (score 44, diepte 2) There jobs are to serve the board.  The board works for the voters.  The voters are.... the parents.
[kumzhqt] (score 43, diepte 4) Can we clone you?
[kum2dry] (score 43, diepte 0) I mean, yes, we can agree on that all day long. Their parents won’t though. I can’t get their parents to pull all the way through the car line. They all want to stop right in front of the door, so that their precious baby angel doesn’t have to walk an extra 150 feet. You think they are going to let me hold those kids feet to the fire? Gtfooh.
[kum6s8k] (score 40, diepte 2) I do. I have zero issues putting in a zero if the assignment isn’t turned in.
[kun5a5p] (score 37, diepte 2) >What put her in therapy? Me putting in 0's for her not turning in work.

You monster. 

/s
[kumnia8] (score 36, diepte 1) I say get rid of admins and run schools as teacher co-ops.
[kum0j7s] (score 36, diepte 0) I give optional extra credit homework every week. The kids that don’t need it are the ones who do it, and of course those who need it don’t take the opportunity. I’ve definitely told my class as a group to not let the other students hold them back and that those doing the extra work will be the ones in charge when they’re adults. It lifts them up. It’s slow, but I’m seeing sparks ignite in many students who didn’t care for the first half of the year. But it’s almost time for them to move on and I hope it stays with them. Because lord knows ain’t nobody bein held back. 

Ultimately, with proper guidance, they’ll be okay. Not babying them is a huge part of this. If not at first, eventually they appreciate not being babied. It has to be explicitly explained that that’s what we’re doing, though. This way they understand what’s expected and why. I do worry about follow through with teachers they’ll have the next year and the next.
[kum0nfq] (score 35, diepte 0) As someone who allows students to turn in late work - even at the last day of the trimester without penalty - I have to disagree that late work should get a zero.

Before I get crucified, my logic is that I don't know what goes on outside of school. I don't know a kid's situation, I don't know what they go home to every night. Kids are busy; they're juggling friends, family, sports, clubs, activities, hobbies, 5 other classes at my school, and jobs. 

To me, it's more important that they do the work and show me they can do something than forcing them to turn it in by a due date that is largely arbitrary. Just because you didn't learn something by January 5th doesn't mean you'll never be able to learn it. If you can do it, you should get credit for it. If it takes you longer, then so be it. *But at least you can do it.* And I think that is what school is supposed to be: proving what you can and can't do, and earning a grade that corresponds.
[kum3mrx] (score 35, diepte 0) Every time I try to enforce my expectations I get accused of yelling at them. My admin told me to just be monotone and let things go. I am absolutely done.
[kumwct0] (score 34, diepte 1) that 10% thing is wild, that's a total exit from reality.   


about 25% will fail no matter what, at the HS level. That's the entire point, actually.   


Just pointing out the failure rate for the school's sophomores on the ASVAB (if the school is taking it) should give the admin a reality check on what the ACTUAL failure rate should be. If they fail to score a 31 or lower on that (which, 25% of people do), they are below a 6th grade reading and writing level, and it's tied to their IQ--not anyone's teaching ability. THAT is the acceptable failure rate. That's reality.    


Dang it's wild how out of touch admins have got.   


They exist now as an economic class, and *nothing else*. A burden to budgets and progress, that protects an economic classes income with 'easy' jobs.
[kum98ic] (score 33, diepte 3) Yuuuppp. Or more pjeoratively, "Loser". 🤣
[kunvaxf] (score 33, diepte 2) This is another reason why degree creep happens. When employers can no longer trust that the person with a high school diploma actually has the skills and knowledge that you need to earn the diploma, high school graduate jobs become community college graduate jobs. And then those former jobs become university degree jobs, and so forth.

It isn't just that there are more high school gradautes now than before - it's that the pieces of paper can't be trusted.
[kum94p0] (score 33, diepte 1) >*50% is the lowest grade we can give, even if they turn in nothing we cannot give less than 50%.*

Such. Bullshit.
[kuly5i2] (score 33, diepte 0) Consequences get results.
[kum016v] (score 33, diepte 0) We only have control over our respective classrooms. We have NO CONTROL over parents and whether or not we receive appropriate levels of support from our building administration. 

I personally think that our schools were sadly diminished through the adoption of state standardized testing because teaching to the test is oriented towards minimum levels of performance.

School administrators also need to uphold district policy and/or state school law pertaining to chronic truancy. Students SHOULD NOT be socially promoted if they lack the academic prerequisites to succeed at a higher grade level.

In an ideal world, we would have intervention teachers who could pull students to address academic deficiencies before small problems become larger ones. Since so much of what we teach builds upon prior learning, it's critical that students stay current with what's being learned. For example, we cannot teach compound multiplication to students who don't know their multiplication facts.
[kum069r] (score 31, diepte 0) I'm not allowed to fail a kid because of absences....a student can go to Mexico on vacation for a month, do 2 assignments before he goes, and still get a B.....I'm only allowed to grade a student for work he does when he's here....they literally do not have to make up missed work if they are out. It's madness.
[kulx87g] (score 30, diepte 0) No wonder everyone on this sub is miserable and hates their job.
(430 reacties met lagere score weggelaten)

=== THREAD 1k3vcrl ===
SUBREDDIT: r/Teachers
DATUM: 2025-04-20  SCORE: 164  REACTIES: 372
TITEL: Teachers with flat feet or weak ankles, what shoes are we wearing?
POST (source_id=post):
Just like the title says…I’m a young female in my full time student teaching internship. I haven’t even officially STARTED my career and my ankles are absolutely killing me with standing on my feet most of the day every day. I’m very used to standing but my shoes just aren’t cutting it anymore. I’m extremely flat footed and I knew it would cause trouble in my ankles eventually but I didn’t realize it would kickstart now.

What shoes are we wearing!? I would LOVE some suggestions. Both casual and professional or at least semi-professional. Ankle support sneakers are great but they don’t look cute with my teacher outfits and they aren’t very nice looking either. I also don’t want to dress like an old lady…I’m in my early 20s and would like to savor dressing like my age while I can LOL. 

I’ve been seeing Mary Jane sneakers by a brand called Asyllum floating around and I don’t know how they’d fair but they look nice enough to dress down or up— not sure about what they would do to my ankles though.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mo59du8] (score 248, diepte 0) You're not going to like my answer because it's not "cute" nor does it fit what is likely your idea of cute teacher outfits. 

Hokas. 

I say this as someone who went through almost tqo years of not being able to walk in the morning because the tendons in my ankles were seized up so badly. I'd have to spend a minimum of a half hour stretching before I could walk. 

So if you're flat footed or have weak ankles, stick to the sneakers that offer good support.
[mo5bzcu] (score 56, diepte 0) I was diagnosed with “moderate to severe” plantar fasciitis this year in my seventh year. Problems really started two years ago. Birkenstocks and then Birkenstock sneakers in the winter were the only thing that gave relief while wearing. Pain came back as soon as the shoes were off, so that’s where the podiatrist came in, but it’s now been three months essentially pain free.
[mo5fqxh] (score 48, diepte 1) *This is the answer.*

If you’re set on shoes, OP, I reco Clarks, Taos, Söfft, Aerosoles, Vionic. You’ll probably have to look hard to find an orthopedic shoe that’s fashionable enough unless you’re old like me (60).
[mo5a3gb] (score 45, diepte 1) And they need T least two pair to rotate each day.
[mo58rkq] (score 32, diepte 0) Hokas 😝
[mo5bm3o] (score 28, diepte 0) Do you wear custom orthotics (from a podiatrist, not a running store)?  If not, you need to start there.  You can wear them in almost any closed-toe shoe.  That being said, I also have completely flat feet with ankles that roll in on each other and I only wear ASICS running shoes to teach.  No, they're not cute, but they're professional enough to get the job done and I can work multiple days in a row without too much pain in my legs.  I can guarantee you that nobody else is paying attention to what shoes you wear in the classroom.  You can put on the cute shoes after work or on the weekend when you don't have to be on your feet all day.
[mo5f4eh] (score 25, diepte 1) Birkenstocks are the only shoes I’ve worn my teaching career (10 years?) if it’s cold I’ll wear other shoes in the building and change. The treads also help me because our classroom laminate floors are just so slick!
[mo5o2tq] (score 24, diepte 2) Three would be ideal.   Two pairs is def worth the price and will last longer.
[mo5dyp7] (score 21, diepte 1) I hate the way they look but I had no choice and they made a Huge difference.
[mo59z9d] (score 19, diepte 0) Orthotics and Compression stockings.  Not pretty but your heart will thank you later.  With the orthotics, you’ll probably need new shoes to accommodate them.
[mo5gqp0] (score 18, diepte 1) Hokas are the best I have ever had. Now they make all black ones too. At least for Men. Not sure about womens shoes.
[mo58z5h] (score 17, diepte 0) I don’t have flat feet but I have had two severe ankle injuries on the same foot, so I have to be picky about what I wear. I usually wear Clarks or Danskos.
[mo5a10a] (score 16, diepte 0) New balance 501
[mo5mzln] (score 15, diepte 2) Same. Although I've just tried Brooks glycerin GTS, and they're kind of awesome. I did live in Hokas for quite some time (plantar fasciitis) and was disappointed with how they hold up. The Brooks have some lovely cushion to them and are also supportive.
[mo5e5js] (score 15, diepte 1) I looked them up and they’re just a cute sneaker? ton of colors. Why do we think theyre ugly?
[mo5e6ww] (score 15, diepte 0) Not flat-footed but I have issues with my sesamoid joints, lower back, AND knees. Echoing what others here are saying with the idea of forgetting “cute” and worrying about staying pain-free instead.

I’ve had luck with some Skechers slip-ons, personally, and also server/work shoes have been great for the back pain. For sneakers that look like sneakers, you will have to pry my Brooks Ghost sneakers from my cold dead hands. They have been a game changer.

I’d advise getting a pair of “cute” shoes for interviews and when you know you won’t be standing all day. Prioritize function for work.
[mo5loxh] (score 14, diepte 2) Some Clarks are good, others are meh, I would not recommend for someone who knows they have foot issues unless they are careful which ones they recommend. Aerosoles are even worse -- ok for an office worker who is only occasionally on their feet every hour but not ok for all day teacher wearing, who is on their feet most of 7 hours a day. 


OP, I also recommend looking at European brands, because they seem to often make shoes that are better suited to being on your feet -- likely because Europeans walk so much more than the average American. I like Rieker although I would still steer away from their heels for all day teaching, their walking shoes and sandals are good.
[mo5autm] (score 14, diepte 0) I have the opposite problem - extremely high arches, like in the top 95th percentile. I was having extreme pain in my hips and bottom of my feet. 

Hokas changed my life. 

Worth every penny.
[mo5996p] (score 13, diepte 0) I wear skecher bobs, hey dudes sneakers, and general running shoes (asaics, nike) mixed in with sandals.

First, you're going to need to just condition your feet. They have to get used to the walking, even standing that you do every school year. The first few weeks are rough for me .Because my type of physical activity changes.

I would invest in therapy foot balls. You can also use a tennis ball. Rolling your feet everyday helps a lot.
[mo5g2qj] (score 13, diepte 2) They go well with my Mrs. Frizzle style I don’t know 🤷🏻‍♀️
[mo5kfyp] (score 13, diepte 2) They’re chunky but damn are they comfortable. It’s Hokas in the cold and Birkenstocks when it’s warmer.
[mo5dyrt] (score 12, diepte 0) Consider using a tall stool. I've known teachers who "half-sit" while teaching. It takes a great deal of the weight and pressure off their feet. You'd probably have to provide your own. I'd get one with a back so you don't embarrass yourself by falling off! 

Lace-up shoes are much more supportive than any slip-on shoes. You probably know that. I find New Balance very supportive but I don't have foot problems, so what do I know. Now about my back .  .  . .
[mo5lmiu] (score 11, diepte 1) I only wear Hokas now due to flat feet and arthritis. I also recommend getting some arch support inserts like Superfeet.
[mo5fonj] (score 11, diepte 1) I swear by my ASICS - even over my pair of Hokas. They’re my go to after a flare up of plantar fasciitis. Like I haven’t worn anything else for two years. Wish I had started wearing sneakers every day much earlier. I have me a few pairs in fun colors, black and grey to look slightly more professional.
[mo5fiiq] (score 11, diepte 1) Birkenstock boots in the fall and winter, tennis shoes in the spring and sandals in the summer. Basically all I wear now. 

I also had plantar fasciitis and while hokas helped a little bit I still had some pain. Switched to Birkenstocks and never looked back.
[mo5iccm] (score 10, diepte 1) Yes Birkenstock bend lows have been lifesavers.
[mo5fqvg] (score 10, diepte 0) Look into getting orthodic inserts—you can put them into different shoes for more support. You may have to do a bit of research to get the right kind for your feet but it’s worth it!!
[mo5goc0] (score 9, diepte 2) I actually love mine! I don't think they're ugly. I wish my white ones didn't get so grungy so fast, but I just got a cute pair of black and rose gold ones. I'll be rocking those when we go back from April vaca.
[mo5rtqa] (score 9, diepte 1) I work in a medical school: this is what doctors and nurses wear almost exclusively.
[mo59t3z] (score 9, diepte 0) I thought Vionic sneakers were great. Dansko sneakers are so much better. (Some Clarks sandals have good arch support/cushioning.)
[mo5b61h] (score 8, diepte 0) My first year of state testing I thought I'd be just fine with having to stand and pace around for almost 6 hours a day. By the end of the second day, I literally couldn't walk without limping because my ankles hurt so much! Professionalism in shoes is not high up on my list, so I wear Hokas now and I don't have pain anymore.
[mo5h4x0] (score 7, diepte 2) They do for women, too, at least in the Clifton 9 that I wear. But they're always sold out in my size when I try to get them. Or i don't have the funds.

I typically have an older pair that becomes my yard shoes and a nice pair I use for work and being out and about.
[mo64n5b] (score 7, diepte 1) I'm like so sad and I looked these up, I was imagining they were going to be like Birkenstocks, maybe. A dreary brown. (I wasn't even thinking that like nobody's going to suggest non-close-toed options cuz people in Labs need closed toe shoes.)

Imagine my total delight to see the second shoe in there has my four favorite colors all on a shoe. Thank you.
[mo68o85] (score 7, diepte 1) Hokas with plantar fasciitis insoles!
[mo5b19w] (score 7, diepte 0) I have flat feet and the best shoes for me are ones with flat soles aka converse, vans, or the nikes that are flat on the bottom. Things like danskos with a massive curve kill me.
[mo5cn12] (score 7, diepte 0) I needed steel toe boots to protect myself from the constant getting stepped on. In reality, I wore Hey Dudes, Brooks and Sketchers and the most comfortable flip flops I had (when I could without fear of kids attacking my toes). My principal tried once to make us wear professional shoes…that idea lasted about 2 days as it became clear that many would go get doctors notes to wear what we need to wear. 

I’m 50, so I honestly could care less what they think of my shoes. Find some comfy options and wear shoes that are good for you. Take care of your feet now or pay later. 

I do think crocs on the daily can be pretty tacky, unless you wear the cute sandals that you can make pretty. There was one teacher that wore dirty bright yellow crocs daily and that was just gross. 🤮
[mo5fnv8] (score 7, diepte 0) I wear black Doc Martin boots, they have great arch support.
[mo5i5iq] (score 7, diepte 0) Birkenstock makes some nice leather sneakers which have fantastic arch support
[mo5u500] (score 7, diepte 0) Dansko. They make super comfortable sneakers too if you are not into the clog thing.
[mo5bnj4] (score 6, diepte 0) If you have benefits/can afford to, get orthotics made! I’ve always been flat footed, and every day my feet, ankles and legs would be killing me, and I’m petite, so it wasn’t as though I was putting a ton of weight on my legs/feet. I got orthotics made last year and put them into whichever shoes I’m wearing and they work like magic. Obviously they won’t fit into flats or sandals, but for sandals when it’s really hot I wear Birkenstocks.
[mo5frcc] (score 6, diepte 0) [Brooks saved my back. I have extremely flat feet and found these help the most.](https://www.top5-usa.com/brooks-shoe-for-flat-feet?targetid=dsa-39337268680&matchtype=&device=t&campaignid=19691655358&creative=648221012362&adgroupid=145513486265&feeditemid=&loc_physical_ms=9033614&loc_interest_ms=&network=g&devicemodel=&placement=&keyword=$&target=&aceid=&adposition=&trackid=us_all_top5_1_1&mId=895-263-6903&gad_source=1&gbraid=0AAAAAoKwm5RxUQG5PDdw13PQEdFamviF5&gclid=Cj0KCQjwtpLABhC7ARIsALBOCVpDjwgFQw0QdREXbfaFgy1QI1xPZfbLJ4t5gQJD48w-nlVLbn3MKy0aAjlDEALw_wcB)
[mo5hary] (score 6, diepte 0) I have flat, wide feet like a platypus. Arch support, cushioning, orthotics - none of it works for me. I wear “barefoot” type shoes with flexible soles and a wide toe box. They help my skeletal alignment too. It does take some training to get used to this kind of shoe but once you do - your feet are basically indestructible. There’s a blog called Anya’s Reviews if you want more info. 

Also - lift weights.
[mo6j9l6] (score 5, diepte 3) Don't mind the look of Clark's but the top of many of their shoes rubs the arch of my foot in an annoying way- over several styles. Loathe Hokas bc stupid expensive and not comfortable, also ugly.

I live in Keens and quite strongly dislike when I have to wear closed shoes. Stupid winter.
[mo5zoa2] (score 5, diepte 1) I wrecked my ankle two years ago on a field trip and the first thing my physiotherapist recommended was a good pair of actual running shoes. Definitely seconding this rec.

And if you have flat feet, consider PT to see if it can improve! A bonus side effect of all my post-injury and post-surgery PT has been significant improvements to my arches.
[mo5ke74] (score 5, diepte 2) 860
[mo5cwkg] (score 5, diepte 0) New balance sneakers. Including on music concert nights (they make black ones without a giant letter N).
[mo5h95t] (score 5, diepte 1) If you have flat feet, fallen arches >r weak ankles, you need supplemental support.  Custom orthotics are great but pricy.  Dr Scholl's you get at the kiosks cost about 50 bucks and are good, as well.
[mo7s4js] (score 4, diepte 3) Literally came here to post this exactly. $450. You can claim 2/3 of this as a teaching expense on your taxes next year.
[mo71wte] (score 4, diepte 4) I also like Keens, though they run narrow for me. Saving up for some Birks for my wide hobbit feet.
[mo5yzzm] (score 4, diepte 1) 100% changed my feet
[mo6q3ii] (score 4, diepte 1) Agree.  I had a walking cast for 5-6 months from plantar fascitis. Got Hokas and orthotics. Soooooo much better that I walked all over Italy and Greece 5 months later.
[mo5dpql] (score 4, diepte 0) I had plantar fasciitis surgery in March of 2024 and because of that, I can only wear shoes with a good arch support.   I wear Hokas, On Clouds, Sketchers (especially their arch support line), and Clarks.  I’ve been teaching for 33 years and it’s ruined the bottom of my spine on down, so good for you thinking about taking care of yourself early on!
[mo5lfj8] (score 4, diepte 1) I have two different solid black Sketcher slip ons— both have memory foam in them. My mother-in-law got me some really cute Vans that I wear pretty much every day.  I also have a pair of black Keds but I only wear those when I am going to be doing a lot of sitting as they give zero support. 

If youre *that* worried about being cute, the teacher across the hall from me wears those Teaks brand flats every day and she loves them. They give great support. 

I dunno man. I stopped caring about looking cute at work years ago— my aesthetic is Mrs. Frizzle as an English teacher/ eccentric librarian.
[mo5fpom] (score 4, diepte 0) Running shoes that a store specializing in marathon runners suggest.  Seriously.  You're on your feet all day: get what the people who also run all day wearl.

For wearing with pants, seriously, I've never found anything to compare with Blundstone Women's Classic Chelsea boots.  Chelsea's are in right now, look great with any length of pants, and because are actually made (well at least the ones without the cute woven elastic panels) to be work boots, they are waterproof, breathable, have slip-proof soles, and great arch support.

Keen women's sneakers are good, but not great for this.

Semi-professional?  The best ballet flats you can afford.  Your feet will be happier flat than in heels, and you can move easier in flats than heels.
[mo5rqfc] (score 3, diepte 3) I live in my Bondi 8s (I'll need a pair of 9s soon). They come in all black for women, and I adore them - although I do have custom insoles in them as well (Plantar Faucitis plus overpronation plus a lovely metatarsal/intermediate cuneiform joint that likes to dislocate the metatarsal on the regular ... my insoles are worth EVERY penny.
[mo63hiy] (score 3, diepte 1) I broke my foot a couple of years ago and the orthopedic doctor recommended these, because he knew I was on my feet all day long (we worked on that accommodation) and knew my foot would need a cushion. I love them so much. I have the Clifton's and I love how pretty colors they come in. I want a second pair because it's probably time, and also new colors!
[mo5b83s] (score 3, diepte 0) I’ll hop in and say I wear my Nike Dunk lows! I teach elementary and most teachers dress pretty casual at my school
[mo5l4y9] (score 3, diepte 2) I’ve tried a few different asics- they were all awful for my feet that are, to quote the orthopedist, “flat as hell” 😩
I wanted them to help!!
[mo5sauc] (score 3, diepte 2) Which asics ?
[mo62igb] (score 3, diepte 3) I’m partial to the Gel Kayano sneakers. Started with the 29 because it wasn’t as expensive but have moved on to the 30 or 31 now. I went with those because they have the APMA seal. Now they’re just comfy for me. More expensive than I like but I’ve realized that good shoes are worth it.
[mo6mytq] (score 3, diepte 3) My podiatrist recommended any Asics gel sneakers.  They saved me while waiting for my orthotics to be made.  He also said New Balance 860s wod be good choices
[mo5zqvb] (score 3, diepte 1) I had plantaris fasciitis and used a frozen water bottle to break up the scar tissue, it hurt like hell, but I haven't had issues since.
[mo5cwps] (score 3, diepte 0) Clarks or Skechers, but I’m 53 🤷🏼‍♀️
[mo5eatc] (score 3, diepte 1) My sister, also in her early 50s and also a teacher, swears by Clark's.
[mo5dkr9] (score 3, diepte 0) I tried a few things, Sauconys and Brooks work best for me.
[mo5efz5] (score 3, diepte 0) Nikes. My body is much happier.
[mo5ekd9] (score 3, diepte 0) I remember the footwear several of my teachers wore were flats or very low heel. Blisters would be occupational hazard if it were high heels.
[mo5eryg] (score 3, diepte 0) I have foot problems, really flat feet and some other stuff. I got custom orthotics made at a podiatrist. They are expensive but it is the best money I've ever spent. Made a HUGE difference for me
[mo5ew0e] (score 3, diepte 0) I live in Canada and for the colder months I really love my blundstones!! I have really weak ankle joints and often roll my ankles because of how hard walking can be but booties really help with ankle stability and pain I find :)
[mo5fb1v] (score 3, diepte 0) I have tried them all. Vionics, Bjorn, Abeo, orthotics from Dr. Scholl's, the Good Feet Store, my podiatrist. I have flat feet, weak ankles, plantar fasciitis, and arthritis in my feet. I believe it's called spondyloarthritis. I can never wear heels again. I even have a disabled placard for my car because I'm not able to walk or stand for any length of time. (I also had heart bypass surgery)

I have found that compression socks and Skechers Slip Ins are the most comfortable for my feet when teaching. They come in sneakers, sandals, flats, and boaters, which are what I wear to school. Skechers are comfortable and easy to get on or off, but it's the socks that make a world of difference. Spend the money and get some good ones and get them in pretty colors. (I personally dislike the white and cream colored ones because they just scream ill health)
(303 reacties met lagere score weggelaten)

=== THREAD 1la455z ===
SUBREDDIT: r/Teachers
DATUM: 2025-06-13  SCORE: 92  REACTIES: 347
TITEL: What shoes do you recommend for standing all day teaching for someone who has started getting sore feet?
POST (source_id=post):
What shoes have been the most comfortable for you? Mainly looking for suggestions for someone who started getting sore feet standing all day. Thanks!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mxi904m] (score 218, diepte 0) Do not use just one pair of shoes. You want to rotate through at least two.
[mxhvf2q] (score 76, diepte 0) Brooks running shoes
[mxjtxry] (score 71, diepte 1) Your feet deserve a wardrobe too, don’t make them suffer in a monogamous shoe relationship
[mxhzd0a] (score 59, diepte 0) Brooks

Hoka

New Balance
[mxjj9zl] (score 41, diepte 3) I am not a doctor but I was always told that you need to alternate for shoes to air out completely between wearings.  Shoes harbor moisture and bacteria. Also if they don't dry out completely the support cushioning inside gets compressed faster.
[mxib3v6] (score 34, diepte 0) Birkenstocks!!! (You do need to break them in but once they’re formed to your foot they’re GOLD!) they make sneakers and boots now too if you don’t want a sandal or have admin that insist on “professional” footwear. Same footbed as the standard Birkenstocks. Only thing that helped my plantar fasciitis
[mxhpx09] (score 29, diepte 0) Skechers or Clarks.
[mxidzpl] (score 27, diepte 0) I work in a factory setting.  Asics help a lot in reducing recovery times.
[mxjgru5] (score 24, diepte 1) Yes!  this is something that people don't do enough of (probably due to cost)
[mxkrx4p] (score 22, diepte 1) I teach PE. Even with sneakers I need to rotate my shoes. Feet ache if I wear the same shoes two days in a row. I also wear Birkenstocks and crocs outside of work.
[mxjpbku] (score 21, diepte 1) Beware of Skechers, they made my plantar fasciitis worse. Podiatrist recommended Brooks with a stiff sole.
[mxjjuld] (score 19, diepte 1) Yup, I was starting to have foot issues from lots of standing and walking at my job.  A physio friend recommended the most expensive pair of ASIC RUNNING running shoes that I could afford.  He said the amt of cushion in each step is huge because they are meant for runners who are pounding their feet repeatedly.


I swallowed my budget mindedness and bought an insanely expensive pair and my foot pain magically went away.  


Also, their website often has great sales.
[mxivbvx] (score 18, diepte 1) Clarks offers discounts for teachers, too.
[mxhpw8e] (score 15, diepte 0) Running shoes or walking shoes or whatever is your style....buy some extra insoles.
[mxiqqap] (score 15, diepte 0) Dansko, vionic, brooks, kuru
[mxk0jfw] (score 14, diepte 1) Currently a Brooks adoptee. Mad at myself for wearing cheap ass wal mart shoes for almost all of last school year.
[mxk8o6m] (score 12, diepte 1) I have worn all of these and also run in all. I've loved them all while I was wearing that brand!

In a former life, I was a high end shoe fitter. I highly recommend getting fit for the right shoe for your foot OP. Everyone is so different! So while everyone in this thread is singing high praises to their preferred brands, it's because their foot is perfect for that brand.

As we age, our feet change as well. If you're female, it is also possible pregnancy will change your feet too.

Good luck out there and I hope you find your dream shoe!
[mxhrljs] (score 11, diepte 0) I got those New Balance Fresh Foam X 860v14. Bit expensive but that + inserts and my feet have been in heaven ever since. Best decision I ever made.
[mxi896g] (score 11, diepte 0) Tennis shoes, I like sketchers. Sandals and boots, I like Dansko. Dansko made my plantar fasciitis go away.
[mxjtf70] (score 11, diepte 1) Interesting. It’s the Mister Rogers approach lol.
[mxjs60o] (score 10, diepte 1) As a sped teacher who occasionally chases children and spends most of their day standing… Hokas are my favorite! Also like Clarks and Birks.
[mxisq9r] (score 10, diepte 1) I second Vionic.
[mxjpr7t] (score 9, diepte 1) I’m 9 months pregnant and love my Hokas. Half of my department wears them too
[mxjsxa9] (score 9, diepte 1) Ding ding ding….OP this is the correct answer. I tried all the fancy casual shoes that were supposedly made to help with support and foot health…Brooks, Clark’s, Birkenstocks….and they all sucked. Finally went all on top tier running shoes….and went with ASICS. they are elite. Pissed I wasted all this money on the other stuff.
[mxhp41r] (score 8, diepte 0) I wear Ariat cowboy boots everyday since 2006. They are very comfortable. You don’t need the most expensive but don’t go cheap either.
[mxjio3d] (score 8, diepte 2) Wait is this an actual thing for preserving foot health?
[mxj7ncl] (score 8, diepte 0) Compression socks
[mxjv20n] (score 7, diepte 1) I've got 4E feet, so I was a New Balance dad forever (since 7th grade).  I had heard a lot about Hokas, and was shocked they had extra wide for one of their shoes.  As cliche as it is, it was like stepping on a cloud.
[mxjmnna] (score 7, diepte 0) I ended up hacking my feet again. Went barefoot on minimal shoes and regained the strength and purpose of my feet. This was ten years ago. But take care of your feet they’re the essential part of your job. 

Look up minimal shoes and also start slow by just being barefoot at home for a couple of hours. 

About shoes, just don’t get the ultra soft and comfy ones they’re not bad but get your feet accustomed to softness that your arc loses strength.
[mxi00qw] (score 6, diepte 1) I also wear brooks! Love them and wear them daily.
[mxi4mp7] (score 6, diepte 1) Also a Brooks bro. Very comfy.
[mxl16y5] (score 6, diepte 1) I'm a Brooks Ghost Max disciple. Wore some Glycerins for a month and change that felt great at first. Went back to my old Ghost Max for the last two weeks of work cause my hips have been complaining.
[mxhwa9l] (score 6, diepte 0) Hiking boots (the kind with the shorter ankle) and the customizable Dr. Scholl’s orthopedic inserts. 

I also bought a stool-height chair that I sit at in the front when I’m lecturing or reading out loud or leading class discussion. I know walking around helps with classroom management and engagement, but be kind to yourself and let yourself sit *regularly* so your feet can rest.
[mxk5x9m] (score 6, diepte 2) Wide foot guy here, too and I love NB for this reason. Keen is my go-to for boots because they generally run wider. I'll have to give Hoka a try.
[mxiabdd] (score 6, diepte 0) After you get the good shoes, try taking a different pair to work with you and change into them about halfway through the day. The difference in fit and style the two pairs will make your feet feel a little more refreshed and less tired.
[mxig963] (score 6, diepte 0) ON CLOUDS!!
[mxiqbli] (score 6, diepte 0) I like my Sketchers
[mxkpdyy] (score 5, diepte 1) I have these and I've combined it with the poster above who says to switch up shoes. So basically, I've started wearing a rotation of different Brooks.
[mxicgft] (score 5, diepte 0) Doc Martins.
[mxkp64s] (score 5, diepte 2) Yup, I wear Asics every day with custom made orthotics in them.
[mxhy8am] (score 4, diepte 0) Columbia hiking tennis shoes. I can’t have boots for more than a couple days because of my weird feet, the tennis shoes made for hiking are perfect. 

ASICS gel running shoes are also excellent, but I can’t wear them to school because they squeak so badly on our floors. I’d wear them everyday if they were quieter.
[mxib9lw] (score 4, diepte 0) I usually had to ice my feet after every day, got On Cloud shoes and all my pain went away.  If I have to dress up, Cole Haan is great.
[mxicvem] (score 4, diepte 0) Ecco, they have dress shoes but inside are built like hiking shoes. I’ve had my last pair for 4 years
[mxihmhe] (score 4, diepte 0) Stop standing and do more pacing!

But yeah, comfy sneakers x2.
[mxjb41d] (score 4, diepte 0) Don’t think it’s the shoes. It’s your feet. You need strong feet. I have a standing desk, and put a 2 foot length of rough cut 2x4 (so it’s actually 2”) and periodically do calf raises throughout my day. I just wear Chucks.
[mxhps9w] (score 3, diepte 0) There are lots of companies that make these shoes, but the ones I got are called "Hobibear" and they helped me out SO MUCH.
[mxjsh8q] (score 3, diepte 1) Can’t stress this enough…I tried all the casual nice looking shoes made for “comfort and support” and they still sucked. Went with ASICS running shoes. Not the nicest looking shoe but I don’t care. Rather not be in pain anymore.
[mxk32oc] (score 3, diepte 2) Reeeeeeally…..????!!! I’ll have to check this out. Do you have to go to a brick and mortar store to get the discount?
[mxk4d6h] (score 3, diepte 1) I love my sketchers! I wear custom orthotics in mine though. Also my birks—podiatrist approved!
[mxik6ve] (score 3, diepte 1) Skechers were my go to when I was teaching.
[mxm7xbo] (score 3, diepte 2) Wow. I've honestly NEVER heard this before. I buy one pair of new shoes each school year and that is what I wear. I've usually done fine with that, but this year I've noticed my feet are not bouncing back at the end of the day like they used to. 

  
So, I need to get a couple of different shoes and rotate the ones I wear. Hm. Ok-that's the plan then.
[mxjs311] (score 3, diepte 1) Truth. Need to do this.
[mxia64e] (score 3, diepte 0) Get an area rug. It will make a higher difference.
[mxlf2wz] (score 3, diepte 2) I’ve got three pairs of the low sneakers—leather. I love them. I rotate them but also change out the laces for *fashion*. They hold up really well. I’ve had them for 3 years now. I’ve never had an issue with them being too loose etc—but I also try and wear barefoot shoes or as close as possible when I’m not at work. Birks have a nice wide toe box so that’s something I look for.
[mxjutxy] (score 3, diepte 1) I wear my Birkenstocks most days. Sandals or the Boston clog. Just be sure to swap them out every day so they can air out
[mxicqhy] (score 3, diepte 0) Don't stand all day.
I wear new balances. Walking shoes. Yeah they have large soles. But feet don't hurt
[mxl2r5y] (score 3, diepte 2) I have wide feet so I love Vionics! Rotate with them and Crocs
[mxjru0s] (score 3, diepte 1) I agree. I have felt much better since switching to minimalist shoes both on and off the job two years ago. I teach music, so sitting is only possible at lunch or on planning - the rest of the day I’m standing on a tile floor.
[mxjh7ji] (score 3, diepte 0) Brooks, and some good insoles. I use Powerstep.
[mxkrmsi] (score 3, diepte 1) I second this! I use Lems and a knockoff from Amazon. I like having the wide toe box to let my toes splay.
[mxldlkv] (score 3, diepte 1) I did the same! I got a cheap brand on Amazon called Whitin, and holy I can’t wear any other shoe now. I wore them every day and still do and when I put on a different shoe, I immediately feel the difference.
[mxkbjtj] (score 2, diepte 2) My feet hurt so bad after wearing allbirds one day that I refused to wear them again. Now I wear black adidas cloud foam sneakers every day.
[mxkha5y] (score 2, diepte 3) I have some Vans like that— memory foam is legit and they hold up SO well. 

I rotate between them, two pairs of Sketchers, some TOMS sneakers, and a pair of flats with memory foam when I need a bit more “formal” look.
[mxke3iz] (score 2, diepte 3) Yes! I have Clark’s and received the discount! They are great!
[mxk5tbp] (score 2, diepte 2) Fair enough, I also like Brooks running shoes, well-made and comfortable 😊
[mxhrchn] (score 2, diepte 0) Merrell jungle mocs.
[mxikw3l] (score 2, diepte 1) This is the way.
[mxjtzje] (score 2, diepte 1) Same ☺️
[mxjtbeo] (score 2, diepte 1) This. I have multiple stools stationed around my room as well as empty tables and desks to serve as vantage points. This has saved my feet and back tremendously.
[mxkadph] (score 2, diepte 3) Hokas also have a couple models that are so orthotic that you could use your HSA to pay for them online. I go to Scheels and try them on and then go online to purchase for this and there's more color options online.
[mxnda16] (score 2, diepte 3) In case they don't fit perfectly you have them at least not fitting perfectly in different ways which may reduce injury for repetitive pressure points, etc.
[mxjqmno] (score 2, diepte 2) I’ve got their boots and clogs. Definitely not as great as the sandals. They are both loose. I’ve had to make more holes on the straps to keep them from Sliding around. They aren’t cheap.
[mxj5kht] (score 2, diepte 1) “Shoes wear out in six months”?

What? I have a pair of Red Wings I’ve had for 9 years and a couple of pairs of RM Williams I’ve had more than 10 years. But quality, look after your shoes, rotate and you should get years out of your shoes.
[mxl9k99] (score 2, diepte 1) The real ones tho, even tho they are pricey
[mxiowo6] (score 2, diepte 1) I too, wear Eccos daily. Am a dude who wears a tie almost everyday, and the Eccos complete the outfit. Look like dress shoes, feel like cross trainers.
[mxidfs3] (score 2, diepte 0) Superfeet insoles that have been picked for you by the fleet feet machine. Worth every penny, but have it be replaced pretty regularly
[mxlc2hf] (score 2, diepte 2) Yes. I wore brooks for awhile but their quality went down and switched to asics gel nimbus. Like the best shoe ever!
[mxief86] (score 2, diepte 0) Brooks runnners all the way. I don’t even try to match my outfits anymore with my shoes. I own 20 pairs of vans and converse but I mostly just wear my brooks.
[mxios0h] (score 2, diepte 0) Clark’s
[mxiszi9] (score 2, diepte 0) Hokas, Clarks
(274 reacties met lagere score weggelaten)

