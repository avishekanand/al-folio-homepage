---
layout: page
title: Question Answering on the Curated Web
description: Resources for the tutorial on Question Answering as presented in SIGIR 2020, and ICTIR 2021
img: assets/img/qa-tute-20.png
importance: 2
category: tutorials
giscus_comments: false
---

The last few years have seen an explosion of research on the topic of automated question answering (QA), spanning the communities of information retrieval, natural language processing, and artificial intelligence. This tutorial would cover the highlights of this really active period of growth for QA to give the audience a grasp over the families of algorithms that are currently being used. We partition research contributions by the underlying source from where answers are retrieved: curated knowledge graphs, unstructured text, or hybrid corpora. We choose this dimension of partitioning as it is the most discriminative when it comes to algorithm design. Other key dimensions are covered within each sub-topic: like the complexity of questions addressed, and degrees of explainability and interactivity introduced in the systems. We would conclude the tutorial with the most promising emerging trends in the expanse of QA, that would help new entrants into this field make the best decisions to take the community forward. Much has changed in the community since the last tutorial on QA in SIGIR 2016, and we believe that this timely overview will indeed benefit a large number of conference participants.

This half-day tutorial is divided into two parts of 90 minutes each -- QA over Knowledge graphs, and QA over Text. The schedule and slides are below.

<br>

## Contents

1.  **[Question Answering over Knowledge Graphs](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr.pdf)** by [Rishiraj Saha Roy](http://people.mpi-inf.mpg.de/~rsaharo/). [[Full Video]](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr.mp4)
    - [Background](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-1.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-1.mp4)
    - [Simple QA](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-2.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-2.mp4)
    - [Complex QA](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-3.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-3.mp4)
    - [Heterogeneous QA](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-4.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-4.mp4)
    - [Conversational QA](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-5.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-5.mp4)
    - [Summary](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-6.pdf). [:movie_camera:](http://people.mpi-inf.mpg.de/~rsaharo/sigir20slides_rsr-part-6.mp4)

<br>

2.  **[Question Answering over Textual Sources](../qa-sigir-20/text-intro.pdf)** by [Avishek Anand](http://www.avishekanand.com)
    - [Background](../qa-sigir-20/text-intro.pdf) [:movie_camera:](../qa-sigir-20/video/text-intro.mp4)
    - [Machine Reading Comprehension](../qa-sigir-20/text-mrc.pdf) [:movie_camera:](../qa-sigir-20/video/text-mrc.mp4)
    - [Open-domain QA](../qa-sigir-20/text-odqa.pdf) [:movie_camera:](../qa-sigir-20/video/text-odqa.mp4)
    - [Feedback and Interpretability](../qa-sigir-20/text-feedback-interpretability.pdf) [:movie_camera:](../qa-sigir-20/video/text-feedback-interpretability.mp4)
    - [Conversational QA](../qa-sigir-20/text-conversational-qa.pdf) [:movie_camera:](../qa-sigir-20/video/text-conv-qa.mp4)
    - [Summary](../qa-sigir-20/text-conclusions.pdf)

<br>

---

## References

<br>

[1] Abdalghani Abujabal,Rishiraj Saha Roy,Mohamed Yahya,and Gerhard Weikum. 2017. QUINT: Interpretable Question Answering over Knowledge Bases. In EMNLP.

[2] Abdalghani Abujabal, Rishiraj Saha Roy, Mohamed Yahya, and Gerhard Weikum. 2018. Never-ending learning for open-domain question answering over knowledge bases. In WWW.

[3] Abdalghani Abujabal,Rishiraj Saha Roy,Mohamed Yahya,and Gerhard Weikum. 2019. ComQA: A Community-sourced Dataset for Complex Factoid Question Answering with Paraphrase Clusters. In NAACL-HLT ’19.

[4] Abdalghani Abujabal,Rishiraj Saha Roy,Mohamed Yahya,and Gerhard Weikum. 2017. Automated template generation for question answering over knowledge graphs. In WWW.

[5] Eugene Agichtein,David Carmel,Dan Pelleg,Yuval Pinter,and Donna Harman. 2015. Overview of the TREC 2015 LiveQA Track. In TREC.

[6] Aditya Kalyanpur Alfio Gliozzo and James Fan. 2012. Natural language process- ing in Watson. In NAACL-HLT.

[7] Avishek Anand, Lawrence Cavedon, Hideo Joho, Mark Sanderson, and Benno Stein. 2020. Conversational Search (Dagstuhl Seminar 19461). Dagstuhl Reports 9, 11 (2020).

[8] Sören Auer, Christian Bizer,Georgi Kobilarov, Jens Lehmann, Richard Cyganiak, and Zachary Ives. 2007. DBpedia: A nucleus for a Web of open data. (2007).

[9] Junwei Bao, Nan Duan, Zhao Yan, Ming Zhou, and Tiejun Zhao. 2016. Constraint-based question answering with knowledge graph. In COLING.

[10] Hannah Bast and Elmar Haussmann. 2015. More accurate question answering on Freebase. In CIKM.

[11] Jonathan Berant, Andrew Chou, Roy Frostig, and Percy Liang. 2013. Semantic parsing on Freebase from question-answer pairs. In EMNLP.

[12] Nikita Bhutani, Xinyi Zheng, and HV Jagadish. 2019. Learning to Answer Complex Questions over Knowledge Bases with Query Composition. In CIKM.

[13] Kurt Bollacker, Colin Evans, Praveen Paritosh, Tim Sturge, and Jamie Taylor. 2008. Freebase: A collaboratively created graph database for structuring human knowledge. In SIGMOD.

[14] Pavel Braslavski, Denis Savenkov, Eugene Agichtein, and Alina Dubatovka. 2017. What do you mean exactly? Analyzing clarification questions in CQA. In CHIIR.

[15] Danqi Chen, Adam Fisch, Jason Weston, and Antoine Bordes. 2017. Reading Wikipedia to Answer Open-Domain Questions. In ACL.

[16] Yu Chen, Lingfei Wu, and Mohammed J Zaki.2019. Bidirectional Attentive Memory Networks for Question Answering over Knowledge Bases. In NAACL-HLT.

[17] Eunsol Choi, He He, Mohit Iyyer, Mark Yatskar, Wen-tau Yih, Yejin Choi, Percy Liang, and Luke Zettlemoyer. 2018. QuAC: Question answering in context. In EMNLP.

[18] Philipp Christmann, Rishiraj Saha Roy, Abdalghani Abujabal, Jyotsna Singh, and Gerhard Weikum. 2019. Look before you Hop: Conversational Question Answering over Knowledge Graphs Using Judicious Context Expansion. In CIKM.

[19] Christopher Clark and Matt Gardner. 2018. Simple and Effective Multi-Paragraph Reading Comprehension. In ACL.

[20] Charles L. A. Clarke and Egidio L. Terra. 2003. Passage retrieval vs. document retrieval for factoid question answering. In SIGIR.

[21] Daniel Cohen, Liu Yang, and W Bruce Croft. 2018. WikiPassageQA: A benchmark collection for research on non-factoid answer passage retrieval. In SIGIR.

[22] Silviu Cucerzan and Eugene Agichtein. 2005. Factoid Question Answering over Unstructured and Structured Web Content. In TREC.

[23] Jeffrey Dalton,Chenyan Xiong,and Jamie Callan.2019. CAsT2019: The conversational assistance track overview. In TREC.

[24] Rajarshi Das, Shehzaad Dhuliawala, Manzil Zaheer, Luke Vilnis, Ishan Durugkar, Akshay Krishnamurthy, Alex Smola, and Andrew McCallum. 2018. Go for a walk and arrive at the answer: Reasoning over paths in knowledge bases using reinforcement learning. In ICLR.

[25] Rajarshi Das, Manzil Zaheer, Siva Reddy, and Andrew McCallum. 2017. Question Answering on Knowledge Bases and Text using Universal Schema and Memory Networks. In ACL.

[26] Pradeep Dasigi, Nelson F Liu, Ana Marasovic, Noah A Smith, and Matt Gard- ner. 2019. Quoref: A reading comprehension dataset with questions requiring coreferential reasoning. In EMNLP-IJCNLP.

[27] Mostafa Dehghani, Hosein Azarbonyad, Jaap Kamps, and Maarten de Rijke. 2019. Learning to transform, combine, and reason in open-domain question answering. In WSDM.

[28] Laura Dietz, Manisha Verma, Filip Radlinski, and Nick Craswell. 2017. TREC Complex Answer Retrieval Overview. In TREC.

[29] Jiwei Ding, Wei Hu, Qixin Xu, and Yuzhong Qu. 2019. Leveraging Frequent Query Substructures to Generate Formal Queries for Complex Question Answering. In EMNLP-IJCNLP.

[30] Xin Dong, Evgeniy Gabrilovich, Geremy Heitz, Wilko Horn, Ni Lao, Kevin Murphy, Thomas Strohmann, Shaohua Sun, and Wei Zhang. 2014. Knowledge vault: A web-scale approach to probabilistic knowledge fusion. In KDD.

[31] Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. 2019. DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs. In NAACL-HLT.

[32] Ahmed Elgohary, Chen Zhao, and Jordan Boyd-Graber. 2018. A dataset and baselines for sequential open-domain question answering. In EMNLP.

[33] Anthony Fader, Luke Zettlemoyer, and Oren Etzioni. 2013. Paraphrase-driven learning for open question answering. In ACL.

[34] Anthony Fader, Luke Zettlemoyer, and Oren Etzioni. 2014. Open question an- swering over curated and extracted knowledge bases. In KDD.

[35] James Fan and Ken Barker. 2015. Natural language processing in Watson. In AAAI.

[36] David Ferrucci, Eric Brown, Jennifer Chu-Carroll, James Fan, David Gondek, Aditya A. Kalyanpur, Adam Lally, J. William Murdock, Eric Nyberg, John Prager, Nico Schlaefer, and Chris Welty. 2010. Building Watson: An overview of the DeepQA project. AI magazine 31, 3 (2010).

[37] Bert F Green Jr, Alice K Wolf, Carol Chomsky, and Kenneth Laughery. 1961. Baseball: An automatic question-answerer. In Western joint IRE-AIEE-ACM computer conference.

[38] Daya Guo, Duyu Tang, Nan Duan, Ming Zhou, and Jian Yin. 2018. Dialog-to-action: Conversational question answering over a large-scale knowledge base. In NeurIPS.

[39] Yangyang Guo, Zhiyong Cheng, Liqiang Nie, Yibing Liu, Yinglong Wang, and Mohan Kankanhalli. 2019. Quantifying and Alleviating the Language Prior Prob- lem in Visual Question Answering. In SIGIR.

[40] Sanda Harabagiu and Dan Moldovan. 2001. Open-domain textual question answering. In NAACL-HLT.

[41] Sen Hu, Lei Zou, Jeffrey Xu Yu, Haixun Wang, and Dongyan Zhao. 2017. Answering natural language questions by subgraph matching over knowledge graphs. TKDE 30, 5 (2017).

[42] Sen Hu, Lei Zou, and Xinbo Zhang. 2018. A state-transition framework to answer complex questions over knowledge base. In EMNLP.

[43] Xiao Huang, Jingyuan Zhang, Dingcheng Li, and Ping Li. 2019. Knowledge graph embedding based question answering. In WSDM.

[44] Mohit Iyyer, Wen-tau Yih, and Ming-Wei Chang. 2017. Search-based neural structured learning for sequential question answering. In ACL.

[45] Zhen Jia, Abdalghani Abujabal, Rishiraj Saha Roy, Jannik Strötgen, and Gerhard Weikum. 2018. TEQUILA: Temporal Question Answering over Knowledge Bases. In CIKM.

[46] Magdalena Kaiser, Rishiraj Saha Roy, and Gerhard Weikum. 2020. Conversa- tional Question Answering over Passages by Leveraging Word Proximity Net- works. In SIGIR.

[47] Tushar Khot, Ashish Sabharwal, and Peter Clark. 2017. Answering Complex Questions Using Open Information Extraction. In ACL.

[48] Bernhard Kratzwald and Stefan Feuerriegel. 2019. Learning from on-line user feedback in neural question answering on the web. In WWW.

[49] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, and Ken- ton Lee. 2019. Natural questions: A benchmark for question answering research. TACL 7 (2019).

[50] Patrick Lewis, Ludovic Denoyer, and Sebastian Riedel. 2019. Unsupervised Ques- tion Answering by Cloze Translation. In ACL.

[51] Fei Li and HV Jagadish. 2014. Constructing an interactive natural language interface for relational databases. In VLDB.

[52] Jimmy Lin and Boris Katz. 2003. Question answering techniques for the World Wide Web. In EACL.

[53] YankaiLin,HaozheJi,ZhiyuanLiu,andMaosongSun.2018.Denoisingdistantly supervised open-domain question answering. In ACL.

[54] Xiaolu Lu, Soumajit Pramanik, Rishiraj Saha Roy, Abdalghani Abujabal, Yafang Wang, and Gerhard Weikum. 2019. Answering Complex Questions by Joining Multi-Document Evidence with Quasi Knowledge Graphs. In SIGIR.

[55] Kangqi Luo, Fengli Lin, Xusheng Luo, and Kenny Zhu. 2018. Knowledge Base Question Answering via Encoding of Complex Query Graphs. In EMNLP.

[56] Hao Ma and Yan Ke. 2015. An introduction to entity recommendation and understanding. In WWW.[57] Mausam. 2016. Open information extraction systems and downstream applications. In IJCAI.

[58] Anusri Pampari, Preethi Raghavan, Jennifer Liang, and Jian Peng. 2018. emrQA: A Large Corpus for Question Answering on Electronic Medical Records.In EMNLP.

[59] Boyuan Pan, Hao Li, Ziyu Yao, Deng Cai, and Huan Sun. 2019. Reinforced Dynamic Reasoning for Conversational Question Generation. In ACL.

[60] Panupong Pasupat and Percy Liang. 2015. Compositional Semantic Parsing on Semi-Structured Tables. In ACL.

[61] Yunqi Qiu, Yuanzhuo Wang, Xiaolong Jin, and Kun Zhang. 2020. Stepwise Reasoning for Multi-Relation Question Answering over Knowledge Graph with Weak Supervision. In WSDM.

[62] Filip Radlinski and Nick Craswell. 2017. A theoretical framework for conversational search. In CHIIR.

[63] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. SQuAD: 100,000+ Questions for Machine Comprehension of Text. In EMNLP.

[64] Sudha Rao and Hal Daumé III. 2018. Learning to ask good questions: Ranking clarification questions using neural expected value of perfect information. In ACL.

[65] Deepak Ravichandran and Eduard Hovy. 2002. Learning surface text patterns for a question answering system. In ACL.

[66] Siva Reddy, Danqi Chen, and Christopher Manning. 2019. CoQA: A conversational question answering challenge. TACL 7 (2019).

[67] Marzieh Saeidi, Max Bartolo, Patrick Lewis, Sameer Singh, Tim Rocktäschel, Mike Sheldon, Guillaume Bouchard, and Sebastian Riedel. 2018. Interpretation of Natural Language Rules in Conversational Machine Reading. In EMNLP.

[68] Amrita Saha, Vardaan Pahuja, Mitesh Khapra, Karthik Sankaranarayanan, and Sarath Chandar. 2018. Complex sequential question answering: Towards learn- ing to converse over linked question answer pairs with a knowledge graph. In AAAI.

[69] Denis Savenkov and Eugene Agichtein. 2016. When a knowledge base is not enough: Question answering over knowledge bases with external text data. In SIGIR.

[70] Tao Shen, Xiubo Geng, QIN Tao, Daya Guo, Duyu Tang, Nan Duan, Guodong Long, and Daxin Jiang. 2019. Multi-Task Learning for Conversational Question Answering over a Large-Scale Knowledge Base. In EMNLP-IJCNLP.

[71] Fabian Suchanek, Gjergji Kasneci, and Gerhard Weikum. 2007. YAGO: A core of semantic knowledge. In WWW.

[72] Haitian Sun, Tania Bedrax-Weiss, and William Cohen. 2019. PullNet: Open Domain Question Answering with Iterative Retrieval on Knowledge Bases and Text. In EMNLP-IJCNLP.

[73] Haitian Sun, Bhuwan Dhingra, Manzil Zaheer, Kathryn Mazaitis, Ruslan
Salakhutdinov, and William Cohen. 2018. Open Domain Question Answering Using Early Fusion of Knowledge Bases and Text. In EMNLP.

[74] Huan Sun, Hao Ma, Xiaodong He, Wen-tau Yih, Yu Su, and Xifeng Yan. 2016.
Table cell search for question answering. In WWW.

[75] H. Sun, H. Ma, W. Yih, C. Tsai, J. Liu, and M. Chang. 2015. Open domain question
answering via semantic enrichment. In WWW.

[76] Alona Sydorova, Nina Poerner, and Benjamin Roth. 2019. Interpretable Question
Answering on Knowledge Bases and Text. In ACL.

[77] Alon Talmor and Jonathan Berant. 2018. The Web as a Knowledge-Base for
Answering Complex Questions. In NAACL-HLT.

[78] Alon Talmor and Jonathan Berant. 2019. MultiQA: An empirical investigation
of generalization and transfer in reading comprehension. In ACL.

[79] C. Tan, F. Wei, Q. Zhou, N. Yang, B. Du, W. Lv, and M. Zhou. 2018. Context- Aware Answer Sentence Selection With Hierarchical Gated Recurrent Neural Networks. IEEE/ACM Trans. Audio, Speech & Language Processing 26, 3 (2018).

[80] Christina Unger, Lorenz Bühmann, Jens Lehmann, Axel-Cyrille Ngonga Ngomo, Daniel Gerber, and Philipp Cimiano. 2012. Template-based question answering over RDF data. In WWW.

[81] Svitlana Vakulenko, Javier David Fernandez Garcia, Axel Polleres, Maarten de
Rijke, and Michael Cochez. 2019. Message Passing for Complex Question Answering over Knowledge Graphs. In CIKM.

[82] Ellen M. Voorhees. 1999. The TREC-8 question answering track report. In TREC.

[83] Denny Vrandečić and Markus Krötzsch. 2014. Wikidata: A free collaborative
knowledge base. CACM 57, 10 (2014).

[84] Bingning Wang, Ting Yao, Qi Zhang, Jingfang Xu, Zhixing Tian, Kang Liu, and
Jun Zhao. 2019. Document Gated Reader for Open-Domain Question Answering. In SIGIR.

[85] Zhiyong Wu, Ben Kao, Tien-Hsuan Wu, Pengcheng Yin, and Qun Liu. 2020. PERQ: Predicting, Explaining, and Rectifying Failed Questions in KB-QA Sys- tems. In WSDM.

[86] Wenhan Xiong, Mo Yu, Shiyu Chang, Xiaoxiao Guo, and William Yang Wang. 2019. Improving Question Answering over Incomplete KBs with Knowledge- Aware Reader. In ACL.

[87] Jingjing Xu, Yuechen Wang, Duyu Tang, Nan Duan, Pengcheng Yang, Qi Zeng, Ming Zhou, and Xu Sun. 2019. Asking Clarification Questions in Knowledge- Based Question Answering. In EMNLP-IJCNLP.

[88] Kun Xu, Yuxuan Lai, Yansong Feng, and Zhiguo Wang. 2019. Enhancing Key- Value Memory Neural Networks for Knowledge Based Question Answering. In NAACL-HLT.

[89] Kun Xu, Siva Reddy, Yansong Feng, Songfang Huang, and Dongyan Zhao. 2016. Question Answering on Freebase via Relation Extraction and Textual Evidence. In ACL.

[90] Mohamed Yahya, Klaus Berberich, Shady Elbassuoni, and Gerhard Weikum. 2013. Robust question answering over the web of linked data. In CIKM.

[91] Yunlun Yang, Yu Gong, and Xi Chen. 2018. Query Tracking for E-commerce Conversational Search: A Machine Comprehension Perspective. In CIKM.

[92] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D Manning. 2018. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. In EMNLP.

[93] Scott Wen-tau Yih and Hao Ma. 2016. Question answering with knowledge base, Web and beyond. In NAACL-HLT.

[94] Wen-tau Yih and Hao Ma. 2016. Question answering with knowledge base, Web and beyond. In SIGIR.

[95] Pengcheng Yin, Nan Duan, Ben Kao, Junwei Bao, and Ming Zhou. 2015. Answering questions with complex semantic constraints on open knowledge bases. In
CIKM.

[96] Xinbo Zhang, Lei Zou, and Sen Hu. 2019. An Interactive Mechanism to Improve
Question Answering Systems via Feedback. In CIKM.

[97] Kangyan Zhou, Shrimai Prabhumoye, and Alan W Black. 2018. A Dataset for
Document Grounded Conversations. In EMNLP.

### Citing & Authors

For citing please use the following bibtex

```bibtex
@book{DBLP:series/synthesis/2021Roy,
  author       = {Rishiraj Saha Roy and
                  Avishek Anand},
  title        = {Question Answering for the Curated Web: Tasks and Methods in {QA}
                  over Knowledge Bases and Text Collections},
  series       = {Synthesis Lectures on Information Concepts, Retrieval, and Services},
  publisher    = {Morgan {\&} Claypool Publishers},
  year         = {2021},
  url          = {https://doi.org/10.2200/S0113ED1V01Y202109ICR076},
  doi          = {10.2200/S0113ED1V01Y202109ICR076},
  isbn         = {978-3-031-79511-4},
}

```
