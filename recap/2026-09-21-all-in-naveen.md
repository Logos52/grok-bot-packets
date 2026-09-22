## Recap · All-In · 2026-09-21 · Naveen Rao: 4D Computing, AI's Energy Wall & Beating Biology
url: https://www.youtube.com/watch?v=yAsrMA_ADPc + https://allinchamathjason.libsyn.com/naveen-rao-4d-computing-ais-energy-wall-beating-biology  ·  length: 22:35  ·  text: captions

### Takeaways, arguments, claims (in order)

**Welcome Naveen Rao (00:00)**
- 00:03 · Jason (intro) · Frames Naveen Rao as co-founder/CEO of Unconventional AI (AI chip startup); sold two deep-tech companies; definitional outlier founder.
- 00:47 · Naveen · Anti-doomer: AI among the most transformational technologies humanity has created; will enable the next level of evolution; calls All-In Summit the "anti-doomer conference."
- 01:16 · Naveen · Bio arc: early home computer ~1978; programmed as a kid; electrical engineer via sci-fi / intelligent-machine itch; later PhD in neuroscience to ask how to make computers intelligent — "technologist's dream" now that the world moved that way.
- 02:11 · Naveen · Founded first AI chip company **Nervana Systems** (2014) when AI wasn't common vernacular; hard to convince anyone hardware mattered; sold "way too early" to Intel; started and ran Intel's AI group.
- 02:43 · Naveen · Post-2020: next problem = infrastructure to train bigger LLMs → platformized GPUs at scale (MosaicML path); after ChatGPT (2022) became "best game in town" for people building own models; joined forces with Databricks (2023); claims that biz is ~**¼ of Databricks total revenue** today (with Ali's team).
- 03:23 · Naveen · Unconventional AI = rethink foundations of how a computer works for singular purpose: **power efficiency**. Goal was 1000× power efficiency in 5 years; revised to **~3.5 years** because deep scientific problems solved faster (ironically via AI). Org is top-to-bottom: theorists (math PhDs / theoretical neuroscience) → models trained on real data → physical circuit architects → systems/boards/product.

**Is energy really the problem? (04:45)**
- 04:45 · Naveen · Google publicly: **>3.2 quadrillion tokens/month**. At ~**10 J/token** (lower end of model energy spectrum) → ~**12 GW** for one company's AI services alone.
- 05:20 · Naveen · US puts ~**40 GW** into data centers; US ≈ half of world DC capacity → world under ~**100 GW** DC energy; 12 GW already into one company for AI — bigger models + growing demand → **run out of energy in ~3 years** (his estimate).
- 05:52 · Naveen · Graphic: exponentially growing AI market (~**$1T by 2030**, maybe bigger) vs linearized energy supply — **the gap is the problem**; solve it with technology, not just more power plants.
- 06:15 · Naveen · Data-center bottleneck shifted: floor space → networking → GPUs → **energy first** (get the power contract, then fill it with GPUs).
- 06:40 · Naveen · ~**50% of the cost of serving a token** (e.g. ChatGPT) is energy; rest is hardware/floor-space capex. Business case: monetize every watt **1000× better** than existing hardware.
- 07:08 · Naveen · Biology as proof: human brain ~**20 W**; monkey-scale brain ~**1 W** (≈ phone); rats/bats on milliwatts; **squirrel brain ~8 mW** yet near-perfect branch-jump accuracy — "you could run over 100 squirrel brains on your phone." Biology = right physical substrate for intelligence.
- 08:08 · Naveen · Motto: don't truly understand something until you can create it. Synthetic systems are inefficient mainly because energy goes into **moving information around**.
- 08:28 · Naveen · Human cortex moves ~**16 billion bits/s** across ~13–14B neurons; high-end GPU moves nearly **30 trillion bits/s** in/out of memory (outside chip; inside maybe 10–100× more) — bit-moving drives energy demand.
- 09:03 · Naveen · Computing lineage: mechanical → analog → digital (1930s–40s). 1945 ENIAC operation still similar to today: external memory + compute, shuttle bits — built for **speed** (artillery trajectories faster than human calculators), not energy efficiency. Selling computers = "twice as fast as that other computer," no energy contemplation.
- 10:00 · Naveen · Transistors up, but frequency / single-thread / now **efficiency** stopped scaling; Moore's law (smaller transistors → efficiency) has largely ended → must rethink the problem.

**Cutting out the middleman: abstractions, dynamical systems & a new machine (10:24)**
- 10:24 · Naveen · Intuition: **cut out the middleman**. Stack of lossy abstractions (digital 0/1 over analog transistors → … → neural nets). Brain has neurons but no linear algebra / floating-point — **physics of neurons** gives rise to intelligence; mimic that with semiconductors.
- 11:28 · Naveen · Computation throughout nature: flocking birds, ant colonies — simple local rules → emergent intelligence (**dynamical systems theory**); brain works this way; they build circuits from these ideas.
- 12:07 · Naveen · Metronome demo: many metronomes on a rolling plank synchronize via physics alone (scalable to hundreds) — physical dynamical system; can imagine more complex phase patterns from interconnection.
- 13:07 · Naveen · Can such a system do generative AI? Released open-source simulated model **UNO** — image generation on coupled oscillators; first demo they could scale, train, and get useful image output; state-space trajectories differ by conditioned class (airplane/car/bird).
- 14:13 · Naveen · Further science: **sparsity** — full all-to-all is N² (10→100 links; 1000→1M); throw away connections and you can **rescue** (even improve) behavior and trainability. Works in simulation **and** real physical systems — rare win: more efficient + more scalable + more performance ("holy grail").
- 15:28 · Naveen · **First public reveal**: first physical dynamical computer ever built; company earnest from January (no team yet); taped out **June 1**; chip back in lab with results — first images generated from such hardware.
- 16:09 · Naveen · Not image-only: can do sequence modeling / language models. Energy claim: ~**500 nJ per image** vs GPU-order **mJ** — many orders of magnitude more efficient because it doesn't shuttle information the von Neumann way. Proof positive it works.
- 16:51 · Naveen · Evolution: CPU → GPU → compute-in-memory = still **von Neumann** (memory↔compute shuttle). Their **dynamical computer**: compute and memory unified; each element is memory; no memory interface.
- 17:20 · Naveen · Brands this **4D computing**: time dimension in the dynamics + 3 physical dimensions (planar + die stacking).
- 17:42 · Naveen · Implications of 1000× power efficiency: optimize **intelligence per watt**; thermodynamic limit exists; mammalian brains within ~1–2 orders of that limit; today's silicon ~**10 billion×** away from the limit. In ~3.5 years hit limits of 2D lithography; company goal: **beat biology** — compute everywhere including new robotic forms within ~a decade.
- 18:33 · Naveen · Shift from giant gigawatt data centers → many small local DCs (more environmental / adaptive); enable billions of robots that dynamically assemble to solve problems.
- 19:03 · Naveen · If AI is a $1T market and you disrupt cost 1000×, **Jevons paradox**: cheaper → consume more than the price drop; 1000× cheaper → consume more than 1000× → "largest market humanity's ever seen."

**Chamath joins: path to product, porting, team (19:40)**
- 19:34 · Chamath · Reaction: "extremely unexpected… pretty amazing." Asks path from early chip → hand/product given need for fabs/packagers ecosystem (Jensen earlier).
- 20:09 · Naveen · Full product within **~2 years**. Product = new **data-center rack/system** (not a phone VM): tokens in / tokens out over network cable; inner guts completely different.
- 20:32 · Chamath · Will existing model families / KV-cache abstraction world port? How do the rest of us take the efficiency curve?
- 20:56 · Naveen · Sliding scale: how much better vs how much pain to move; aim to make move compelling. Port at the **model layer**, not ops layer — existing models will work, but fair bit of compute to transition.
- 21:19 · Chamath · Does matmul exist on this machine?
- 21:26 · Naveen · Can characterize as matmul analytically, but does **not** implement as matmul — implements as **time-varying behavior**; each timestep analyzable as current-state matrix × transition matrix.
- 21:38 · Chamath · Who is the team — biologists + physicists?
- 21:45 · Naveen · Theorists from dynamical-systems world (century-old field) + chip builders who **don't talk to each other** — facilitating that span is one of the hardest parts of the company.
- 22:06 · Chamath · CUDA-like bridge between theorists and chip people?
- 22:13 · Naveen · Built Python libraries (not CUDA) — a language to express time-varying elements with **stochastic** behavior.
- 22:26 · Chamath · Closes: incredibly impressive / ambitious; thanks.

### Quotes (verbatim, ≤ 25 words each, 3–6)
- 00:58 Naveen: "I'm the opposite of a doomer. I think AI is one of the most transformational"
- 06:56 Naveen: "I get a power contract I need to monetize every watt"
- 08:08 Naveen: "I don't feel like we truly understand something until we can create it."
- 15:36 Naveen: "This is actually the first physical dynamical computer ever built."
- 17:49 Naveen: "So intelligence per watt is what we care about."
- 18:20 Naveen: "the overarching goal of this company is to beat biology."

### One paragraph
All-In Summit talk by Unconventional AI CEO Naveen Rao (Nervana→Intel AI, then MosaicML→Databricks): AI will hit an **energy wall** in ~3 years — Google alone at 3.2Q tokens/mo × ~10 J/token ≈ 12 GW, while world DC power is under ~100 GW, and ~50% of token cost is already energy — so the gap vs a ~$1T-by-2030 market must be closed with **1000× more efficient hardware**, not just more power contracts. Thesis: von Neumann machines waste energy shuttling bits (GPU ~30T bits/s vs cortex ~16B); biology (20 W brain; 8 mW squirrel) proves a better substrate. Solution: cut lossy abstractions and build a **dynamical / 4D computer** (oscillator physics + sparsity + die stacking + time) — first physical prototype taped out June 1 after a Jan start, generating images at ~500 nJ vs mJ-class GPUs; open UNO demo preceded it. Goal in ~3.5 years: approach 2D-lithography limits and eventually **beat biology** on intelligence-per-watt, enabling many small local DCs and robot swarms (Jevons: 1000× cheaper compute → largest market ever). Chamath Q&A: ~2-year path to a tokens-in/out data-center rack; port at model layer (not ops); no native matmul — time-varying dynamics; team = dynamical-systems theorists + chip people bridged by Python libs.

### Footer
canary: published 2026-09-21T21:03:00Z (libsyn RSS) / YT uploadDate 20260921 · fetched 2026-09-22T04:08:00Z · length 22:35 (1355s) · captions English auto via yt-dlp --write-auto-sub --sub-lang en --convert-subs srt → /workspace/recap/tmp-0922-naveen/yAsrMA_ADPc.en.srt · chapters from YT description used as section anchors · ASR name cleanup in body only (Ralph→Rao, Nirvana→Nervana, jewels→joules, gawatt→gigawatt, Chat GBT→ChatGPT, data bricks→Databricks, Alli→Ali, millowatts→milliwatts, vonoyman→von Neumann, Jieven's→Jevons, maple/mapm→matmul, stoastic→stochastic, goomer→doomer in intro clip) · quotes from caption text · no ASR on box · no third-party transcript sites
