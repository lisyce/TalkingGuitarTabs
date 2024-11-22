# CSE 493 Final Project Handin: Talking Guitar Tabs

**Names: Cara Lisy and Jasmine Herri**

TODO: Cara
## Introduction (in plain language) – ~2 paragraphs (about 750 words): 

Comptency info: You can follow best practices for text simplification and ensure that everyone in the disability community can benefit from information that is shared.
- 3: Demonstrates consistent use of and understanding of five or more principles	
- 2: Demonstrates consistent use of and understanding of four or more principles	

### The problem we are solving

### Why it is important to solve this problem

## Positive Disability Principals ~3-5 paragraphs: Address the questions in this competency

### Ableist
This technology is not ableist. It is tailored specifically for people with low vision, reading, or cognitive processing disabilities that results in it being difficult to read guitar tabs. This project tackles the visual barrier of guitar tabs and converts them into an textual and potentially auditory form when read with a screen reader. While this product does not only have to be used by people with disabilities, it is not discriminatory against disabled individuals. It can be used by anyone who either needs or prefers non-visual musical representation whether they are disabled or not. This includes people who are visually impaired or people who are auditory learners. This product is also not a disability dongle because both of our first person accounts explained the difficulties of reading existing sheet music. Therefore, the Talking Guitar Tabs web application is a reasonable solution for a real problem in the disabled community. 

### Accessible in part or as a whole
This product is accessible as a whole. It completely translates visual guitar tabs into a textual and auditory form. It is not a partial translation nor does it require a significant amount of user action. This translation includes all imperative information in the original sheet music including key, time signature, and tempo per measure. The Talking Guitar Tabs web application also provides users with the option of showing this information for every measure or not. Therefore, not only are the guitar tabs more accessible in the app, but users are given autonomy in how they want to use it, giving them more control on how they process the music being interpreted. This app also addresses a variety of disabilities ranging from low vision/blindness to dyslexia and cognitive-processing disorders. Thus, this app reaches many different groups within the disabled community, contributing to its accessibilty as a whole. 

### Disability led
This product is not disability led. Neither of the group members possess the visual or cognitive disabilities that could benefit from this product. However, as previously mentioned, this product is not limited to use by disabled individuals only. It can also be used by people who simply prefer auditory instruction over visual cues. Moreover, we based this product on multiple first-person accounts by people with disabilities as described in our proposal. These first-person accounts detailed the difficulties of visual music reading from their personal experience, supporting the development of this product.

### Being used to give control and improve agency for people with disabilities
This product definitely gives controls and improves agency for people with disabilities. It allows individuals to choose what method they want to learn music in. Even within this app, with the textual representation of the music, users can both magnify the text for interpretation or use a screen reader to read the information aloud. This, this web app frees users from the limitations of textual sheet music in multiple ways. Also, in the Concert Band and Low Vision first person account, the writer talked about  how “a school paraprofessional would resize my music on larger paper and print it horizontally, and my directors would work with me to ensure no notes or important symbols were cut off.” This tool with remove the dependence on other people to provide accessible music, improving agency for people with disabilities.  In addition, as previously mentioned, the Talking Guitar Tabs web application also provides users with the option of showing the key, time signature, and tempo for every measure or not. Therefore, users are given autonomy in how they want to use the app, giving them more control on how they process the music they want to interpret.

### Addressing the whole community
This product does not address the whole community because it is specifically tailored towards individuals with visual or cognitive disabilities. This product would not be effective for those with hearing impairments since the output either textual but in a different format than before or auditory with a screen reader. It also does not directly address nor exclude those with mobility issues. Even though the product is not aimed to be incredibly complex to use, the goal was not to improve mobility concerns for musicians.

TODO: Cara
## Related Work– ~3 paragraphs: Talk about relevant work that closely connects with your project.

TODO: Cara reads over Jasmine's work 
## Methodology and Results– ~6 paragraphs : 

### What we designed and implemented
We designed a Flask application that takes in a .musicXML file and then parses it into a text format that can be read by a screen reader. The output of the file parser looks like this:

h1: Title
    h2: Song summary
        Composer
        # of measures 
    h2: Formatting options 
        Toggle: show time, key, and tempo every measure
    h2: Measures
        h3: Measure 1
            Time signature
            Key 
            Tempo 
            - <note duration>, <string #, fret #>, <string #, fret #>
            - <note duration>, <string #, fret #>
        h3: Measure 2
            Etc. 

Specifically, we extracted the time signature, key, and tempo for each measure. We also extracted the notes and chords of the measure. We then placed this information into a customized dictionary as the output of our parser. 

On the Flask side, we have a home page template and a guitar_tab_template. The home page accept the .musicXML file through a form submission and the guitar_tab_template shows the parsed results. 

One of the key things we implemented was the toggle under Fomratting Options that controls whether the user sees the the time, key, and tempo every measure. This toggle is automatically set to true when the page laods. When it is set to false, then the time, key, and tempo are only displayed if they change. For example, if the tempo is different in Measure 3 than in Measure 2 then the tempo will be dislayed in Measure 3. Since the time sigature and the key didn't change, they are not displayed in Measure 3. 

### Metrics for success
- Web application is keyboard navigable
- HTML output of the MusicXML file is navigable with a screen reader 
- Web application meets WCAG guidalines for font size, colors, spacing, etc. 
- Appropriate aria labels on HTML components

### Validating metrics
To validate our metrics, we tested the web application with a screen reader to check the keyboard navigation and aria labels. We made there that there were no empty lines being read aloud and that users have the autonomy to skip over information they may not want to listen while still maintianing the flow of the music. We then ran out web application through an automated checker for WCAG guidelines to ensure those are met, making adjustments accordingly. 

### Image ADD ALT TEXT

## Disability Model Analysis ~3 paragraphs (one per principal)

Competency info: You can argue for how a given technology or research project, including your own, meets or fails to meet appropriate disability principles drawn from from disability justice’s 10 principles laid out by Sins Invalid.
- 3: Uses three or more principals correctly (including defining them and correctly explaining why they apply)	
- 2: Uses at least two principals correctly	

Disability principles: https://static1.squarespace.com/static/5bed3674f8370ad8c02efd9a/t/5f1f0783916d8a179c46126d/1595869064521/10_Principles_of_DJ-2ndEd.pdf

### Recognizing Wholeness

#### Defintion 
The principle of Recognizing Wholeness acknowledges that every individual is a culmination of past and present experiences. These experiences include their thoughts, emotions, and fantasties. Every person is a whole person, whether they are disabled or not. 

#### Analysis
Music is an inherently personal thing. Many musicians play to evoke the audience's emotions by communicating their experiences through song. The Talking Guitar Tabs web application recognizes wholeness by increasing accessibility to guitar tabs. This project provides another way for guitarists with disabilities--whether they be visual or mobile or otherwise--to perceive the typically visual notes as written, allowing them to interpret music in way that aligs with their own experiences and emotions.

### Intersectionality

#### Defintion 
This principle of Intersectionality refers to the cross-over between a person's discriminatory and non-discriminatory experiences. This overlap can both compound or improve unjust experiences, showing that a person is a culmination of multiple areas of life. Theese areas include the overlap between sexism and racism, ableism and homophobia, etc. 

#### Analysis
Music is a key component of many cultures and religions. Thus, music is an imperative portion of an individual identity in addition to disability. Tabs are one way that these songs can be represented, so increasing accessibility to these tabs can make sharing these cultural perspectives more accessible for blind or low vision musicians who may wish to share music that is part of their identity. Moreover, when it comes to the crossover of different disabilities, someone with both mobile and visual disabilties may struggle with visual guitar tabs. Therefore, the Talking Guitar tabs web application can address this challenging experience by providing an additional method of musical interpretation. 

### Anti-capitalist Politics

#### Defintion 
The Anti-capitalist Politics principle refers to the rejection of a system that prioritizes those who are able-bodied, of the racial majority (typically White), and are gender normative. The rejetion of this system discourages competing for survival and encourages all contributions from all sorts of people.

#### Analysis
While this project (and music itself) is not inherently political, it has the power to both embody and fail to embody this principle depending on how it’s employed. Music can be a leisurely activity, giving listeners a break to feel their emotions or connect with others' emotions. By increasing accessibility for sheet music, we can increase accessibility to making music and the leisurely experience of listening to it. However, music is often also a means to profit. To embody this principle, accessible sheet music formats cannot be a reason to make more monetizable music, but rather more music for enjoyment. Thus, this project does not encourage montetary advancement or competiting for survivial but rather emphasizes additional modes of musical access.


TODO: Cara
## Learnings and future work ~1-2 paragraphs (about 400 words):

### What we learned

### Future applications and extensions