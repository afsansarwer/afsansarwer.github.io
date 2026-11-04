---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 1
description: Bacterial genomes, mobile resistance genes, and microbiology in Bangladesh.
---

<link rel="stylesheet" href="{{ '/assets/css/academic.css' | relative_url }}">

<p class="academic-lead">How do bacteria acquire resistance, and what can their genomes tell us about its movement across animals, food, and the environment?</p>

My veterinary background shapes the questions I ask. I work with phenotypic and molecular results alongside bacterial genomes, with particular interests in plasmids, mobile genetic elements, and the interpretation of genomic relationships.

<nav class="academic-jump-links" aria-label="Research sections">
  <a href="#seafood">Seafood genomics</a>
  <a href="#thesis">Equine thesis</a>
  <a href="#vegetables">Vegetable isolates</a>
  <a href="#software">Software</a>
  <a href="#methods">Methods &amp; skills</a>
</nav>

<section class="academic-section" id="seafood" markdown="1">

<p class="academic-eyebrow">Published research · Second author</p>

## Genomic relationships of seafood-derived _E. coli_

We compared ten ESBL-producing _Escherichia coli_ isolates from seafood in Bangladesh with global genomes to examine population structure, resistance, virulence, and genomic relationships.

My contribution included comparative genome analysis and building a core-genome SNP phylogeny from hundreds of publicly available genomes. This work gave me experience in dataset preparation, Linux workflows, resistance and plasmid profiling, and interpreting phylogenetic patterns in their sampling context.

Fahim, Sarwer, et al. · _Frontiers in Microbiology_ · 2026. [Read the publication](https://doi.org/10.3389/fmicb.2026.1737712)

</section>

<section class="academic-section" id="thesis" markdown="1">

<p class="academic-eyebrow">MS thesis · Ongoing research</p>

## Bacteria from horses and their environments

My thesis is titled “Molecular and Phenotypic Characterization of _Staphylococcus aureus_, _Enterococcus faecalis_, and _Rhodococcus equi_ from Horses and Associated Environments in Bangladesh.”

I collected horse and environmental samples, cultured bacteria, performed PCR-based detection, and assessed antimicrobial susceptibility and biofilm formation. I am also examining _E. faecalis_ genomes for resistance determinants, plasmid associations, and mobile genetic elements.

This work asks how phenotypic resistance relates to molecular findings and how bacterial characteristics differ among sample sources. It connects field sampling and laboratory microbiology with genomic interpretation.

Supervised by Prof. Dr. Md. Tanvir Rahman and co-supervised by Prof. Dr. Mahbubul Pratik Siddique, Bangladesh Agricultural University.

</section>

<section class="academic-section" id="vegetables" markdown="1">

<p class="academic-eyebrow">Ongoing research · Conference poster presented</p>

## Plasmids and resistance in vegetable-derived _E. coli_

I am comparing five vegetable-derived _E. coli_ isolates from Dhaka with publicly available genomes from Bangladesh. The analysis examines accessory gene content, population relationships, and plasmids carrying antimicrobial resistance genes.

My work includes pangenome analysis, plasmid profiling, and comparison of resistance gene contexts. I want to understand whether similar resistance determinants occur in related bacterial lineages or across different genomic backgrounds.

I presented this work at BSVER ASCon XXXIV in 2026. [Conference details]({{ '/publications/#conferences' | relative_url }})

</section>

<section class="academic-section" id="software" markdown="1">

<p class="academic-eyebrow">Workflow development · Public beta</p>

## ChromoPlas

I developed ChromoPlas to bring bacterial genome screening and contig-level gene localization into one Python workflow. It combines ABRicate screening with MOB-suite predictions and produces genome maps, gene localization summaries, and HTML/TSV reports.

The workflow records the original contig coordinates and retains unresolved classifications. It is a research prototype in public beta, with its current testing and biological validation scope documented in the repository.

[Source code, installation, and validation notes](https://github.com/afsansarwer/ChromoPlas)

</section>

<section class="academic-section" markdown="1">

<p class="academic-eyebrow">Independent project · August–December 2024</p>

## Microscopy and machine learning

With advice from Dr. A K M Anisur Rahman, I developed a YOLOv8 prototype to detect livestock parasite eggs and cysts in microscopy images. I worked on image annotation, model training in Google Colab, and evaluation using precision, recall, F1-score, and mean average precision.

I presented the exploratory work at the 23rd Science Council of Asia Conference in Dhaka in 2024. It introduced me to evaluating computational methods on biological image data.

</section>

<section class="academic-section" id="methods" markdown="1">

<p class="academic-eyebrow">Practical experience</p>

## Methods & skills

| Area                   | Experience                                                                                                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microbiology           | Sample collection and processing, bacterial culture and isolation, phenotypic characterization, antimicrobial susceptibility testing, and Congo red agar biofilm assessment |
| Molecular methods      | DNA extraction, PCR-based bacterial identification and gene detection, and gel interpretation                                                                               |
| Genome analysis        | Read quality control, assembly, assembly assessment, annotation, AMR and virulence gene screening, MLST, and plasmid profiling                                              |
| Comparative genomics   | Pangenome analysis, SNP phylogeny, genomic visualization, and interpretation of mobile genetic elements                                                                     |
| Computing              | Bash/Linux workflows, environment management, troubleshooting, and Python for processing tabular outputs and making figures. Basic R for data exploration and visualization |
| Research communication | Data validation, figure preparation, poster presentations, and manuscript contributions                                                                                     |

Tools I have used include FastQC, Trimmomatic, SPAdes, QUAST, Prokka, ABRicate, MOB-suite, PanACoTA, Parsnp, and iTOL. I choose methods according to the biological question and the available data.

</section>
