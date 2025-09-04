# Antivirus Engines

The book <a href="https://shop.elsevier.com/books/antivirus-engines/gagniuc/978-0-443-32952-4">Antivirus Engines: From Methods to Innovations, Design, and Applications</a> shows a comprehensive exploration of antivirus engine technologies and their evolution in response to the complex cyber threat landscape. While the first part of the book provides detailed foundational knowledge about operating systems, internet infrastructure, cryptography, and the historical context of malware and defenses, the second part stands out for its deep technical insight into the methodologies and novel solutions driving the next generation of antivirus detection and countermeasures.

> **Note:** The repositories below showcase a few demo algorithmic implementations provided from the total of 127 algorithms presented in 
> *Antivirus Engines: From Methods to Innovations, Design, and Applications* (Elsevier Syngress, 2024). You may find these standalone tools insightful:
> - [Ex. (17) - The Hash table](https://github.com/Gagniuc/Hash-table)
> - [Ex. (19) - Aho-Corasick algorithm](https://github.com/Gagniuc/Aho-Corasick-algorithm)
> - [Ex. (20) - The Bloom filter algorithm](https://github.com/Gagniuc/The-Bloom-filter)
> - [Ex. (42) - Hexadecimal Signature Extractor](https://github.com/Gagniuc/Hexadecimal-Signature-Extractor-for-Aho-Corasick)
> - [Ex. (49) - Optimized HEX Signature Scanner](https://github.com/Gagniuc/Aho-Corasick-Malware-Scanner)
> - [Ex. (52) - Aho–Corasick Native Malware Scanner](https://github.com/Gagniuc/Aho-Corasick-Native-Malware-Scanner)

In the second part, the book systematically dissects the full spectrum of detection techniques employed by modern antivirus engines, moving from classic signature-based scanning to advanced heuristic, algorithmic, and behavioral approaches. It presents in detail the algorithms behind signature matching, such as the use of hash tables, the Aho-Corasick algorithm, Bloom filters, and large-scale hash signature optimization, focusing on the scalability challenges as malware volumes soar. The text goes beyond mere description, presenting new comparative analyses of single and dual MD5/SHA signatures, recursive scan logic, and binary search on massive signature databases, introducing practical algorithms for real-world implementation.

***

<div align="center">
  <img src="https://github.com/Gagniuc/Antivirus-Engines/blob/main/img/antivirus_front.png" alt="Antivirus Engines: From Methods to Innovations, Design, and Applications">
</div>

***

The core novelty of the second part lies in its full treatment of innovative heuristic techniques. The book introduces and unpacks multiparametric heuristics, region-based and information-content-driven signature strategies, Markov chain analysis, perceptron-based heuristics, byte frequency analysis, and genetic algorithm-driven signature convergence-all supported by concrete example code and critical assessment of their detection accuracy. It further explores smart heuristics for context-aware file analysis (including header/extension discrepancies, file hiding, and archive content scanning), real-time process and behavior monitoring, and network-layer integration with process-port correlation. The chapters on disinfection mechanisms and malware banks (vaults, banks, and curator strategies) bring a unique perspective on resilience and post-infection remediation, rounding out the modern vision for autonomous, adaptive antivirus technologies. The latter half of the book is a thorough, methodical reference for professionals and researchers looking to understand not just how antivirus engines function today, but where the frontier of detection methodology and automated malware analysis is headed. The novelty lies in the integration of engineering insight gained from the <i>Scut Antivirus</i> project, practical algorithmic guidance, and forward-looking analysis of heuristic and machine learning models that are shaping the future of cybersecurity.

# About: “Antivirus Engines” (IEEE Spectrum)
The <a href="https://spectrum.ieee.org/antivirus-software">IEEE Spectrum</a> article on antivirus software documents the release in 2024 of the very first book devoted to antivirus (AV) engines. This publication marks a significant milestone in computer security history, offering an in-depth exploration of the core techniques, innovations, design, and real-world applications of AV engines-systems at the heart of detecting and defeating malware. Key points about this book: a) It contains a total of 127 implementations. b) Acknowledged by IEEE Spectrum as the first book dedicated to antivirus engines, it establishes a foundation for both academic research and industry development. c) It covers a broad spectrum of topics, including detection methods, performance issues, heuristic design, evasion techniques, and future innovations. d) This work contributes to new understanding and advances in the ongoing battle against cyber threats. If you are looking to learn not only how antivirus tools work, but also the engineering principles and technical breakthroughs behind them, this book, as introduced by <a href="https://spectrum.ieee.org/antivirus-software">IEEE Spectrum</a>, is a must-read and a unique contribution to the cybersecurity field. Link to the article: <a href="https://spectrum.ieee.org/antivirus-software">IEEE Spectrum: Antivirus Software</a> (overview and context for the book)

<div align="center">
  <img src="https://github.com/Gagniuc/Antivirus-Engines/blob/main/img/author.png" alt="Antivirus Engines: From Methods to Innovations, Design, and Applications">
</div>

# Dedication
I dedicated this book to the people of Europe because their collective story is a testament to cooperation across borders, perseverance in the face of adversity, and an enduring commitment to knowledge and progress. Europe’s legacy of curiosity, debate, and innovation served as a key inspiration throughout the writing process. My hope is that this book, in some small way, reflects the diverse strengths and shared aspirations found across the continent.

![Dedication](https://github.com/Gagniuc/Antivirus-Engines/blob/main/img/dedication.png)

# References

- <i>Paul A. Gagniuc. Antivirus Engines: From Methods to Innovations, Design, and Applications. Cambridge, MA: Elsevier Syngress, 2024. pp. 1-656.</i>

***

<details>
<summary>More [+]</summary>

# Antivirus Engines: From Methods to Innovations, Design, and Applications

A go-to resource for those wanting to fully explore the subject of antivirus software, whether they are brushing up on specifics or approaching the topic for the first time.

## Overview

*Antivirus Engines: From Methods to Innovations and Design* offers an in-depth investigation into the intricacies and advancements in antivirus technology, aimed at professionals and enthusiasts in the field of cybersecurity. This comprehensive guide explores the evolution of detection methods, spanning from traditional signature-based approaches to sophisticated heuristic, behavior-based, and machine learning algorithms that protect against emerging threats. Readers will find detailed analyses of various antivirus solutions, exploring their structure, functionality, and the underlying technologies that ensure robust defense mechanisms against malware.

The second part of the book focuses extensively on practical applications in Python and the design of antivirus systems. It addresses the challenges and techniques involved in creating effective malware scanners, discussing the integration of complex algorithms such as hash tables, Aho-Corasick, and Bloom filters in the context of large-scale signature databases. The text also covers the strategic deployment of these systems within different environments to maximize threat detection and system efficiency. Moreover, it highlights the critical role of interprocess communication and the architecture of client-server models in the scaling and management of antivirus operations.

This resource is indispensable for those looking to enhance their understanding of the technical aspects and operational frameworks of antivirus software, providing the tools and insights necessary to navigate and innovate within this critical area of cybersecurity.

## Key Features

- **Explore Detection Methods**: Learn how antivirus programs utilize a variety of detection methods including signature-based, heuristic, and behavior-based techniques to identify and neutralize threats. This includes innovative uses of machine learning and cloud-based solutions designed to enhance the accuracy and speed of threat detection.
- **Insights into Malware Detection**: Gain insights into the methods and challenges involved in the detection and analysis of malware, including the use of polymorphism, encryption, and other evasion techniques that malware authors employ to thwart detection.
- **Advanced Algorithms**: Understand the application of complex algorithms like Aho-Corasick and Markov Chains in the development of malware scanners and how these contribute to the robustness of detecting known and possible threats.
- **Systematic Categorization**: The main text systematically categorizes various methods for detection and analysis of exploits and malware, including detailed discussions on opcode analysis, pattern matching, and the utilization of cryptographic techniques in malware identification.

## About the Author

Dr. Paul A. Gagniuc is a professor of programming languages at National University of Science and Technology Politehnica Bucharest (NUSTPB) in Romania. Over a period of a decade, Dr. Gagniuc provided an original learning experience for many generations of students from many parts of the world. Dr. Gagniuc is the author of the most cited book in the 200 years history of NUSTPB. He has published numerous high-profile scientific research articles, patents, books and is the recipient of several awards for exceptional scientific results. Moreover, he is the creator of an antivirus project called Scut Antivirus, from which he brings his security expertise, and is also in a teaching position with the Military Technical Academy "Ferdinand I" on security matters.

</details>


# Table of Contents

## 1. History
- 1.1 Introduction  
- 1.2 Early days and mainframe security  
- 1.3 Rise of personal computers and networked systems  
- 1.4 Internet age and global connectivity  
- 1.5 Threats and cybercrime  
- 1.6 Current and future challenges  
- 1.7 Antivirus engines  
- 1.8 Back to the future  
- 1.9 Conclusions  

## 2. The Internet
- 2.1 Introduction  
- 2.2 The structure of the internet  
  - 2.2.1 Physical infrastructure  
  - 2.2.2 Internet Protocol (IP) addressing  
  - 2.2.3 Routing  
  - 2.2.4 Domain Name System (DNS)  
  - 2.2.5 Internet Protocols  
  - 2.2.6 Internet Services and Applications  
- 2.3 Key components  
  - 2.3.1 End-user devices  
  - 2.3.2 Internet Service Providers (ISPs)  
  - 2.3.3 Protocols and standards  
  - 2.3.4 Internet Services and Applications  
- 2.4 Internet Layers  
- 2.5 Internet visibility  
  - 2.5.1 Surface Web  
  - 2.5.2 Deep Web  
  - 2.5.3 Dark Web  
- 2.6 Domains  
  - 2.6.1 Domain Names  
  - 2.6.2 Domain Name System (DNS)  
  - 2.6.3 Domain Name Registrars  
  - 2.6.4 DNS Records  
  - 2.6.5 Domain Name Resolution  
  - 2.6.6 Malware and domains  
  - 2.6.7 Domain Blacklisting  
  - 2.6.8 Domain Redirection and Traffic Hijacking  
- 2.7 Conclusions  

## 3. Operating Systems
- 3.1 Introduction  
  - 3.1.1 Operating System types  
  - 3.1.2 The Windows OS  
- 3.2 Structure of the Windows OS  
  - 3.2.1 Hardware Abstraction Layer  
  - 3.2.2 Windows Kernel  
  - 3.2.3 System processes  
  - 3.2.4 Windows Subsystems  
  - 3.2.5 Windows API  
  - 3.2.6 Windows Services  
  - 3.2.7 Registry  
  - 3.2.8 NTFS File System  
  - 3.2.9 Drivers  
  - 3.2.10 Graphical User Interface  
  - 3.2.11 Security  
- 3.3 The OS structure and malware implications  
  - 3.3.1 Kernel modes vs malware  
  - 3.3.2 HAL vs malware  
  - 3.3.3 Device Drivers vs malware  
  - 3.3.4 File System vs malware  
  - 3.3.5 Process Management vs malware  
- 3.4 Memory Management  
  - 3.4.1 The link to malware  
  - 3.4.2 Targeting memory  
  - 3.4.3 Process injection  
- 3.5 File Management  
  - 3.5.1 The link to malware  
- 3.6 User Interface  
  - 3.6.1 Malware visual tricks  
- 3.7 Networking  
  - 3.7.1 Networking: Link to malware  
  - 3.7.2 Malware tactics  
  - 3.7.3 Frequently attacked ports  
  - 3.7.4 About low level protocols  
  - 3.7.5 Transmission Control Protocol/Internet Protocol  
  - 3.7.6 User Datagram Protocol  
  - 3.7.7 Cybersecurity of TCP/IP  
  - 3.7.8 Cybersecurity of UDP  
- 3.8 Conclusions  

## 4. Operating System APIs
- 4.1 Introduction  
- 4.2 The Windows API  
- 4.3 Key libraries  
  - 4.3.1 Kernel32.dll  
  - 4.3.2 User32.dll  
  - 4.3.3 Gdi32.dll  
  - 4.3.4 Advapi32.dll  
  - 4.3.5 Comctl32.dll  
  - 4.3.6 Shell32.dll  
  - 4.3.7 Netapi32.dll  
- 4.4 APIs and Malware scanners  
  - 4.4.1 Malware signatures  
  - 4.4.2 Heuristics analysis  
  - 4.4.3 Behavior monitoring  
  - 4.4.4 Real-time protection  
  - 4.4.5 Windows Event Log API  
- 4.5 Malware tactics and API libraries  
- 4.6 Conclusions  

## 5. Cryptography
- 5.1 Introduction  
- 5.2 Confidentiality and encryption  
  - 5.2.1 Symmetric and Asymmetric encryption  
  - 5.2.2 Management and confidentiality  
  - 5.2.3 About cryptographic standards and protocols  
- 5.3 Integrity and hash functions  
  - 5.3.1 Cryptographic hash functions  
  - 5.3.2 Examples on SHA-3, SHA-256, MD5  
  - 5.3.3 Verification of data integrity  
- 5.4 Authentication and digital signatures  
  - 5.4.1 Public Key Infrastructure (PKI)  
  - 5.4.2 Digital certificates  
  - 5.4.3 Digital signatures  
  - 5.4.4 Message digest and hash functions  
  - 5.4.5 Signing with private key and verification with public key  
  - 5.4.6 Non-repudiation  
- 5.5 Key exchange and secure communication  
  - 5.5.1 Encryption basics  
  - 5.5.2 Key exchange challenges  
  - 5.5.3 Asymmetric cryptography  
  - 5.5.4 Diffie-Hellman key exchange  
  - 5.5.5 Public Key Infrastructure (PKI)  
  - 5.5.6 Secure communication protocols  
  - 5.5.7 Forward secrecy  
- 5.6 Password security  
- 5.7 Cryptographic techniques in malware  
  - 5.7.1 Code obfuscation and encryption  
  - 5.7.2 Polymorphism and cryptographic keys  
  - 5.7.3 Concealing command-and-control communication  
  - 5.7.4 Ransomware and encryption  
  - 5.7.5 Detection and solution strategies  
- 5.8 Concealment of communication channels  
  - 5.8.1 Encryption  
  - 5.8.2 Tunneling  
  - 5.8.3 Steganography  
  - 5.8.4 Covert channels & Defense strategies  
- 5.9 Malware resistance to analysis  
  - 5.9.1 Code obfuscation  
  - 5.9.2 Packing and encryption  
  - 5.9.3 Anti-debugging techniques  
  - 5.9.4 Polymorphism and Metamorphism  
  - 5.9.5 Challenges and future trends  
- 5.10 Cryptography as a defensive measure  
- 5.11 Future implications and challenges  
- 5.12 The impact of artificial intelligence  
  - 5.12.1 AI in threat detection  
  - 5.12.2 Incident response and threat intelligence  
- 5.13 Conclusions  

## 6. Exploits
- 6.1 Introduction  
- 6.2 Code Injection exploits  
  - 6.2.1 Code injection techniques  
  - 6.2.2 History of Code Injection exploits  
- 6.3 Buffer Overflow exploits  
  - 6.3.1 History of buffer overflow exploits  
  - 6.3.2 Buffer overflow main steps  
  - 6.3.3 Low-level computer languages  
  - 6.3.4 High-level computer languages  
  - 6.3.5 C and C++: At the base of everything  
- 6.4 Format string exploits  
  - 6.4.1 Practical example  
  - 6.4.2 The format specifiers  
  - 6.4.3 The meaning of the output  
  - 6.4.4 A striking demonstration  
  - 6.4.5 The limits of the exploit  
  - 6.4.6 Non-printf examples  
- 6.5 SQL Injection exploits  
  - 6.5.1 Working example  
  - 6.5.2 History of SQL Injection Exploits  
- 6.6 Command injection  
  - 6.6.1 A command injection on a UNIX-like OS  
  - 6.6.2 A command injection on a Windows OS  
  - 6.6.3 A clear and dangerous exemplification  
  - 6.6.4 History of command injection  
- 6.7 Cross-Site Scripting (XSS) exploits  
  - 6.7.1 Mechanisms of XSS exploitation  
  - 6.7.2 A test in a Web Server Environment  
  - 6.7.3 A cross-site scripting exploit  
  - 6.7.4 Evaluate user input as an expression  
  - 6.7.5 History of Cross-Site Scripting exploits  
- 6.8 Remote Code Execution (RCE) exploits  
  - 6.8.1 The mechanisms of RCE  
  - 6.8.2 Example of a simple RCE  
  - 6.8.3 How to test it?  
  - 6.8.4 A second example of a simple RCE  
  - 6.8.5 History of Remote Code Execution exploits  
- 6.9 Privilege escalation exploits  
  - 6.9.1 The mechanisms of privilege escalation  
  - 6.9.2 History of privilege escalation  
- 6.10 Man-in-the-Middle (MitM) exploits  
  - 6.10.1 The mechanisms of MitM exploits  
  - 6.10.2 History of MitM exploits  
- 6.11 Zero-day exploits  
  - 6.11.1 The mechanisms of zero-day exploits  
  - 6.11.2 History of zero-day exploits  
- 6.12 Social engineering exploits  
  - 6.12.1 The mechanisms of social engineering exploits  
  - 6.12.2 History of social engineering exploits  
- 6.13 Denial-of-Service (DoS) and Distributed DOS Exploits  
  - 6.13.1 Mechanisms of DoS and DDoS Attacks  
  - 6.13.2 Brief History of DoS and DDoS Attacks  
- 6.14 Conclusions  

## 7. Malware Types & Classification
- 7.1 Introduction  
- 7.2 Computer languages and malware designs  
- 7.3 List of malware types  
- 7.4 Malware classification  
  - 7.4.1 Malware notation criteria  
- 7.5 Paradigms in computer virus infection  
  - 7.5.1 File Infectors  
  - 7.5.2 Macro Viruses  
  - 7.5.3 Boot Sector Infectors  
  - 7.5.4 Network Viruses  
  - 7.5.5 Email Viruses  
  - 7.5.6 Polymorphic Viruses  
  - 7.5.7 Worms: The mirror of the past  
  - 7.5.8 Malware: Polymorphic vs Metamorphic  
- 7.6 Paradigms in anti-virus disinfection  
  - 7.6.1 Quarantine  
  - 7.6.2 Removal/Cleaning  
  - 7.6.3 System Restore  
  - 7.6.4 Repair/Recovery  
  - 7.6.5 Patching/Vulnerability Remediation  
- 7.7 Conclusions  

## 8. Antivirus Engines
- 8.1 Introduction  
- 8.2 Detection methods  
  - 8.2.1 Signature-based detection  
  - 8.2.2 Behavior-based detection  
  - 8.2.3 Heuristic detection  
  - 8.2.4 Sandbox detection  
  - 8.2.5 Machine learning detection  
  - 8.2.6 Cloud-based detection  
  - 8.2.7 Reputation-based detection  
- 8.3 Antivirus solutions: the structure  
  - 8.3.1 Proactive monitoring  
  - 8.3.2 File Verification and scanning  
  - 8.3.3 Decision and mitigation  
  - 8.3.4 Scheduled scans and updates  
- 8.4 Signature databases  
- 8.5 Antivirus files  
  - 8.5.1 Organisation  
- 8.6 Antivirus persistence  
  - 8.6.1 The invasive OS dependent method  
  - 8.6.2 The non-invasive OS independent method  
  - 8.6.3 File integrity  
  - 8.6.4 Antivirus self-protection model  
  - 8.6.5 File encryption and decryption  
- 8.7 Interprocess Communication (IPC)  
  - 8.7.1 IPC methods  
  - 8.7.2 SendMessage  
- 8.8 The clients, the server and the laboratory  
  - 8.8.1 A historical link  
- 8.9 Conclusions  

## 9. Algorithms
- 9.1 Introduction  
- 9.2 Signature matching with some examples  
- 9.3 The signature lookup process  
  - 9.3.1 <a href="https://github.com/Gagniuc/Hash-table">Hash Tables</a>
  - 9.3.2 Hash Tables (native)  
  - 9.3.3 <a href="https://github.com/Gagniuc/Aho-Corasick-algorithm">Aho-Corasick Algorithm</a>
- 9.4 The hundred million hash signature file  
  - 9.4.1 Hash function: Size and speed  
  - 9.4.2 <a href="https://github.com/Gagniuc/The-Bloom-filter">Bloom filters, caching, and search optimizations</a>
  - 9.4.3 Hardware methods  
  - 9.4.4 Hash tables vs Binary search  
- 9.5 Conclusions  

## 10. MD5/SHA Signatures & Scanners
- 10.1 Introduction  
- 10.2 Single MD5 scanners  
  - 10.2.1 Whole file MD5 signatures & file path  
  - 10.2.2 Whole file MD5 signatures & file name (I)  
  - 10.2.3 A malware scanner using single MD5 signatures (II)  
  - 10.2.4 Signature generator on dual regions and single MD5 signatures (I)  
  - 10.2.5 A malware scanner for dual regions and single MD5 signatures (II)  
  - 10.2.6 Another approach to the same problem  
- 10.3 Dual signatures vs one signature on dual file regions  
  - 10.3.1 Advantages and disadvantages of using signatures for each region  
  - 10.3.2 Advantages and disadvantages of a single signature for multiple regions  
- 10.4 Dual MD5 scanners  
  - 10.4.1 The reference system  
  - 10.4.2 Signature generator for dual MD5 signatures (I)  
  - 10.4.3 Single file scanner for mono MD5 signatures (II)  
  - 10.4.4 Single file scanner for dual MD5 signatures (III)  
- 10.5 Recursive Malware Scanners  
- 10.6 Discussions on speed and efficiency  
  - 10.6.1 Why not more than two MD5 signatures?  
  - 10.6.2 Linear search vs Binary search  
- 10.7 Binary search on signature files  
  - 10.7.1 Signature generator for MD5 binary search (I)  
  - 10.7.2 Scanner using binary search in memory loaded signatures (II)  
  - 10.7.3 Scanner using binary search in memory and extension filter (III)  
  - 10.7.4 Additional considerations  
- 10.8 Hash tables on signature files  
  - 10.8.1 Scanner using hash table on dual MD5 signatures  
  - 10.8.2 Time complexity O(n) vs O(1)  
  - 10.8.3 Large scale signature files  
- 10.9 Conclusions  

## 11. Disinfections, Banks and Vaults
- 11.1 Introduction  
- 11.2 The malware bank considerations  
  - 11.2.1 Malware bank and automatic signature extraction  
  - 11.2.2 The end of file problem  
  - 11.2.3 Self-Sequence alignment  
  - 11.2.4 Elimination of potential confusions  
  - 11.2.5 Signature pre-validation scanner: The curator  
- 11.3 The malware vault  
  - 11.3.1 Malware activation and inactivation by encryption  
- 11.4 Malware (Virus) Disinfection  
  - 11.4.1 Baseline – The executable critical area  
  - 11.4.2 Virus disinfection - A prefix restoration approach  
  - 11.4.3 Mono vs dual regions  
- 11.5 Disinfection by forced deletion  
  - 11.5.1 Privileged processes and their files  
  - 11.5.2 Malware persistence  
  - 11.5.3 The malware process and file terminator  
  - 11.5.4 WARNING: Use the code with extreme caution  
- 11.6 Infection in progress: What now?  
  - 11.6.1 Exclusive file lock on a set of files  
  - 11.6.2 Direct API access: the LockEx example  
  - 11.6.3 A wise note on prevention  
- 11.7 Conclusions  

## 12. Hexadecimal Signatures & Scanners
- 12.1 Introduction  
- 12.2 Hexadecimal inspection  
  - 12.2.1 <a href="https://github.com/Gagniuc/Hexadecimal-Signature-Extractor-for-Aho-Corasick">Alignment of multiple files in hexadecimal (raw)</a>
  - 12.2.2 Header alignment of two files (inf vs normal)  
  - 12.2.3 Pairwise sequence alignment of 2 files (infected vs clean)  
- 12.3 Automatic signature extraction  
  - 12.3.1 The hexadecimal signature generator  
  - 12.3.2 Signature quality: Measurements  
- 12.4 Signature detection  
  - 12.4.1 A primitive malware scanner with wildcard support  
- 12.5 Malware scanners with Aho-Corasick algorithm  
  - 12.5.1 In-Deep - Malware Scanner  
  - 12.5.2 <a href="https://github.com/Gagniuc/Aho-Corasick-Malware-Scanner">High speed - Malware scanner</a> 
- 12.6 Scanner speed and Malware location  
  - 12.6.1 In-depth scanner (with libraries)  
  - 12.6.2 Optimized scanner (with libraries)  
  - 12.6.3 <a href="https://github.com/Gagniuc/Aho-Corasick-Native-Malware-Scanner">Optimized scanner (native Aho-Corasick)</a> 
  - 12.6.4 Results and Discussion  
- 12.7 Polymorphic Malware Scanner: Wildcards  
  - 12.7.1 The meaning of wildcards  
  - 12.7.2 The regex malware scanner  
  - 12.7.3 Aho-Corasick vs Regular expressions  
- 12.8 Conclusions  

## 13. Heuristic Signatures & Scanners
- 13.1 Introduction  
- 13.2 Heuristic detection on a multiparameter strategy  
  - 13.2.1 Signature generator for a multiparametric approach (I)  
  - 13.2.2 Malware scanner using multiparametric signatures (II)  
- 13.3 Heuristic detection on discrete file regions  
  - 13.3.1 Computation of indices on 10 successive file regions  
  - 13.3.2 Computation of a global index for each file region  
  - 13.3.3 Signature generator for discrete file regions (I)  
  - 13.3.4 Malware scanner using discrete file regions (II)  
- 13.4 Heuristic in-depth using Information Content  
  - 13.4.1 The mathematical model  
  - 13.4.2 A concrete example  
  - 13.4.3 Model dissection  
  - 13.4.4 The Information Content  
  - 13.4.5 Signature generator for self-sequence alignment (I)  
  - 13.4.6 Malware scanner using self-sequence alignment (II)  
- 13.5 Heuristic detection on strings  
  - 13.5.1 String extraction from Portable Executables  
  - 13.5.2 The use of extracted strings from executable files  
  - 13.5.3 API function name detection in PE files  
  - 13.5.4 A malware scanner based on weighted findings  
  - 13.5.5 A malware scanner based on the Index of Suspicion  
  - 13.5.6 The whole reasoning behind the API function names  
- 13.6 Heuristic detection using PWMs  
  - 13.6.1 The Entry Point  
  - 13.6.2 What follows the entry point?  
  - 13.6.3 The bytes at the Entry Point  
  - 13.6.4 The 200 bytes coverage  
  - 13.6.5 The PWM generator based on PE Entry Points (I)  
  - 13.6.6 The PWM size on malware detection  
  - 13.6.7 How many positions for a PWM?  
  - 13.6.8 Byte consensus of a malware type  
  - 13.6.9 The conceptualization of ideal byte regions  
  - 13.6.10 The use of byte frequency distribution in the Entry Point  
  - 13.6.11 Malware family classification  
  - 13.6.12 Manual vs Automatic signature extraction  
  - 13.6.13 About integration  
  - 13.6.14 A malware scanner using PWMs (II)  
  - 13.6.15 Virus infection experiments and detection refinement  
- 13.7 Heuristic detection using Markov Chains  
  - 13.7.1 Markov Chains for static analysis  
  - 13.7.2 A Markov Chains signature  
  - 13.7.3 Markov Chains signature generator (I)  
  - 13.7.4 Markov Chains signature scanner (II)  
- 13.8 Heuristic detection using transition matrices  
  - 13.8.1 Transition matrix generator for binary data  
  - 13.8.2 Transition matrix signature generator (I)  
  - 13.8.3 Single file malware scanner (II)  
  - 13.8.4 Malware Scanner with transition matrix signature-based detection  
- 13.9 Heuristics by using perceptrons  
  - 13.9.1 Perceptron data generator for a malware scanner (I)  
  - 13.9.2 Malware scanner - Perceptron level-up binary signature training  
- 13.10 Heuristics by random sampling convergence  
  - 13.10.1 Random sampling - Signature generator  
  - 13.10.2 Signature generator based on random sampling (I)  
  - 13.10.3 Malware signature scanner with signature file and linear search (II)  
  - 13.10.4 Malware scanner with fault tolerant matching and binary search (III)  
  - 13.10.5 Signature Generator vs Malware Scanner  
  - 13.10.6 Signature convergence via genetic algorithms  
- 13.11 Heuristics by searching for opcodes  
  - 13.11.1 The opcodes  
  - 13.11.2 The conditional vs unconditional jumps  
  - 13.11.3 The entry point and unconditional jumps  
  - 13.11.4 Types of jumps  
  - 13.11.5 Heuristic PE File Analyzer  
  - 13.11.6 Single PE file scanner with weighted jumps  
  - 13.11.7 A heuristic scanner using weighted jumps  
- 13.12 Heuristics of Entry Point Obfuscation  
  - 13.12.1 Entry Point: High entropy  
  - 13.12.2 Entry Point: Low entropy  
  - 13.12.3 Entry Point: Moderate entropy  
  - 13.12.4 Entry Point Obfuscation (EPO)  
  - 13.12.5 The baseline scanner (I)  
  - 13.12.6 The EPO scanner (II)  
  - 13.12.7 EPO: Concentration vs Dilution  
  - 13.12.8 The NOP scanner  
- 13.13 Conclusions  

## 14. Smart Scanners & Rabbit Holes
- 14.1 Introduction  
- 14.2 Heuristics on header vs extension  
  - 14.2.1 Multi-file header alignment for signature identification  
  - 14.2.2 File scanner: type vs extension  
  - 14.2.3 Folder scanner for type vs extension verification  
- 14.3 Heuristic multiple file headers  
  - 14.3.1 Folder scanner for multiple file headers  
  - 14.3.2 How to test the scanner?  
- 14.4 Heuristic multiple file extensions  
  - 14.4.1 A scanner for detection of multiple file extensions  
- 14.5 Heuristics on hidden files  
  - 14.5.1 Hidden file scanner  
- 14.6 Scanning the archive content  
  - 14.6.1 A simple look in the archives  
  - 14.6.2 Scanning executable files from inside archives  
  - 14.6.3 Detection workflow in compressed archives  
- 14.7 Registry monitoring  
  - 14.7.1 What is the Windows Registry?  
  - 14.7.2 Physical storage  
  - 14.7.3 Registry baseline (I)  
  - 14.7.4 Windows Registry change detector (II)  
- 14.8 Conclusions  

## 15. Process and User Behavior
- 15.1 Introduction  
- 15.2 The extension frequency  
  - 15.2.1 General file extension count  
  - 15.2.2 File extension count by folder (path)  
  - 15.2.3 File extension relative and overall frequency: baseline reference  
  - 15.2.4 Extension frequency monitoring of suspicious activity  
  - 15.2.5 Directory monitor via Win32 API  
  - 15.2.6 The system folder default paths  
- 15.3 User monitor  
  - 15.3.1 Primitive active window to process path monitor  
  - 15.3.2 Active window to process path monitor for malware detection  
  - 15.3.3 Real-time user activity tracking  
  - 15.3.4 Processes and network connections  
- 15.4 Process monitor  
  - 15.4.1 Frequent processes - baseline map generator (I)  
  - 15.4.2 Anomaly detection through initial process maps (II)  
  - 15.4.3 Process path validation for proactive malware identification (III)  
  - 15.4.4 The overall monitoring strategy  
  - 15.4.5 Process alarm for CPU usage  
  - 15.4.6 A general download & upload network monitoring  
  - 15.4.7 Established connections - network connection monitoring  
  - 15.4.8 Scan all processes under established connection  
  - 15.4.9 Process monitoring for suspicious activity over the network  
  - 15.4.10 Adaptive suspicious scoring thresholds for network monitoring  
  - 15.4.11 Detection of hidden windows  
- 15.5 Conclusions  

## 16. The Network
- 16.1 Introduction  
  - 16.1.1 Communication protocols: in brief  
  - 16.1.2 Ports and their significance: in brief  
  - 16.1.3 Processes and networks  
- 16.2 The firewall  
  - 16.2.1 Stop connection by PID and IP  
  - 16.2.2 List all processes and ports/IP  
  - 16.2.3 List only processes with connections  
  - 16.2.4 Monitor processes with open ports  
  - 16.2.5 Stop process connection with GUI  
  - 16.2.6 The Command Prompt tools  
  - 16.2.7 Integration of netstat output into a GUI  
  - 16.2.8 Pièce de résistance: The PE file vs. the network  
- 16.3 Conclusions  

## 17. Appendices
- 17.1 Appendix 1 - Executable file extensions  
- 17.2 Appendix 2 - PWM to JSON  
- 17.3 Appendix 3 - File headers  
- 17.4 Appendix 4 - Running processes  
- 17.5 Appendix 5 - Hidden windows  
- 17.6 Appendix 6 - Registry snapshots  
- 17.7 Appendix 7 - Registry key list  
- 17.8 Appendix 8 - Built-in tools and utilities  
- 17.9 Appendix 9 - CMD built-in commands  
- 17.10 Appendix 10 - A general overview of Scut Antivirus  
  - 17.10.1 The webpage  
  - 17.10.2 The laboratory  
  - 17.10.3 The setup wizard  
  - 17.10.4 The on-demand scanner  
  - 17.10.5 Scanner settings  
  - 17.10.6 Full & Critical scans  
  - 17.10.7 Tests & results  
  - 17.10.8 The output of the scan  
  - 17.10.9 File/process organization  
  - 17.10.10 The communication protocol  
  - 17.10.11 Firewall (I)  
  - 17.10.12 Firewall (II)  
  - 17.10.13 Process monitor & Scanning  
  - 17.10.14 Network monitoring & Scanning  
  - 17.10.15 Proactive firewall (III)  
  - 17.10.16 CPU monitor & Process role  
  - 17.10.17 Security logs  
  - 17.10.18 Graphical User Interface  
  - 17.10.19 The VX Heaven website  
- 17.11 Appendix 10 - Words of wisdom  
- 17.12 Glossary

## References

***

- <i>Paul A. Gagniuc. Antivirus Engines: From Methods to Innovations, Design, and Applications. Cambridge, MA: Elsevier Syngress, 2024. pp. 1-656.</i>

