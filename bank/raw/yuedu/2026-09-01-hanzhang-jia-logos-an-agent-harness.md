---
id: 2026-09-01-hanzhang-jia-logos-an-agent-harness
kind: paper
title: "Logos: An Agent Harness on a Cross-Process Bus"
source: "https://arxiv.org/abs/2608.28553"
author: Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, and Bo Ma
published: 2026-08-28
captured: 2026-09-01
via: grok-bot/多恩刊
lane: yuedu
status: raw
private: false
---

                                         Research Paper Track                                                                                               AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


                                                                Logos: An Agent Harness on a Cross-Process Bus
                                                                          Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, and Bo Ma
                                                                                                    University of Sussex
                                                                                                Brighton, United Kingdom
                                                                                              Zhejiang Gongshang University
                                                                                                     Hangzhou, China
                                                                                     Shanghai Shuyuan Information Technology Co., Ltd.
                                                                                                      Shanghai, China
                                                                                                    hj303@sussex.ac.uk
                                         Abstract                                                                              calculus [7]. In that calculus, a capability is a component carrying
arXiv:2608.28553v1 [cs.AI] 28 Aug 2026




                                         Modern agent systems assemble capabilities at runtime, and this                       a tracked inverse, assembly applies an effect, removal applies the
                                         dynamic composition has recently received a complete formal treat-                    recorded inverse, and an agent is assembled from such components
                                         ment in the spatiotemporal-composability calculus, in which a ca-                     as plugins, with every record of assembly and removal kept in one
                                         pability is a component carrying a tracked inverse, and agents are                    shared context. The calculus proves a reversibility guarantee, and
                                         assembled as plugins. This plugin form is carried by a single pro-                    the guarantee is complete within a single-process implementation.
                                         cess sharing one context, a carrier that places all components in                     However, that one process carries all plugins, all records, and all
                                         one physical failure domain, a fault suspends every component at                      sessions, so the process is a single point of failure for everything
                                         once, and process death interrupts every session the process hosts.                   it hosts.
                                         This paper shows that neither the modeling nor the calculus binds                         Hosting all plugins in one process incurs four engineering costs.
                                         an agent to one process, the statelessness of the language model                      A physical fault in the hosting process, a crash, memory exhaus-
                                         keeps all cross-step state outside the model, and the soundness                       tion, or a blocked event loop, terminates all components at once,
                                         invariant is defined on the state space alone. These observations                     the withdrawal of one service unloads its dependents and renders
                                         condense into four lemmas whose premises are the hypotheses                           the tools they provide unavailable to the model until reload, so
                                         of the calculus and the statelessness of language-model inference.                    the isolation that holds between components in the mathematics
                                         On these lemmas this paper constructs Logos, a ROS-like cross-                        loses its meaning inside a shared process. The death of the pro-
                                         process agent harness in which a plugin is a process and the only                     cess terminates every component and every co-resident session
                                         shared state is an append-only transcript. Eighty sessions resume                     at once, and recovery restarts the whole stack. Replacing or up-
                                         with no repeated effect after kills placed at the four boundaries                     grading one plugin requires a process restart or a reload that tears
                                         of the tool-call cycle, and a same-fault comparison with a single-                    down and re-runs every dependent, and every co-resident session
                                         process reference configuration shows one fault interrupting every                    halts with the restart. The process is also a single-language envi-
                                         co-resident session while under the peer-process construction one                     ronment, in which plugins are confined to the host language and
                                         fault ends at one node.                                                               cross-language reuse goes through translation layers and remote
                                                                                                                               calls. Together, these four costs point to plugin composition across
                                         Keywords                                                                              processes.
                                                                                                                                   For these problems, this paper presents four lemmas. Lemma
                                         LLM agents, agent infrastructure, distributed systems, hot swap-
                                                                                                                               1, orchestration externality, asserts that each forward pass of the
                                         ping, fault tolerance, composability
                                                                                                                               model is a stateless pure map, that cross-step state already lives
                                         ACM Reference Format:                                                                 outside the model, and that the input can be synthesized anywhere.
                                         Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, and Bo Ma. 2027. Logos:                 On this basis, Lemma 2, carrier substitution, allows state to move to
                                         An Agent Harness on a Cross-Process Bus. In Proc. of the 26th International           any persistent carrier, and recovery rebuilt from the carrier equals
                                         Conference on Autonomous Agents and Multiagent Systems (AAMAS 2027),                  in-place recovery under observational equivalence. Lemma 3, re-
                                         Hanoi, Vietnam, 3–7 May 2027, IFAAMAS, 10 pages.
                                                                                                                               covery localization, draws on the calculus’s assumption of compo-
                                                                                                                               nent independence and asserts that the recovery of each compo-
                                         1 Introduction                                                                        nent needs no coordination with any other. Finally, Lemma 4, ex-
                                         Modern agent systems assemble capabilities at runtime, loading                        ternal resolution, moves dependency resolution out of the process
                                         and unloading components with their effects fully reverted, and                       as well, into a table keyed by capability name. The four lemmas rest
                                         this dynamic composition of software components has recently re-                      on nothing beyond the assumptions the calculus already states and
                                         ceived a complete formal treatment in the spatiotemporal-composability the fact that language-model inference is stateless, adding no new
                                                                                                                               mathematical hypotheses. It follows that spatiotemporal compos-
                                                           This work is licensed under a Creative Commons Attribution Inter-   ability holds across processes. Considering the design freedom of
                                                           national 4.0 License.
                                                                                                                               complex systems and the plugin form, this paper therefore selects
                                         Proc. of the 26th International Conference on Autonomous Agents and Multiagent Sys-   the ROS architecture [6] as its basis and constructs Logos, a dis-
                                         tems (AAMAS 2027), M. Baldoni, F. Fang, W. Yeoh, N. Yorke-Smith (eds.), 3–7 May 2027, tributed plugin-based system. The system runs as a set of peer pro-
                                         Hanoi, Vietnam. © 2027 International Foundation for Autonomous Agents and Multi-
                                         agent Systems (www.ifaamas.org).                                                      cesses on a bus. A harness runs the loop of input synthesis, model
Research Paper Track                                                                                    AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


calls, and output settlement over one session. A tool provides a         Table 1: What each framework moves out of the process, and
capability. The router registers nodes and forwards messages by          what stays in it.
recipient. A node is any process that conforms to the protocol, and
anything the rules admit mounts as a peer. In Logos a plugin is a         Framework        Moves out of the process    Stays in the process
process, the router holds only its routing table, and all shared state
                                                                          MCP and its      tool servers and calls    composition and session
lives in an append-only transcript owned by no process. The tran-
                                                                          derivatives                                state
script records every step of a session as it happens, and after any
                                                                          Temporal         execution                 assembly and the work-
process dies, a new process rebuilds the session from the transcript
                                                                          and its peers                              flow definition
and continues, a form of recovery called cold switching. Logos it-
                                                                          AutoGen and      nothing                   all capabilities as in-
self also removes the language cost, with a Go router, Python har-
                                                                          LangGraph                                  process objects
nesses and tools, and Node.js tools running as peers on the same
                                                                          Logos            composition and assem- nothing but the routing
bus.
                                                                                           bly, state into the tran- table
   Runtime verification shows that Logos passes messages without
                                                                                           script
loss, duplication, or reordering, keeps one registrar per capability
name, and delivers supply-change notifications in order, establish-
ing the engineering feasibility of the distributed architecture, and a
stress audit exercises each condition directly, with 3,500 calls from           autonomous adoption of tools introduced during a task, and
as many as two hundred concurrent callers pair with no loss, du-                mixed-language operation on one bus, measured in Section 6.
plication, or misattribution, one registration wins among one hun-
dred simultaneous claims of the same name with ninety-nine ex-           2 Related Work
plicit denials, and two observers record identical supply-change         In-process agent frameworks make the capability a library object
sequences across thirty rounds of churn among fifty providers. In        inside the host that imports it. AutoGen organizes capabilities through
concurrent multi-agent scenarios, routing restores automatically         conversation programming [9], and LangGraph organizes them
after the router is killed, and the tasks of the harnesses complete      through state graphs [3], both as in-process objects. Logos, in con-
as usual. Twelve end-to-end sessions undergo six process kills, all      trast, gives each capability its own operating-system process and
resume through cold switching, and no previously executed action         places composition on the bus.
is repeated after recovery. Eighty further sessions extend the cov-         Existing distributed architectures move actions across processes.
erage to four kill points of the tool-call cycle, during tool execu-     MCP and its derivatives move tool servers out of the process, with
tion, after return but before persistence, after persistence but be-     calls crossing processes while composition remains in the host,
fore announcement, and after announcement. All eighty resume             which holds session state [2]. Temporal and its peers move execu-
and complete with no repeated effect, and the work redone after re-      tion out of the process, with assembly remaining in the workflow
covery equals exactly the work the transcript had not yet recorded.      definition and recovery delivered through history replay [8]. Ta-
A tool comes online during a task, and the model makes its first au-     ble 1 lines up the four frameworks by what each moves out of the
tonomous call 8.4 s after the registry-update broadcast. The median      process and what stays in it.
cost of a bus hop is 0.215 ms, 1/823 of the model’s 177 ms first-token      The architectural lineage is the robot operating system, whose
latency, invisible at the model’s time scale.                            peer-to-peer processes and name-based routing this construction
   Existing distributed architectures move actions across processes,     inherits [6]. The spatiotemporal-composability calculus takes plu-
MCP and its derivatives move tool servers out of the process, and        gin assembly as its subject and proves a reversibility guarantee in
Temporal and its peers move execution out of the process, while          a single-process reference [7]. This work takes that treatment as its
composition and assembly remain in the host [2, 8]. Logos moves          starting point and extends it to a multi-process carrier with suffi-
composition and assembly themselves out of the process, carried          cient conditions, a construction, and measurements. Two parallel
by registration and broadcast among peer nodes.                          preprints study adjacent questions of agent state and history [4,
   In summary, this paper makes three contributions.                     5]. Neither examines cross-process reversibility. Within the frame-
                                                                         works surveyed, composition and assembly stay in the host pro-
                                                                         cess, and this work moves them onto a bus shared by peer nodes.
     • The sufficient conditions, Theorem 1, under which the re-
       versibility guarantee of the spatiotemporal-composability cal-    3 Preliminaries
       culus holds across processes, with the four supporting lem-       The notation fixes a context Γ, an effect context 𝜕Γ made of the
       mas, with premises drawn from the calculus itself and the         state 𝛾 and the accumulated inverse composite 𝜑 , the two transfor-
       statelessness of language-model inference, stated in Section 4.   mations track and recover, the transformation monoid 𝔐(𝑓 ), ob-
     • The minimal construction of Logos, a cross-process agent          servational equivalence ≃, the macrostate projection Π, and com-
       harness built on the ROS architecture, in which a plugin is       positions reading from right to left. Theorem numbers follow the
       a process and the only shared state is an append-only tran-       calculus, and notations introduced in Section 4 are defined at their
       script, constructed in Section 5.                                 first occurrence.
     • Adversarial and end-to-end evaluation of the fully imple-
       mented system, covering concurrent recovery under router            Definition 3.1 (Component). A component is an effect function
       failure, cold-switch resumption after process termination,        on the context, a map 𝑓 that takes a state 𝛾 to a pair of a new state
Research Paper Track                                                                                         AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


𝛿 and an inverse map 𝑔 , where the inverse returns the state it was        4 Sufficient Conditions
chosen at, 𝑔(𝛿) = 𝛾 , and is unconstrained everywhere else.
                                                                           4.1 From One Process to an Assignment
   A single 𝑔 with                                                         The formal model of the calculus shares one context Γ∞ , the re-
                            𝑔 ∘ 𝑓 = id                          (1)        cursive context type of the calculus, among all plugins, all records
meets the constraint at every state at once and induces an element         of assembly and removal, and all sessions it hosts. The soundness
of the witnessed form, and the calculus proves the induction a ho-         invariant of Definition 4 carries no carrier, it is a property of the
momorphism.                                                                state space alone. The records of assembly and removal lack this
   Definition 3.2 (Assembly and removal). Assembly and removal             freedom, they reside in the shared context, and the shared context
are the two transformations track and recover, where track applies         resides in the process that hosts it. The calculus states no theorem
an effect and extends a running composite of inverses, and recover         for more than one process, and its sole treatment of the process
applies that composite to the current state and resets it, so that         boundary is an application note, in which the service broker spans
removal reverses every applied assembly in the reverse order of            processes and calls obey an asynchronous contract. The implemen-
application.                                                               tation of the calculus hosts the shared context in a single process.
                                                                               This paper therefore relaxes the co-residence restriction, the con-
   What each tracking step preserves is the result of recovery itself,
                                                                           finement of components and records to one process, to an arbi-
from whatever state it is taken.
                                                                           trary assignment of components and records to processes, and the
   Definition 3.3 (Independence). Two effect functions are indepen-        soundness invariant imposes no constraint on the assignment. Un-
dent when every transformation of one commutes with every trans-           der an assignment, an abstract trace is a sequence of assembly and
formation of the other, and neither one’s transformations disturb          removal steps in the state space, and an implemented trace is the
the inverse the other yields.                                              sequence of steps the processes actually perform. An assignment
   The global theorems of the calculus assume pairwise indepen-            is faithful when for every abstract trace 𝜏 there is an implemented
dence, and coeffect operations on disjoint keys commute uncondi-           trace 𝜏 ′ such that the two agree pointwise under Π,
tionally.                                                                                               Π(𝜏 ′ ) = Π(𝜏 ).                           (3)
    Definition 3.4 (Soundness invariant). The soundness invariant states
that for every effect pair with 𝑔(𝑓 (𝛾 )) = 𝛾 , recovering after track-    4.2    Two Modeling Facts
ing returns what recovering before tracking would have returned,           The first modeling fact is that a forward pass of the language model
that is, the value                                                         is a stateless pure map, all cross-step state already resides outside
                            𝐼 (𝛾 , 𝜑) = 𝜑(𝛾 )                       (2)    the model, and the input can be synthesized anywhere. The second
is unchanged along every witnessed track step, and recover reads           modeling fact is the minimal model 𝑦 = 𝑓 (𝑥), input synthesis and
it out.                                                                    output parsing are operations outside 𝑓 , and a multi-turn session is
                                                                           nested passes of 𝑓 with synthesis and parsing as the outer routing.
   The invariant is a property of the state space alone, its definition    Together the two facts make a session a sequence of stateless maps
refers to the context and to composition of maps and to no process,        over an external sector, and co-residence a choice.
no memory, and no closure.
   Definition 3.5 (Observational equivalence and macrostate). Ob-          4.3    Four Lemmas
servational equivalence ≃ relates two states when no observer of              Lemma 4.1 (ORchestRation exteRnality). If the model is a
the context can distinguish them, and the macrostate of 𝛾 is its           stateless pure map and synthesis and parsing are outside it, then all
equivalence class under the projection Π.                                  cross-step state resides in a shared sector 𝑆 , the store the runtime reads
  The physical equality of recovery is an idealization, because the        and writes, outside any model call, the runtime’s entire role is the
physical state cannot be recovered as it stood, and every recovery         two operations of input synthesis 𝜔 and output settlement 𝜌 , and the
equality holds up to ≃.                                                    model becomes an ordinary dispatchable node.
   Definition 3.6 (Registry). A registry 𝐹𝛾 carries each fiber under           Cross-step state cannot live inside a stateless map, and synthesis
its name and is well formed when parent pointers form one tree             and parsing are defined as external operations, so the shared sector
rooted at a common root, the provides sets of distinct fibers are          is the only remaining residence, and the sector being readable from
disjoint, and a committed view resolves a demand key to at most            anywhere, the input 𝑥 = 𝜔(𝑆) is the system state made inputtable
one installed provider.                                                    and can be synthesized at any process.
   Preservation of this form is a theorem of the calculus, every rule         Lemma 4.2 (CaRRieR substitution). Let 𝒟 be the inverse data
step carries a well-formed registry to a well-formed one.                  of a history with anchors 𝑎𝑖 and inverses 𝑔𝑖 . A persistent store 𝒞 with
   Definition 3.7 (The outside). An operation is outside the bound-        a readout map 𝜌 is a faithful carrier when 𝜌(𝑎𝑖 ) ≃ 𝑔𝑖 holds at every
ary when the system can neither exclusively modify nor recover             anchor, and the accumulator rebuilt from the carrier by composition
its state, an outside operation acts as the identity on the context        in application order is ≃-equal to the original, so recovery through
and is neither tracked nor recovered, and emission, the crossing           the carrier equals in-place recovery under Π.
form, has withholding and compensation as its only routes.                   The inverse data form a monoid, a composite of maps that re-
   Compensation holds at a coarser equivalence.                            spect ≃ respects ≃, pointwise equality of readouts composes to
Research Paper Track                                                                                          AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


equality along the chain, and recover merely evaluates the invari-            Table 2: The four lemmas against the parts of the construc-
ant. Reversibility leaves a record, a persistent carrier is the physical      tion that satisfy them.
lower bound of the reversible, and process memory under a de-
ployment that tolerates process death satisfies the premise for no             Lemma                           Satisfied by
process. The most general persistent carrier of a monoid element is
                                                                               1, orchestration externality    the model as an ordinary dispatch-
the free monoid on its generators, an append-only transcript, and
                                                                                                               able node on the bus
a new process that imports the transcript rebuilds the external ac-
                                                                               2, carrier substitution         the append-only transcript and
cumulator and composes it with what the failed process had kept.
                                                                                                               cold switching
   Lemma 4.3 (RecoveRy localization). Let the effect functions                 3, recovery localization        capabilities as independent pro-
of components 𝑐1 through 𝑐𝑀 be pairwise independent in the sense                                               cesses, recovery data per process
of Definition 3, and let an arbitrary partition place them into 𝑁 pro-         4, external resolution          the router holding only the rout-
cesses. The inverse data of a component then need reside only in its                                           ing table, registration as a revert-
own process, global recovery is any global interleaving of the per-                                            ible effect
process recoveries, and no ordering constraint and no shared state
exists between processes for the sake of recovery.
                                                                              4 to move resolution to the routing table, and the pointwise agree-
   Any interleaving of the local last-in-first-out sequences is a per-
                                                                              ment under Π follows. The full induction appears in the appen-
mutation of all the inverses, recovery is invariant under permuta-
                                                                              dix.                                                             □
tion of the applied inverses, so the endpoint is the same whichever
interleaving runs. The shared mutable state of this system is entry              Under the idealized model, the theorem admits a distributed im-
tables whose operations are appends and deletions, which fall in-             plementation. The practical construction is subject to three con-
side the domain the commutative keys satisfy, and the discharge               straints, E1 every response is paired with its own call, E2 each
mechanism of the calculus is the basis. Shared databases and quota            name carries exactly one registration and a conflicting claim re-
resources pass through single-writer tools or stay outside the bound-         ceives an explicit refusal, and E3 every observer receives the same
ary.                                                                          sequence of supply-change notifications. The single-registration
    Lemma 4.4 (ExteRnal Resolution). The operating requirements               constraint is the single-writer clause of the theorem enforced at
of spatial composability are the real-time resolution of keys to providers,   registration, and the common order of notifications is the supply
a single writer per key, and supply before demand with withdrawal             order of Definition 6 carried by the broadcast. A deployment as a
after consumption, and their content is entirely an assignment of keys        set of peer processes is admissible once the bus time scale separates
to providers, that is, a routing table.                                       from the model time scale, a millisecond hop against a first token
                                                                              a hundred times slower, the topology stationary at the step scale
   The routing table is the representative case of a commutative              of the model.
key in the calculus, registration is a revertible effect, so the table           Table 2 lists the four lemmas against the parts of the construc-
resides in the commutative part of the state space and a copy main-           tion that satisfy them.
tained by broadcast of registration events is observationally equiv-
alent to an in-memory registry.                                               5 The Logos Construction
                                                                              This construction moves composition and assembly out of the host
4.4     The Theorem                                                           process. A bus takes the place of the host. The routing table belongs
   TheoRem 4.5. An implementation over 𝑁 processes is a faithful              to the bus. The transcript and the event stream belong to no pro-
implementation of the calculus and the two modeling facts when ev-            cess. A plugin is a process. A message follows the full path, the har-
ery effect that must be reversible writes its anchor to a persistent          ness synthesizes input from the transcript, the model answers, the
transcript at the step of occurrence, and every key admits one writer,        router forwards the tool call, the result settles into the transcript,
enforced at registration.                                                     and the broadcast carries the change to every node. Figure 1 shows
                                                                              the construction.
    Under the two conditions, Lemma 1 places the state in the shared
sector and Lemma 2 makes the transcript a faithful carrier. Lemma
3 confines each component’s recovery data to its own process and
                                                                              5.1    The Bus
Lemma 4 moves resolution to the routing table, and an induction               The router is a single Go process that registers nodes and forwards
over the abstract trace yields an implemented trace agreeing with             messages by recipient. Its three duties are registration, forwarding,
it pointwise under Π.                                                         and broadcast, a node registers under an id with a role and a list of
                                                                              provided capabilities, a call is forwarded to the node whose capabil-
   PRoof sKetch. The base case holds, the empty abstract trace is             ity matches, and an event is delivered to every registered node. The
implemented by the empty trace. Each assembly step uses Lemma                 router holds only its routing table, it schedules nothing and it reads
1 to place the state in the shared sector and Lemma 2 to make the             no payload. A message names its recipient, an id for a direct deliv-
transcript prefix the anchor record, and the pointwise agreement              ery, the wildcard for a broadcast, and a missing recipient returns an
under Π holds after the settlement is recorded. Each removal step             explicit error to the sender. The wire protocol is NDJSON over TCP,
uses Lemma 3 to confine recovery to the component and Lemma                   one object per line, frames up to 64 MB, malformed lines skipped,
Research Paper Track                                                                                       AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


                                                                           Algorithm 1 Harness loop with recovery
                                                                           Require: session id, transcript
                                                                            1: import the transcript, rebuild the projection
                                                                            2: loop
                                                                            3:   synthesize input from the projection
                                                                            4:   call the model, stream the answer into the transcript
                                                                            5:   if the model asks for a tool then
                                                                            6:      route the call, append the result to the transcript
                                                                            7:   end if
                                                                            8:   settle outputs, broadcast the change
                                                                            9:   {on process death, resume from the first line}
                                                                           10: end loop



                                                                           free monoid on the generators of the inverse data, the mathemati-
Figure 1: The Logos construction, peer processes on a bus, the             cal carrier of Lemma 2. The replay of a transcript is checked against
router holding only its routing table, harnesses and tools as              four invariants, I1 entries follow a well-formed order, I2 identifiers
nodes, and the append-only transcript outside any process.                 are monotone, I3 every tool use has exactly one result, and I4 the
                                                                           rebuilt projection equals the messages the session showed. The set-
                                                                           tlement order is durable before visible, an effect is appended to the
and lossy streams are separated from control messages, which are           transcript before it is announced on the bus.
paired and never dropped. Each connection holds a bounded out-
bound queue of 1024 entries with its own writer coroutine, a write         5.4    The Event Stream
timeout of five seconds disconnects the peer, a full queue drops           An observer node records every broadcast into an append-only
the oldest entry of a lossy stream and counts the drop in a notice,        file, the event stream. The stream covers system behavior, the tran-
and a full queue of control messages disconnects the peer. Delivery        script covers the session, and the two stay separate. The same re-
is layered, control messages arrive at least once with idempotent          play checks apply to both.
pairing by global call ids, and a lossy stream loses at most a pre-
fix, the surviving sequence stays contiguous. A disconnected node          5.5    Nodes
re-registers, and the replay fills the gap. Every registration and ev-     A node is any process that conforms to the protocol, and anything
ery refusal returns a receipt to its sender, and a refused duplicate       the rules admit mounts as a peer. A harness runs the loop of in-
name carries an explicit denial. The bus imposes no language, a            put synthesis, model calls, and output settlement over one session,
tool is any process that implements the protocol, and Go, Python,          and a tool provides a capability. A node registers with one of three
and Node.js processes run as peers on one bus in this system. The          roles, harness, tool, or observer, and the observer receives every
bus meets the three constraints by construction, pairing by global         broadcast and announces nothing. Every process holds the same
call ids, single registration by explicit refusal, and one order by se-    handle, and the roles differ only in the register call. Harnesses and
rialized broadcast.                                                        tools count equally as residents, and the router exits when no res-
                                                                           ident remains. Algorithm 1 gives the loop.
5.2     The Routing Table
The routing table maps a name to a connection, together with the           5.6    Assembly, Removal, and Recovery
role and the provided capabilities. Any node can read the whole            A capability is a process, tools mount at their own endpoints with
table at any time, registered or not. Registration adds a row, de-         the router unchanged. Mounting with a missing provider leaves
parture deletes it, and the online and offline broadcasts carry the        the component in waiting, its calls answered by an explicit refusal
change to every node. One name admits one row, and a conflicting           naming the missing capability, and a later online broadcast acti-
claim receives an explicit refusal. Registration is a revertible effect,   vates it without code change on any side. A provider going offline
and a copy maintained by broadcast of registration events is obser-        triggers re-resolution, a replacement provider of the same capabil-
vationally equivalent to the in-memory table, following Lemma 4.           ity rebinds the dependents, and a provider announcing departure
                                                                           waits for its confirmed dependents to leave before it withdraws.
5.3     The Transcript                                                     The discipline is a soft layer over the late binding of the bus, a
The transcript is an append-only JSONL file owned by no process,           component that follows none of the three stages still runs, its calls
the single source of truth, and every step of every session is written     answered with an explicit error at the layer below. The order fol-
to it as it happens. An entry records the round, the input, the tool       lows Definition 6, supply precedes consumption and withdrawal
uses with their results, and the streamed text. Messages shown to          follows it. After any process dies, a new process of the same id im-
the model are a projection over the transcript, long tool results are      ports the transcript, rebuilds the projection, and continues the ses-
pruned in the projection while the full text remains in the file, and      sion. Recovery has no rollback and no fork, the rebuilt view equals
nothing is removed from the file itself. The append-only form is the       the view the failed process held, and the steps already recorded are
Research Paper Track                                                                                     AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


never repeated. The rebuilt accumulator composes with whatever           Table 3: The measurement scenarios and their headlines.
the failed process had kept, following Lemma 2, and no other pro-
cess participates, following Lemma 3. An outward effect, payment         Scenario                Model                   Headline
for example, stays outside the boundary, untracked and unrecov-
                                                                         Bus hop latency         GLM-5.3                 median 0.215 ms over
ered, with withholding and compensation as its only routes.
                                                                                                                         10,000 calls
                                                                         Model-side latency      DeepSeek      V4        first token 177 ms, full
5.7     Deployment Boundary                                                                      Flash                   inference 1896.8 ms
Every deployment of this paper runs within trusted networks, on          Router and tool kill    Claude Opus 4.6         20 and 10 trials, all ses-
one machine over the loopback bus and on private grids, and ad-                                                          sions alive
mission to the bus is registration. Trust is placed at mounting, a       Cold-switch mecha-      GPT-5.4                 pure-function      check
tool is admitted by a person who has reviewed its code and started       nism                                            100 of 100
its process. The transcript remains plaintext, and its single-source     End-to-end resump-      DeepSeek          V4    12 of 12 sessions
form is a design choice. Snapshot and compaction are engineering         tion                    Flash
items that archive prefixes and leave replay semantics unchanged.        Crash points            GLM-5.2                 80 of 80 sessions at four
                                                                                                                         kill points
6 Experiments                                                            Plugin assembly         DeepSeek V4 Pro         removal 10 of 10, modi-
                                                                                                                         fication 5 of 5
6.1 Testbed                                                              Multi-agent faults      DeepSeek          V4    three harnesses, two in-
All measurements run on one machine, an AMD Ryzen 7 7435H                                        Flash                   jected faults
with 16 GB of memory under Windows 11, the router and every              Contention    and       GLM-5.3                 4.00 s serialization, first
node as separate processes over the loopback bus, the router in          adoption                                        call 8.4 s
Go 1.26, harnesses and tools in Python 3.13 and Node.js 24. The          Conformance audit       Claude Opus 5           3,500 paired calls, viola-
models in these measurements are DeepSeek V4 Flash, DeepSeek                                                             tions zero
V4 Pro, GLM-5.2, GLM-5.3, Claude Opus 5, Claude Opus 4.6, GPT-
Image-2, and GPT-5.4, the end-to-end and multi-agent runs use
DeepSeek V4 Flash, the crash-point runs use GLM-5.2, and GPT-
Image-2 is the model behind the imagegen tool. Faults arrive as
kills of live processes from outside the system. Every assertion is     6.3    Router Kill
checked against two independent on-disk sources, the transcript         Killing the router process in twenty trials leaves every node alive
and the event stream, and every scenario carries a replay com-          and every session running, the nodes reconnect through supervi-
mand.                                                                   sion, and restoration takes a median of 858 ms, every trial between
   Table 3 lists the scenarios. The comparison group composes the       857 ms and 860 ms. The restoration window is set by the supervi-
same session code from the reference implementation of the calcu-       sion polling granularity, the supervision loop polls, detects, and
lus, same faults, same injections, same criteria, and what the com-     relaunches, and the window follows the polling loop alone. The
parison varies is the form of residence. The reference configura-       death of the router narrows the failure domain from every session
tion composes the session code natively with zero source changes,       to the routing-change window, nodes keep their sessions running
both configurations receive identical injections through the same       through direct connections.
functions and thresholds, and the no-fault baseline differs by 0.8         Killing a tool process in ten trials returns errors to its callers
percent, so the measured damage belongs to the fault.                   in 0.321 ms, the provider remounts in 100.5 ms on the production
                                                                        grid, and the transcript replays under I1 through I4 without a bad
6.2     Scale Separation                                                line. For comparison, killing the whole host of the single-process
                                                                        configuration is detected in 149.5 ms by the external watchdog and
A bus hop costs a median of 0.215 ms over 10000 calls, with a 99th      the full stack restarts in 397.9 ms with a total outage of 547.1 ms,
percentile of 0.377 ms, a 99.9th percentile of 0.623 ms, and a maxi-    while the same fault here ends with the node remounted in 41.3
mum of 3.045 ms. The in-process baseline is a median of 0.005 ms,       ms in thirty trials on the comparison grid and the other nodes un-
so the bus costs 43 times a local call. The model side costs a median   affected.
first token of 177 ms over three calls and a median full inference of
1896.8 ms, so one hop is 1/823 of the first token and 1/8822 of the
full inference. Three orders of magnitude separate the two scales,      6.4    End-to-End Resumption
and the topology is stationary at the step scale of the model.          Twelve sessions run under six process kills, all twelve deliver under
   Concurrent loads of 50, 100, and 200 callers run three rounds        the same criteria, no previously executed action is repeated, and
each with zero losses, and an audit of 3500 calls from 200 con-         the rounds after each kill are 3, 4, 2, 3, 2, and 4. A restart costs
current callers pairs every call with its answer, with no loss, no      1.36 s, following the path of Theorem 1, the transcript prefix as the
duplication, and no misattribution. A compute-bound pair of tools,      anchor record and the rebuilt accumulator composed onto it. The
each saturating one core, finishes in 2000.8 ms on two cores against    white-box replay of the event streams passes I1 through I4 with
4001.3 ms serialized in one host, the two-to-one gap being the          monotonically matching identifiers, and an extended run of thirty
host’s single core.                                                     resumptions succeeds in 30 of 30 trials.
Research Paper Track                                                                                       AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


                                                                           turns with every step on the transcript, and the three rounds de-
                                                                           liver all results correct. Six results are recomputed and the faulting
                                                                           session takes 135 seconds against the 5 seconds of the untouched
                                                                           sessions, the unavoidable cost of the injected fault.
                                                                              Two harnesses claim the tool simultaneously, the calls serialize
                                                                           through 4.00 s, each answer returns to its own caller, and no false
                                                                           timeout occurs. The three sessions recover each from its own shard
                                                                           of the transcript with no coordination, Lemma 3 partitioned per
                                                                           session.


                                                                           6.7    Single-Process Comparison
                                                                           Both configurations run the same session code under the same
Figure 2: The timeline of the concurrent sessions, three har-              faults. The single-process configuration composes it from the ref-
nesses share one tool, the router and the tool provider killed             erence implementation of the calculus [1], version v0.1.0-rc.5 with
together, the fault detected through the broadcast, the tool               250 file fingerprints recorded, and faults arrive as process-tree kills
remounting, and the three rounds completing.                               from outside either configuration, and the criteria are the same,
                                                                           an interruption being a session’s largest gap between consecutive
                                                                           outputs exceeding one and a half times its period. What the com-
   Eighty further sessions extend the coverage to four kill points         parison varies is the form of residence, one host process versus a
of the tool-call cycle, during execution, after return but before per-     set of peer processes.
sistence, after persistence but before announcement, and after an-            Restoration after provider withdrawal in the single-process con-
nouncement. All eighty resume and complete with no repeated ef-            figuration is serial in the number of dependents. Each dependent’s
fect, and the work redone after recovery equals exactly the work           setup re-runs on the shared event loop, one after another, so with
the transcript had not yet recorded, four rounds at the first two          50 ms of loading work per dependent the restoration takes 250.9
points, three at the third, two at the fourth.                             ms at five dependents, 501.5 ms at ten, and 1003.0 ms at twenty,
                                                                           and during the whole restoration an unrelated session in the same
                                                                           host cannot run, frozen for 987.2 ms at twenty dependents. The
6.5     Assembly, Adoption, and Arbitration
                                                                           loading work is controlled injection, and the measurement reads
Removal with a tracked inverse succeeds in 10 of 10 trials with the        the slope of the per-dependent restoration cost across the three de-
external state remounted, in-place modification of a mounted tool          pendent counts. The share of this time that the swap mechanism
succeeds in 5 of 5, isolation between sessions sharing the bus holds       itself accounts for is the empty-closure floor, 0.263 ms to withdraw
in 10 of 10 with a median hop of 0.243 ms, and fifteen rounds of           and 0.567 ms to restore, which is 0.2 percent of the restoration at
churn among providers leave the table equal to the set of living           five dependents and 0.06 percent at twenty. The single-process ad-
providers in 15 of 15 trials. A tool coming online during a task is        vantage in swapping cost exists only when the components being
adopted autonomously, the first call arrives 8.4 s after the registry-     swapped do no work, and under real loading it vanishes into the
update broadcast with no prompt naming the tool, and three such            serial re-execution it must perform. The peer-process construction
adoptions all succeed, an extended run at 10 of 10.                        pays one process start, 126.3 ms measured at the twenty-dependent
   One registration wins among one hundred simultaneous claims             point, and an unrelated session in its own process runs throughout,
of the same name with ninety-nine explicit denials, each denial            with zero freezing.
reaching its claimant, and two observers record identical supply-             A component whose remote resource goes offline terminates its
change sequences across thirty rounds of churn among fifty providers,      host. The unhandled rejection from the connection attempt propa-
the event stream alone reconstructing the final table. A duplicate         gates past the plugin boundary and ends the whole process in all
name never enters the table, and an online tool reaches its con-           five trials, and repair requires redeploying the resource and cold-
sumers through the broadcast alone.                                        restarting the entire stack, 1105 ms before the session runs again.
                                                                           The failing node in the peer-process construction returns an ex-
6.6     Concurrent Sessions                                                plicit error to its caller and keeps running in all five trials, and
Three harnesses share one tool under two injected faults. The provider     repair is the resource’s return, the next round resuming in 107.8
of the shared tool is killed alongside the router, the fault is detected   ms, since the node never died and there was nothing to restart.
in 2.8 ms through the broadcast, the tool remounts in 1 s and the             The host’s death reaches every session it hosts, so the number of
model adopts it autonomously, and the system restores service. Fig-        interrupted sessions is the number of co-resident sessions, a struc-
ure 2 shows the timeline of the two faults and the recovery.               tural consequence of hosting sessions in one process rather than
   The window costs six interim results, the three rounds complete         a measured trend. The five-session composition shows this law in
in 9, 4, and 3 turns, and the two faulting sessions deliver with two       both directions. A single hosting process turns one session’s fault
errors each, both caught and repaired at the time. The calls inside        into the interruption of all five sessions it hosts, in ten trials out
the window reach the dead provider and return explicit errors, the         of ten. The four sessions independent of the fault stopped with the
loud failure of the injection, the model retries and corrects in later     host, the pipeline restarted at step one, discarding completed steps
Research Paper Track                                                                                                AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


Table 4: The single-process reference configuration and the                     Measurements on one machine show twelve sessions resumed
peer-process construction under the same faults.                             through six kills and eighty further sessions through kills at the
                                                                             four boundaries of the tool-call cycle with no repeated effect, nodes
 Fault                 Single-process    refer- Peer-process construc-       reconnect and routing resumes after router loss, and a same-fault
                       ence                     tion                         comparison in which one fault interrupts every co-resident ses-
                                                                             sion while under the peer-process construction one fault ends at
 Host killed    149.5 ms detected, 547.1         remount 41.3 ms in 30
                                                                             one node. The commutation discipline holds as an architectural
                ms total outage, every           of 30 trials, other nodes
                                                                             fact, the shared mutable state of this system being entry tables, the
                co-resident session in-          unaffected
                                                                             broadcast order carries the supply order, the failure behavior of the
                terrupted
                                                                             channel is covered by engineering evidence, the router is a single
 Provider with- closure unload 0.263 ms,          loud error 1.02 ms, re-
                                                                             process whose death narrows the failure domain to the routing-
 drawn          restore 0.567 ms                  mount 80.28 ms in 10
                                                                             change window, and the append-only transcript replays the full
                                                  trials
                                                                             session. Future work strengthens each item into its formal coun-
 Provider              0.518 ms, dependents 10 remount 94.5 ms, callers
                                                                             terpart, a per-key verification of the discipline, a proof of coverage
 restarted             of 10 reloaded             10 of 10 untouched
                                                                             for the order, a formal semantics of loss, partition, and reconnec-
 Cascade cost          50 ms per dependent, one process start 126.3
                                                                             tion, and extends the construction across machines and to larger
                       987 ms freeze              ms, zero freezing
                                                                             provider sets.
 Remote offline        host crash 5 of 5, repair node alive 5 of 5, repair
                       1105 ms                    107.8 ms
                                                                             References
 Co-resident           host dies 10 of 10, 4 of 4 faulty node only 10 of     [1] DeepSeek-AI. 2026. DeepSeek Harness: Everything is a Plugin. https://github.
 fault                 innocent sessions inter- 10, 0 of 4 interrupted           com/deepseek-ai/deepseek-harness. Reference implementation of the calculus,
                       rupted                                                    version v0.1.0-rc.5, 250 file fingerprints recorded.
                                                                             [2] Xinyi Hou, Yanjie Zhao, Shenao Wang, and Haoyu Wang. 2026. Model Con-
 No fault              makespan 24516 ms          makespan 24722 ms, 0.8         text Protocol (MCP): Landscape, Security Threats, and Future Research Directions.
                                                  percent gap                    ACM (2026). doi:10.1145/3796519
                                                                             [3] LangChain Inc. 2024. LangGraph: Building Stateful, Multi-Actor Applications
                                                                                 with LLMs. https://github.com/langchain-ai/langgraph. In-process graph or-
                                                                                 chestration library.
                                                                             [4] Yang Li, Siqi Ping, Xiyu Chen, Xiaojian Qi, et al. 2025. AgentGit: A Version
and recorded progress. Peer processes turn the same fault into one               Control Framework for Reliable and Scalable LLM-Powered Multi-Agent Systems.
node’s replacement, in ten trials out of ten. Those four sessions                arXiv preprint arXiv:2511.00628 (2025).
                                                                             [5] Qin Liu. 2026. 𝜆𝐴 : A Typed Lambda Calculus for LLM Agent Composition. arXiv
delivered without a single gap, the pipeline completed monotoni-                 preprint arXiv:2604.11767 (2026).
cally, and the archive progress strictly advanced. Table 4 lists the         [6] Morgan Quigley, Brian Gerkey, Ken Conley, Josh Faust, Tully Foote, Jeremy Leibs,
                                                                                 Eric Berger, Rob Wheeler, and Andrew Y. Ng. 2009. ROS: an open-source Robot
two configurations side by side.                                                 Operating System. In ICRA Workshop on Open Source Software.
                                                                             [7] Yifan Shi, Wei Zhang, and Tianyi Cui. 2026. A Programming Paradigm for Spa-
6.8      Verification                                                            tiotemporal Composability. arXiv preprint arXiv:2608.25512. Submitted August
                                                                                 26, 2026. https://doi.org/10.48550/arXiv.2608.25512.
Fifteen unit tests check the replay invariants, and a past incident          [8] Temporal Technologies Inc. 2025. Temporal Workflow Execution Platform. https:
                                                                                 //docs.temporal.io. Durable execution engine; workflows defined in code, recov-
is detected in the same replay, two writers, five orphaned entries,              ery via event replay.
and two inversions, caught by I1 through I4 in the event stream.             [9] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Berc Li, Erkang Zhu, Li Jiang,
Approval runs in two layers, dry runs touching nothing outside                   Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, et al. 2024. AutoGen: Enabling Next-
                                                                                 Gen LLM Applications via Multi-Agent Conversation. In First Conference on Lan-
and full runs leaving a record, and the endpoint contract passes                 guage Modeling (COLM). arXiv:2308.08155.
six scenarios with nine assertions. Three checks link the layers to-
gether, the pure-function check passes 100 of 100 and establishes
                                                                             A Proofs
the premise of Lemma 2, the cold-switch check passes 12 of 12 and
establishes Corollary 1, and the contract check establishes the be-          A.1 Setup
havioral face of external resolution. I1 through I4 form an audit            Fix an assignment of components and records to 𝑁 processes and
layer over every measurement of this section, and a replay either            the two conditions of Theorem 1, every effect that must be re-
holds at every entry or names the entry that fails.                          versible writes its anchor to a persistent transcript at the step of
                                                                             occurrence, and every key admits one writer, enforced at registra-
7     Conclusion                                                             tion. An abstract trace is a sequence of assembly and removal steps
This paper established sufficient conditions under which the re-             in the state space. An implemented trace is the sequence of steps
versibility guarantee of the spatiotemporal-composability calculus           the processes actually perform. The theorem constructs, for every
survives the process boundary. The premises of the four lemmas               abstract trace, an implemented trace that agrees with it pointwise
are the hypotheses the calculus already states and the statelessness         under the macrostate projection Π.
of language-model inference. On these conditions it constructed
Logos, where a plugin is a process, the router holds only a routing          A.2      Proof of Lemma 1
table, the only shared state is an append-only transcript, and the           The proof rests on the two modeling facts. By the first fact, a for-
construction satisfies the lemma conditions and the three condi-             ward pass of the language model is a stateless pure map, so cross-
tions of the distributed carrier.                                            step state cannot live inside the model. By the second fact, input
Research Paper Track                                                                                      AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


synthesis and output parsing are defined as operations outside the         and quota resources pass through single-writer tools or stay out-
model. The shared sector is therefore the only remaining residence         side the boundary.
for cross-step state. Co-residence with the model then carries no
state that must stay in the model’s process, and the absence of this       A.5    Proof of Lemma 4
necessity is the contrapositive, co-residence would be necessary
                                                                           The operating requirements of spatial composability are each a fact
only if the state lived inside the model, which the first fact denies,
                                                                           of the calculus, the real-time resolution of keys to providers rests
or if synthesis and parsing had to run where the model runs, which
                                                                           on Definitions 45 and 46, the single writer per key on Definition
the second fact denies by defining them as external operations.
                                                                           58, and supply before demand with withdrawal after consumption
Since the sector is readable from anywhere, the input 𝑥 = 𝜔(𝑆)
                                                                           on Theorem 63. Their content is entirely an assignment of keys to
is the system state made inputtable and can be synthesized at any
                                                                           providers, a routing table. The routing table is the representative
process, and the model becomes an ordinary dispatchable node.
                                                                           case of a commutative key in the calculus, the registration of a
                                                                           route or of an event listener being the representative case in the
A.3     Proof of Lemma 2                                                   original text, and registration is a revertible effect, each provider
The inverse data form a monoid, the composite of two maps that             registering with the broker through a revertible effect. The table
respect ≃ respects ≃, pointwise equality of readouts composes to           therefore resides in the commutative part of the state space, and
equality along the chain, and recover merely evaluates the invari-         a copy maintained by broadcast of registration events is observa-
ant. Each of these steps is a fact of the calculus. Definition 37 re-      tionally equivalent to an in-memory registry. The correspondence
quires inverses to respect ≃, Lemma 38 supplies the machine that           between the calculus constructs and the Logos construction is the
composites of maps respecting ≃ respect ≃, the premise 𝜌(𝑎𝑖 ) ≃ 𝑔𝑖         following.
at every anchor then composes pointwise along the chain of an-
chors, and the readout of the accumulator equals the invariant read.
Recovery through the carrier therefore equals in-place recovery            Table 5: The calculus constructs against the parts of the Lo-
under Π.                                                                   gos construction that realize them.
   Three corollaries follow. The first is the necessity of a record. Re-
versibility leaves a record, a persistent carrier is the physical lower     Calculus construct              Logos realization
bound of the reversible, and this is the commonsense form of the
                                                                            𝐹𝛾 and the per-key provider  the router registry, register with
Landauer principle, stated without a formal citation. Process mem-
                                                                            map                          provides and query the routing ta-
ory under a deployment that tolerates process death satisfies the
                                                                                                         ble
premise for no process, since the process can die, so process mem-
                                                                            notify𝑑 of Definition 26     the node online and offline broad-
ory fails the carrier condition in any fault-tolerant deployment.
                                                                                                         casts driving the tool view
   The second corollary is the derivation of the append-only form.
                                                                            the committed view           the routing in use, the current res-
The algebra of the inverse data is a monoid, and the most general
                                                                                                         olution
persistent carrier of a monoid element is the free monoid on its
                                                                            the order of Theorem 63      the broadcast order plus the serial-
generators, an append-only transcript. The mathematical deriva-
                                                                                                         ized registration
tion reaches exactly the append-only replayable form. The plain-
                                                                            the single writer of Defini- the registration conflict refusal,
text form and the single-source form are design choices, not deriva-
                                                                            tion 58                      measured
tions.
   The third corollary is cold switching. A new process imports the
transcript, rebuilds the external accumulator, and composes it with
what the failed process had kept, the full accumulator being the
composite of the external and the in-process parts. The departure          A.6    The Construction Checklist
of the original process leaves the soundness invariant untouched,          The Logos construction satisfies the four lemmas through the fol-
and under this lemma a process is a disposable auxiliary carrier.          lowing parts. C1 through C4 are given by the lemma conditions,
                                                                           C5 by Lemma 1 together with Lemma 2, C6 is the direct manage-
A.4     Proof of Lemma 3                                                   ment of the boundary of Definition 7, and C7 makes the projection
                                                                           computable.
Any interleaving of the local last-in-first-out sequences is a permu-
tation of all the inverses. Corollary 21 of the calculus asserts that
recovery is invariant under permutation of the applied inverses,           A.7    The Three Engineering Constraints
so the endpoint is the same whichever interleaving runs. The local         The cross-process execution requires three engineering constraints
storage claim and the no-coordination claim follow from the arbi-          beyond the lemma conditions. E1 pairs every response with its
trariness of the permutation. The local storage claim additionally         own call, E2 carries exactly one registration per name with an ex-
rests on the confinement of Definition 48 and on the disjointness          plicit refusal for a conflicting claim, and E3 delivers the same se-
of supply of Definition 58. The shared mutable state of this system        quence of supply-change notifications to every observer. The con-
is entry tables whose operations are appends and deletions, which          struction meets E1 through the single NDJSON protocol and the
fall inside the domain the commutative keys satisfy, and the dis-          bounded queues, E2 through the registration conflict refusal, and
charge mechanism of the calculus is the basis. Shared databases            E3 through the broadcast order plus the serialized registration. The
Research Paper Track                                                                                  AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam


Table 6: The construction parts against the lemma condi-               any interleaving of per-process recoveries, so the removal step
tions they satisfy.                                                    needs no ordering constraint and no shared state with any other
                                                                       process. By Lemma 4 the resolution of the removed component
 Construction part         Satisfied condition                         moves to the routing table, and the routing table is maintained by
                                                                       registration broadcasts, a copy being observationally equivalent
 C1, a capability is an    recovery localization, the component
                                                                       to an in-memory registry. The constraints E2 and E3 guarantee
 independent process       unbound from a host
                                                                       that the registration state and the supply-change order seen by ev-
 C2, the router routes     external resolution and carrier sub-
                                                                       ery observer agree with the abstract resolution step. The pointwise
 and registers only,       stitution, the registry rebuilt by re-
                                                                       agreement under Π follows from Lemma 3 for the recovered com-
 holding no business       registration
                                                                       ponent and from Lemma 4 for the unchanged resolution state.
 state
 C3, the transcript        the free monoid carrier, the replayable     A.8.4 Completion. Induction over the abstract trace assembles the
 is append-only and        form a derivation and the plaintext form    two step cases, and the implemented trace agrees with the abstract
 plaintext, the single     a design choice                             trace pointwise under Π at every step. The implementation is faith-
 source of truth                                                       ful, and the theorem follows. The admission of the deployment as
 C4, cold switching re-    the composition of the rebuilt accumu-      a set of peer processes requires the bus time scale to separate from
 sumes the same id         lator with what the failed process kept     the model time scale, a millisecond hop against a first token a hun-
 C5, the model is an       orchestration externality and carrier       dred times slower, and the topology stationary at the step scale of
 ordinary dispatchable     substitution                                the model, under which the asynchronous contract of the applica-
 bus node                                                              tion note holds throughout the induction.
 C6, outward effects       Definition 7, withholding and compen-
 stay    outside    the    sation as the only routes
 boundary
 C7, every event is        the computable projection, the
 broadcast and re-         macrostate     reconstructable from
 playable                  the event stream


three constraints are engineering realizations, and their formaliza-
tion is future work, the failure semantics of the asynchronous con-
tract, loss, partition, and reconnection, being covered by engineer-
ing evidence at present.

A.8     The Induction
A.8.1 Base Case. The empty abstract trace is implemented by the
empty trace. Both sides start at the same macrostate, and the agree-
ment holds vacuously.
A.8.2 Assembly Step. Let the abstract trace end in an assembly
step. By Lemma 1 the cross-step state resides in the shared sector
outside any model call, so the assembly step does not require the
state to live inside the executing process. By Lemma 2 the tran-
script is a faithful carrier, and the step writes its anchor to the
transcript at the step of occurrence, by the first condition of the
theorem, the settlement order being durable before visible, the an-
chor lands in the transcript before the step is announced on the
bus. The induction hypothesis gives an implemented trace agree-
ing with the abstract prefix under Π up to this step. The constraint
E1 pairs the response of the step with its call, so the implemented
trace contains exactly one step corresponding to the abstract as-
sembly step, and the settlement recorded at the anchor keeps the
pointwise agreement under Π after the step. The macrostate after
the step is determined by the anchor alone, so any process that
reads the transcript prefix reaches the same macrostate.
A.8.3 Removal Step. Let the abstract trace end in a removal step.
By Lemma 3 the inverse data of the component reside in its own
process, and the local last-in-first-out recovery is invariant under
