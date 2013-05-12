#Abstract

#Introduction
1.  Why are these systems important

2.  Why are we writing this paper
    * Aggregate knowledge on the subject as a whole bc for the most part it is
        distributed
    * Write to a less knowledgeable audience, treating this as an introduction to
        the field of study

3. Lay out the structure of the paper, including each type of attack
    * Why did we choose this taxonomy?
        - It was how the DARPA data set was broken up, and seemed like the highest level description that covered all cases
        - <!-- JAKE, THIS IS WHERE YOU WILL TALK ABOUT THE DECISION TO MERGE YOUR TWO TOPICS --!>
    
#Body
Intrusion Detection Systems [Mell,Peter @ EDPACS unless otherwise stated]
-----------------------------
1.  Audit Systems
    * Network based
        * Analyse behavior of a network by monitoring network loads and packet headers
        * Adv:
            - Network based signature detection systems can easily cover an entire network
            - Easy to retro fit onto an existing network
            - Little impact on network performance
            - Easy to secure from attack
        * Dis:
            - Performance is generally inversely proportional to traffic load i.e. may fail to detect attacks during high periods of traffic
            - Increases in speed usually lead to decreases in accuracy and these systems need to be fast
            - Do not work well in switch based networks, specifically one implemented with switched that lack monitoring ports because all traffic can not be mirrored to the sensors
            - Use is becoming more limited as the use of encrypted network channels is becoming more popular
    * Host based
        * Analyse behavior of a particular host machine by monitoring system logs
        * Adv:
            - Can effectively be used in an encrypted network because they can analyse data after is has been decryted by the host
            - Are able to detect attacks that a network based sensor can not (Ex''s include many privilege escalation types of attacks) because of their ability to monitor one specific hosts behaviour with very fine granularity
            - Fully functional within switched networks
        * Dis:
            - Must be installed and maintained on every host on a network individually
            - Can be the target of an attack because they are processes running on a host machine
            - Usually unable to detect DoS attacks, which are becoming one of the more popular types of attacks 
            - Use up computing resources on the hosts which run them
    * Application Based
        * Analyse behavior of a particular application running on a machine by monitoring that particular applications log files
        * The line between these systems and host based IDS''s is very thin
        * Adv:
            - Fully functional in encrypted environments
            - Able to monitor behavior with the highest level of granularity, and can often track misuse to a particular host
        * Dis:
            - The most vulnerable type of IDS to attack

2.  Event Analysis
    * Signature based
        * The most prominent form of detections used in most IDS''s today
        * They work by looking for predefined patterns in audit data, which means that there must be explicit rules defined for each type of attack.
        * SNORT is a prominent example of a signature based detection system
        * The more explicitly a rule is defined the less false positives it will generate, but the less likely it will be at detecting even slight variations from known attacks.
            * Adv:
                - Can be effective without generating an overwhelming number of false alarms
            * Dis:
                - Are not very good at detecting novel attacks, or even variations from previously seen attacks, so called 'neighboring' attacks [Labib; Vemuri]
    * Anomaly based
        * These systems work by building up a profile of "normal" behavior and detect variations from that profile within a system
        * Usually consist of three phases [Alenizi; Reed]
            - Parameterization: The significant parameters of a system are defined
            - Training: The IDS forms a profile of "normal" behavior
            - Detection: Activity is compared to the training profile and flagged as either normal or abnormal
        * Adv:
            - Able to detect novel attacks
        * Dis:
            - Typically produce large numbers of false positives
            - Require extensive and well made training data sets, which historically are very hard to produce

3. Limitations of IDS''s 
    * Scalability problems: 
        - There is a large human component that it takes to keep an IDS in operation, the larger a system is -> the more sensors it needs -> the more data generated that needs to be evaluated -> more personnel and man hours needed for affective analysis
    * Usually generate a high number of false positives that require an IT analyst to be sorted out
    * Most IDS''s are not insulated from attack themselves
    * Must be maintained by skilled personnel to achieve maximum effectiveness
    * New attacks are generated quicker than IDS''s that can detect them

Breakdown of Attacks and Detection
------------------------------------
(This idea here is to use these major categories of attacks to highlight how intrusion dtection systems work)

1.  Probes
    * Port Scans
        - A port scan is a method of determining what services are running on a host or network by observing the responses from various ports [Bhuyan, Bhattacharyya, Kalitan]
        - Basically a port scan consists of sending a message to every port on a host machine and listening for a response
        - Analogy to walking a neighborhood looking for open doors
        - There are 65,536 defined ports on a given machine [Bhuyan, Bhattacharyya, Kalitan]
    * Information organized by source
        - ###Staniford, Haugland and McAlerney
        - ###Bhuyan, Bhattacharyya, Kalitan
        - ###Sources from Bhuyan, Bhattacharyya, Kalitan

2.  Privilege Escalation
    * Remote to User
        - A remote to user attack is simply an attacker gaining access to a system equivalent to what a local user would be allowed
        - Such attacks can take a staggering array of forms, from obtaining user authentication information without the knowledge of said user, to exploiting application vulnerabilities
        - Note that such an attack is not necessarily malicious, as the breach occuring at all, regardless of any malicious activity performed by the user, categorizes this as a "remote to local" attack
    * User to Root
        - A user to root attack is when an attacker enables themselves to gain privileges greater than what they were assigned by an administrator
        - These attacks often start with an attacker already having local user access to a system, but can be done remotely and skip the step of gaining a local user account
    
3.  Denial of Service
    * Multiple authors argue that signature based detection methods are ineffective for this type of attack [Peng(16), Kompella(21), Cheng(22) all from Alenzi;Reed]
        - However [Alenzi, Reed] argue that signature based methods can be used to rule out simple DoS attacks such as TCP mixed flags attack.
    * General DoS IDS Classification [Alenzi; Reed]
        - IP-Attribute based lassification [Yongua 17 FROM Alenzi;Reed]
            * Packet header parameters are analysed such as source IP, Port and TTL
        - Traffic volume based [" "]
            * Ex''s include MULTOPS, SYN, and other satistical algorithms
    * Information organized by source
        - ### Labib and Venuri
            * They use multivariate statistical approaches to detect DoS and Netptune attacks. More specifically, they use Principle Component Analysis to reduce the multidementional space represented by network feature vectors for real time analysis. They are able to detect 100% of attacks, however, the data set they use has been highly criticized and is far outdated. 
        - ### Sources from Alenezi and Reed
        - ### Sourced from Labib and Venuri, LOOK IN RELATED WORK
Conclusion
----------
    * Talk about data sets
        * The design of a training data set is paramount in IDS performance, mainly anomaly based systems, but that is where this field is trending
        * DARPA data set <!-- DOES THIS BELONG HERE? --!>
            - One of the most prolific training sets out there
            - Highly criticized [Brugger, Terry; Chow, Jedediah]
                * Outdated
                * Did not adequately represent real network traffic [McHugh && Malhony; Chan]
                * <!-- MORE TO FOLLOW FROM BRUGGER; CHOW --!>

    * Most probing activity can be detected using signature based methods
        * BUT WHAT SHOULD ONE DO WITH THIS INFORMATION?
            - Some people ignore it
            - Others block those IP addrs
        
    * A multi-tiered system is the most effective
        * Network based sensors configured for detecting probing activity
        * host based sensors for privilege escalation attacks
        * Needs to be used in conjunction with a file wall/defence system

    * Open Problems in the field
        * Generating meaningful, labeled, and representative data sets for training
        * Designing systems that can detect novel attacks while also producing few false alarms


