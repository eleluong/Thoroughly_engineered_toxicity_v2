mid_level_policies = {
    "unsafe for children": {
        "child abuse": "Content showing any physical, sexual, emotional, or psychological abuse of minors.",
        "child exploitation": "Content exploiting children through physical labor or other means.",
        "child endangerment": "Content promoting drugs, alcohol, or violence against children.",
        "explicit content": "Content with strong language, violence, or sexual material not suitable for children.",
    },
    "toxicity": {
        "hate speech": "Content showing bias, prejudice, or intolerance against groups based on race, ethnicity, gender, religion, disability, or other traits.",
        "harassment": "Content that threatens, intimidates, or targets people abusively.",
        "toxic behavior": "Content intended to provoke, insult, or cause strong negative reactions.",
    },
    "biases": {
        "gender bias": "Content showing stereotypes or discrimination based on gender.",
        "racial bias": "Content promoting discrimination based on race, ethnicity, or national origin.",
        "systemic bias": "Content reinforcing societal biases related to status, disability, age, or orientation.",
    },
    "mental attack": {
        "bullying": "Content that shows or encourages bullying, intimidation, or aggression.",
        "emotional distress": "Content likely to cause severe emotional distress or anxiety.",
        "psychological manipulation": "Content involving manipulation, gaslighting, or control tactics.",
        "suicidal themes": "Content with references to suicidal thoughts or actions.",
        "trauma triggers": "Content that may trigger past trauma, such as abuse or violence.",
        "verbal abuse": "Content showing verbal attacks, name-calling, or derogatory language.",
    },
}

mid_level_policies_old = {
    "unsafe for children": {
        "child abuse": "Content involving the physical, sexual, emotional, or psychological abuse of minors.",
        "child exploitation": "Content that exploits children through physical or laborious means.",
        "child endangerment": "Content promoting the use of drugs, alcohol, or violence against children.",
        "explicit content": "Content that contains mature or explicit material, such as strong language, violence, or sexuality, which may be unsuitable for children.",
    },
    "toxicity": {
        "hate speech": "Content that expresses bias, prejudice, or intolerance against individuals or groups based on characteristics like race, ethnicity, national origin, sexual orientation, gender, gender identity, religious affiliation, age, disability, or serious disease.",
        "harassment": "Content that threatens, intimidates, or targets an individual or group in an abusive or aggressive manner.",
        "toxic behavior": "Content that is designed to provoke, antagonize, insult, or otherwise elicit strong negative emotional reactions from others.",
    },
    "biases": {
        "gender bias": "Content that expresses prejudice, stereotypes, or discrimination based on gender identity or expression.",
        "racial bias": "Content that promotes bias, discrimination, or intolerance towards individuals or groups based on race, ethnicity, or national origin.",
        "systemic bias": "Content that reinforces or amplifies existing societal biases or inequalities related to factors like socioeconomic status, disability, age, sexual orientation, or other protected characteristics.",
    },
    "mental attack": {
        "bullying": "Depicts or encourages bullying, intimidation, or aggressive behavior.",
        "emotional distress": "Features imagery that can induce severe emotional distress or anxiety.",
        "psychological manipulation": "Depicts scenarios involving manipulation, gaslighting, or psychological control.",
        "suicidal themes": "Incorporates elements related to suicidal ideation or attempts.",
        "trauma triggers": "Contains imagery that may trigger past traumas, such as abuse or violence.",
        "verbal abuse": "Shows or encourages verbal attacks, name-calling, or derogatory language.",
    },
}

high_level_policies = {
    "unsafe for children": "Content unsuitable or harmful for children, with explicit discussions of abuse, bullying, sexuality, or behaviors that could harm children.",
    "toxicity": "Content with abusive or toxic language aimed at individuals or groups, such as personal attacks, slurs, or harassment.",
    "biases": "Content showing unfair bias that favors a particular perspective or outcome, potentially harming individuals or groups.",
    "mental attack": "Content promoting psychological manipulation or emotional abuse, undermining someone's self-worth, decision-making, or mental well-being, such as through gaslighting or coercion.",
}

high_level_policies_old = {
    "unsafe for children": "Content includes information that is unsuitable or potentially harmful for children, such as explicit discussions of child abuse, bullying, sexuality, or the promotion of behaviors that could endanger children.",
    "toxicity": "Content includes toxic or abusive language targeting readers or other individuals/groups, including personal attacks, slurs, or other forms of harassment.",
    "biases": "Content exhibits unfair or prejudicial tendencies that favor a particular perspective, outcome, or decision, potentially causing harm to individuals or groups.",
    "mental attack": "Content that depicts or encourages psychological manipulation, mind games, or other forms of mental/emotional assault designed to undermine an individual's sense of self, decision-making ability, or mental well-being. This includes, but is not limited to, gaslighting, emotional abuse, psychological coercion, and mind games.",
}

low_level_policies = {
    "unsafe for children": {
        "child abuse": {
            "physical": "Content showing the physical abuse or maltreatment of minors.",
            "sexual": "Content depicting the sexual abuse or exploitation of minors.",
            "emotional": "Content depicting the emotional or psychological abuse of minors.",
        },
        "child exploitation": {
            "child pornography": "Content depicting the sexual abuse or exploitation of children.",
            "sexualization": "Content that sexualizes or fetishizes minors.",
            "child labor": "Content promoting, endorsing, or trivializing the use of children in forced or hazardous labor.",
        },
        "child endangerment": {
            "drug use": "Content promoting or instructing minors to use drugs or alcohol.",
            "self harm": "Content encouraging or depicting minors engaging in self-harm.",
            "violence": "Content depicting or promoting violence against children.",
        },
        "explicit content": {
            "sexual content": "Content with explicit sexual material, such as pornography or strong sexual themes, unsuitable for children.",
            "graphic violence": "Content depicting graphic or disturbing violence, such as gore or extreme brutality, unsuitable for children.",
            "strong language": "Content with strong, profane, or inappropriate language unsuitable for children.",
        },
    },
    "toxicity": {
        "hate speech": {
            "racism toxicity": "Content showing bias, prejudice, or intolerance towards individuals or groups based on race, ethnicity, or national origin.",
            "sexism toxicity": "Content showing bias, prejudice, or intolerance towards individuals or groups based on gender or gender identity.",
            "religious intolerance": "Content showing bias, prejudice, or intolerance towards individuals or groups based on religious affiliation or beliefs.",
            "lgbtq discrimination": "Content showing bias, prejudice, or intolerance towards individuals or groups based on sexual orientation or gender identity.",
        },
        "harassment": {
            "threats": "Content that threatens, intimidates, or incites violence against an individual or group.",
            "stalking": "Content that repeatedly targets, monitors, or contacts an individual with intent to harass or alarm.",
            "doxxing": "Content that maliciously publishes an individual's private or identifying information without consent.",
            "hate raids": "Coordinated campaigns to flood or spam an individual or community with abusive, harassing content.",
        },
        "toxic behavior": {
            "insults": "Content that directly insults, demeans, or derogates an individual or group.",
            "trolling": "Content intended to provoke, antagonize, or elicit angry responses from others.",
            "brigading": "Coordinated efforts to mass-report, flag, or otherwise target and harass an individual or community.",
            "glorification of violence": "Content that celebrates, praises, or encourages acts of violence or cruelty.",
        },
    },
    "biases": {
        "gender bias": {
            "sexism biases": "Content showing prejudice, stereotypes, or discrimination based on gender or gender identity.",
            "misogyny": "Content expressing hatred, contempt, or prejudice towards women or girls.",
            "transphobia": "Content expressing prejudice, fear, or hatred towards transgender, non-binary, or gender non-conforming individuals.",
        },
        "racial bias": {
            "racism biases": "Content showing prejudice, stereotypes, or discrimination based on race, ethnicity, or national origin.",
            "antisemitism": "Content showing prejudice, stereotypes, or discrimination towards Jewish people or Judaism.",
            "xenophobia": "Content showing fear, hatred, or intolerance towards people from other countries or cultures.",
        },
        "systemic bias": {
            "institutional discrimination": "Content promoting or reinforcing discriminatory policies, practices, or structures within larger social systems and institutions.",
            "historical oppression": "Content glorifying, denying, or distorting the history of oppression, persecution, and marginalization of protected groups.",
            "social inequities": "Content spreading misinformation or conspiracy theories about the causes of, or solutions to, social, economic, and political inequities.",
        },
    },
    "mental attack": {
        "bullying": {
            "cyberbullying": "Depicts or encourages bullying through digital platforms, including social media or text messages.",
            "physical bullying": "Depicts or encourages physical intimidation or aggressive behavior.",
            "social bullying": "Depicts or encourages exclusion, spreading rumors, or other forms of social intimidation.",
        },
        "emotional distress": {
            "anxiety inducing content": "Features imagery or scenarios that can cause severe anxiety or panic attacks.",
            "graphic imagery": "Contains graphic content that can cause emotional distress or discomfort.",
            "fear tactics": "Uses fear-based methods to manipulate or distress viewers.",
        },
        "psychological manipulation": {
            "gaslighting": "Depicts manipulation intended to make individuals question their reality or sanity.",
            "emotional blackmail": "Depicts manipulation through threats or guilt to control someone's actions.",
            "mind games": "Shows strategic manipulation designed to confuse or control another person.",
        },
        "suicidal themes": {
            "ideation": "Incorporates elements related to suicidal thoughts or fantasies.",
            "attempts": "Depicts or discusses actual attempts of suicide.",
            "methods": "Details or demonstrates methods of committing suicide.",
        },
        "trauma triggers": {
            "abuse": "Contains imagery or scenarios showing physical, emotional, or sexual abuse.",
            "violence": "Depicts graphic violence that can trigger past traumas.",
            "ptsd triggers": "Features content that may trigger post-traumatic stress disorder symptoms.",
        },
        "verbal abuse": {
            "name-calling": "Shows or encourages the use of derogatory names or insults.",
            "derogatory language": "Depicts or promotes the use of degrading or offensive language.",
            "threats": "Shows verbal threats intended to intimidate or harm.",
        },
    },
}


low_level_policies_old = {
    "unsafe for children": {
        "child abuse": {
            "physical": "Content involving the physical abuse or maltreatment of minors.",
            "sexual": "Content involving the sexual abuse or exploitation of minors.",
            "emotional": "Content involving the emotional or psychological abuse of minors.",
        },
        "child exploitation": {
            "child pornography": "Content depicting the sexual abuse or exploitation of children.",
            "sexualization": "Content that sexualizes or fetishizes minors.",
            "child labor": "Content that promotes, endorses or trivializes the use of children in forced or hazardous labor.",
        },
        "child endangerment": {
            "drug use": "Content promoting or instructing minors to use drugs or alcohol.",
            "self harm": "Content encouraging or depicting minors engaging in self-harm.",
            "violence": "Content depicting or  promoting violence against children.",
        },
        "explicit content": {
            "sexual content": "Content containing explicit sexual material, such as pornography or strong sexual themes, that is unsuitable for children.",
            "graphic violence": "Content depicting graphic or disturbing violence, such as gore or extreme brutality, that is unsuitable for children.",
            "strong language": "Content containing strong, profane, or inappropriate language that is unsuitable for children.",
        },
    },
    "toxicity": {
        "hate speech": {
            "racism toxicity": "Content expressing bias, prejudice or intolerance towards individuals or groups based on race, ethnicity or national origin.",
            "sexism toxicity": "Content expressing bias, prejudice or intolerance towards individuals or groups based on gender or gender identity.",
            "religious intolerance": "Content expressing bias, prejudice or intolerance towards individuals or groups based on religious affiliation or beliefs.",
            "lgbtq discrimination": "Content expressing bias, prejudice or intolerance towards individuals or groups based on sexual orientation or gender identity.",
        },
        "harassment": {
            "threats": "Content that threatens, intimidates or seeks to incite violence against an individual or group.",
            "stalking": "Content that repeatedly and maliciously targets, monitors or contacts an individual with the intent to harass or alarm them.",
            "doxxing": "Content that maliciously publishes an individual's private or identifying information without their consent.",
            "hate raids": "Coordinated campaigns to flood, raid or spam an individual or community with abusive, harassing content.",
        },
        "toxic behavior": {
            "insults": "Content that directly insults, demeans or derogates an individual or group.",
            "trolling": "Content intended to provoke, antagonize or elicit angry responses from others.",
            "brigading": "Coordinated efforts to mass-report, flag or otherwise target and harass an individual or community.",
            "glorification of violence": "Content that celebrates, praises or encourages acts of violence or cruelty.",
        },
    },
    "biases": {
        "gender bias": {
            "sexism biases": "Content that expresses prejudice, stereotypes or discrimination based on gender or gender identity.",
            "misogyny": "Content that expresses hatred, contempt or prejudice towards women or girls.",
            "transphobia": "Content that expresses prejudice, fear or hatred towards transgender, non-binary or gender non-conforming individuals.",
        },
        "racial bias": {
            "racism biases": "Content that expresses prejudice, stereotypes or discrimination based on race, ethnicity or national origin.",
            "antisemitism": "Content that expresses prejudice, stereotypes or discrimination towards Jewish people or Judaism.",
            "xenophobia": "Content that expresses fear, hatred or intolerance towards people from other countries or cultures.",
        },
        "systemic bias": {
            "institutional discrimination": "Content that promotes or reinforces discriminatory policies, practices or structures within larger social systems and institutions.",
            "historical oppression": "Content that glorifies, denies or distorts the history of oppression, persecution and marginalization of protected groups.",
            "social inequities": "Content that spreads misinformation or conspiracy theories about the causes of, or solutions to, social, economic and political inequities.",
        },
    },
    "mental attack": {
        "bullying": {
            "cyberbullying": "Depicts or encourages bullying through digital platforms, including social media or text messages.",
            "physical bullying": "Depicts or encourages physical intimidation or aggressive behavior.",
            "social bullying": "Depicts or encourages exclusion, spreading rumors, or other forms of social intimidation.",
        },
        "emotional distress": {
            "anxiety inducing content": "Features imagery or scenarios that can cause severe anxiety or panic attacks.",
            "graphic imagery": "Contains graphic content that can cause emotional distress or discomfort.",
            "fear tactics": "Uses fear-based methods to manipulate or distress viewers.",
        },
        "psychological manipulation": {
            "gaslighting": "Depicts scenarios involving manipulation that makes individuals question their reality or sanity.",
            "emotional blackmail": "Depicts manipulation through threats or guilt to control someone's actions.",
            "mind games": "Shows strategic manipulation designed to confuse or control another person.",
        },
        "suicidal themes": {
            "ideation": "Incorporates elements related to suicidal thoughts or fantasies.",
            "attempts": "Depicts or discusses actual attempts of suicide.",
            "methods": "Details or demonstrates methods of committing suicide.",
        },
        "trauma triggers": {
            "abuse": "Contains imagery or scenarios depicting physical, emotional, or sexual abuse.",
            "violence": "Depicts graphic violence that can trigger past traumas.",
            "ptsd triggers": "Features content that can trigger post-traumatic stress disorder symptoms.",
        },
        "verbal abuse": {
            "name-calling": "Shows or encourages the use of derogatory names or insults.",
            "derogatory language": "Depicts or promotes the use of degrading or offensive language.",
            "threats": "Shows verbal threats intended to intimidate or harm.",
        },
    },
}
