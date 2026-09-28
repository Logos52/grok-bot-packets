---
id: 2026-09-26-travis-beals-behind-project-suncatcher-our-moonshot-to
kind: article
title: Behind Project Suncatcher, our moonshot to put AI in space
source: "https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/"
author: Travis Beals
published: 2026-09-24
captured: 2026-09-26
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

Behind Project Suncatcher, our moonshot to put AI in space
Sep 24, 2026
Travis Beals, Senior Director, Paradigms of Intelligence

Project Suncatcher explores if space can host scalable machine learning infrastructure for future AI. A prototype satellite will test how Google’s AI chips perform in harsh space conditions. Engineers are tackling major challenges like extreme radiation, intense vibrations, and cooling in vacuums. Future missions aim to link satellite clusters using high-bandwidth lasers for massive AI workloads. This initial launch helps the team learn what works before scaling up by 2027.

After years of research, Project Suncatcher is scheduled to embark on its first test in orbit, launching a prototype satellite to evaluate how Google Tensor Processing Units (TPUs) perform in space.

Announced last year, Project Suncatcher is a long-term, research moonshot exploring whether space could one day host scalable machine learning infrastructure. In low Earth orbit, satellites can access near-constant sunlight, generating up to eight times more solar power than on Earth. Eventually, it could be possible to link together multiple constellations of satellites, allowing them to manage larger AI workloads while in orbit.

Turning that idea into reality starts with a basic question: Can our AI hardware operate in space? This initial mission onboard the upcoming Transporter-18 rideshare mission with SpaceX was developed in partnership with Planet. It’s designed to gather in-orbit data on how our TPUs handle the physical stress of spaceflight and the radiation and thermal extremes of space.

Hardware survival: A rocket trip into low Earth orbit lasts about 10 minutes, during which the spacecraft experiences intense vibration and sustained acceleration loads up to 10 g. Individual components such as TPU chips can experience forces up to 50 to 100 g. Vibration testing on all three axes surprised the team by holding up. Radiation testing at UC Davis Crocker Nuclear Laboratory proton beam facility while running AI workloads showed Trillium TPUs can survive a radiation total ionizing dose greater than a five-year space mission. Putting first TPUs in orbit next week will help get data for future launches.

Cooling in space: TPUs generate large heat in small area; in vacuum heat must diffuse via radiators. Approaches include heat pipes and radiators tested in thermal vacuum chamber.

Satellite interconnectivity: Future satellites will each carry dozens of TPU chips in clusters, communicating via lasers at very high bandwidth over short distances. Precision similar to hitting a coin-size target from miles away while both points are in motion. Test in 2027 with two satellites in orbit.

Just the beginning: This first launch is about seeing what works, identifying points of failure, and applying findings to future missions.
