Abstract
===========

Introduction
==============
1.  Why are these systems important

2.  Why are we writing this paper
    * Aggregate knowledge on the subject as a whole bc for the most part it is
        distributed
    * Write to a less knowledgeable audience, treating this as an introduction to
        the field of study

3. Lay out the structure of the paper, including each type of attack
    

Body
=======
Intrusion Detection Systems [Mell,Peter @ EDPACS unless otherwise stated]
-----------------------------
1.  Audit Systems
    * Network based
        * Analyse behavior of a network by monitoring network loads and packet headers
        * Adv:
            - Little impact on network performance
            - Easy to secure from attack
            - Do not work well in switch based networks, specifically one implemented with switched that lack monitoring ports because all traffic can not be mirrored to the sensors
            - Use is becoming more limited as the use of encrypted network channels is becoming more popular
        * Dis:
            - Performance is generally inversely proportional to traffic load i.e. may fail to detect attacks during high periods of traffic
            - Increases in speed usually lead to decreases in accuracy and these systems need to be fast
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
        * 
    * Anomaly based

Breakdown of Attacks and Detection
------------------------------------
(This idea here is to use these major categories of attacks to highlight how intrusion dtection systems work)

1.  Probes
    * Port Scans

2.  Privilege Escalation
    * Remote to User
    * User to Root
    
3.  Denial of Service
    * Distributed Denial of Service (DDos) 

Conclusion
------------
    What the hell have we learned??
    Cats!
    
    * Most probing activity can be detected using signature based methods
        * BUT WHAT SHOULD ONE DO WITH THIS INFORMATION?
        
    * A multi-tiered system is the most effective
        * Network based sensors configured for detecting probing activity
        * host based sensors for privilege escalation attacks
        * Needs to be used in conjunction with a file wall/defence system



