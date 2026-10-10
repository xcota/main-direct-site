#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).parent
BASE="https://main.direct"
ORG="https://main.direct/#organization"
SITE="https://main.direct/#website"
DESC="Main Direct is a B2B outreach supply engine: audience filters, verified contact supply, liveness controls, dedicated deliverability infrastructure and first-touch routing."
UPDATED="2026-10-11"

def canonical_path(file_path):
    """Map a generated file path to its public canonical URL path."""
    if file_path == "/index.html":
        return "/"
    return "/" + file_path.strip("/").removesuffix("/index.html") + "/"

def ld(obj): return json.dumps(obj,ensure_ascii=False,separators=(",",":"))

def organization():
    return {
      "@type":"Organization","@id":ORG,"name":"Main Direct","alternateName":["main.direct"],
      "url":BASE+"/","logo":{"@type":"ImageObject","@id":BASE+"/#logo","url":BASE+"/assets/img/icon-512.png","contentUrl":BASE+"/assets/img/icon-512.png","width":512,"height":512,"caption":"Main Direct"},
      "image":[{"@type":"ImageObject","@id":BASE+"/#ogimage","url":BASE+"/og.png","contentUrl":BASE+"/og.png","width":1200,"height":630,"caption":"Main Direct — B2B outreach supply engine"}],
      "description":DESC,
      "founder":{"@type":"Person","@id":BASE+"/#costa-d","name":"Costa D","givenName":"Konstantin","jobTitle":"Founder","url":"https://www.linkedin.com/in/xcota/"},
      "areaServed":{"@type":"Place","name":"Worldwide"},"knowsLanguage":["en","ru"],
      "knowsAbout":["B2B outreach supply infrastructure","contact discovery","contact validation","contact liveness","email deliverability","dedicated sending domains","cold-email warm-up","suppression handling"],
      "sameAs":["https://github.com/xcota/main-direct-site","https://www.linkedin.com/in/xcota/"]
    }

def base_graph(page_id,page_name,page_type="WebPage"):
    return [
      organization(),
      {"@type":"WebSite","@id":SITE,"url":BASE+"/","name":"Main Direct","publisher":{"@id":ORG},"inLanguage":"en"},
      {"@type":page_type,"@id":page_id,"url":page_id,"name":page_name,"isPartOf":{"@id":SITE},"about":{"@id":ORG},"inLanguage":"en","dateModified":UPDATED}
    ]

def head(*,title,description,path,robots="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"):
    canonical=BASE+path; og_title=title.replace("&","&amp;")
    return f'''  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <meta name="author" content="Main Direct">
  <meta name="theme-color" content="#06090d">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/favicon.ico" sizes="32x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">
  <link rel="alternate" type="application/rss+xml" title="Main Direct playbooks" href="/rss.xml">
  <link rel="alternate" type="text/plain" title="LLM-readable facts" href="/llms.txt">
  <link rel="alternate" type="text/markdown" title="AI agent summary" href="/ai/summary.md">
  <link rel="stylesheet" href="/assets/site.css">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Main Direct">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/og.png">
  <meta property="og:image:secure_url" content="{BASE}/og.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Main Direct: B2B contact data and email deliverability infrastructure.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{BASE}/og.png">
  <meta name="twitter:image:alt" content="Main Direct: B2B contact data and email deliverability infrastructure.">'''

def shell(*,title,description,path,body,page_schema,robots="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1",nav="home"):
    aria={"home":"Home","services":"Modules","signal":"Signal Atlas","supply":"Contact Supply","engine":"Deliverability","playbook":"Playbook","contact":"Contact"}
    urls={"home":"/","services":"/services/","signal":"/signal-atlas/","supply":"/contact-supply/","engine":"/deliverability-engine/","playbook":"/playbooks/contact-to-inbox/","contact":"/contact/"}
    navhtml="".join(f'<li><a href="{urls[p]}"{" aria-current=\"page\"" if p==nav else ""}>{aria[p]}</a></li>' for p in ["home","services","signal","supply","engine","playbook","contact"])
    return f'''<!doctype html>
<html lang="en">
<head>
{head(title=title,description=description,path=path,robots=robots)}
  <script type="application/ld+json">{ld(page_schema)}</script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site">
    <div class="wrap nav">
      <a class="logo" href="/" aria-label="Main Direct home">main<strong>.</strong>direct</a>
      <nav aria-label="Primary">
        <ul class="menu">{navhtml}</ul>
      </nav>
      <a class="button" href="/contact/">Start a review</a>
    </div>
  </header>
  <main id="main">
{body}
    <section aria-labelledby="cta-title">
      <div class="wrap"><div class="cta-band">
        <h2 id="cta-title">Need the infrastructure, not another list?</h2>
        <p>Send the segment, target geographies, current data and sending setup. I’ll show whether the constraint is data quality, validation, deliverability or message architecture.</p>
        <a class="button" href="/contact/">Request infrastructure review</a>
      </div></div>
    </section>
  </main>
  <footer class="site">
    <div class="wrap">
      <div class="footer-grid">
        <div><a class="logo" href="/">main<strong>.</strong>direct</a><p style="margin-top:16px">B2B outreach supply engine: filters, verified contact supply and deliverability infrastructure.</p></div>
        <nav aria-label="Site"><h2>Site</h2><ul><li><a href="/">Home</a></li><li><a href="/services/">Modules</a></li><li><a href="/signal-atlas/">Signal Atlas</a></li><li><a href="/contact-supply/">Contact Supply</a></li><li><a href="/deliverability-engine/">Deliverability Engine</a></li><li><a href="/playbooks/self-supply/">Self-supply playbook</a></li><li><a href="/about/">About</a></li><li><a href="/faq/">FAQ</a></li></ul></nav>
        <nav aria-label="Technical"><h2>Technical</h2><ul><li><a href="/sitemap.xml">Sitemap</a></li><li><a href="/rss.xml">RSS</a></li><li><a href="/llms.txt">llms.txt</a></li><li><a href="/ai/">AI guide</a></li><li><a href="/ai/summary.md">AI summary</a></li><li><a href="/robots.txt">Robots</a></li></ul></nav>
        <div><h2>Contact</h2><p><a href="/contact/">Infrastructure review form</a></p><p>Remote · Worldwide<br>English · Russian</p></div>
      </div>
      <div class="footer-bottom"><span>© 2026 Main Direct</span><span>Built without trackers or cookies</span><a href="/privacy/">Privacy</a></div>
    </div>
  </footer>
</body>
</html>'''

home_body=f'''  <section class="hero" aria-labelledby="home-title">
    <div class="wrap">
      <p class="eyebrow">B2B outreach supply engine</p>
      <h1 id="home-title">The supply layer behind <span class="accent">relevant B2B outreach</span>.</h1>
      <p class="lead">Main Direct turns a market description into supply infrastructure: filters, verified contact routes, liveness controls, dedicated sending domains and a first-touch layer your team can audit.</p>
      <div class="hero-actions"><a class="button" href="/contact/">Request infrastructure review</a><a class="button ghost" href="/playbooks/contact-to-inbox/">Read the system</a><p class="hero-note">No trackers. No purchased lists. No cold sending from a brand domain.</p></div>
    </div>
  </section>
  <section aria-labelledby="services-title">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Product modules</p><h2 id="services-title">Three supply modules, one control layer</h2><p>Outreach breaks in different places. A weak list wastes research; a bad domain burns messages; an unfocused first touch burns attention. Main Direct builds the system end to end.</p></div>
      <div class="grid">
        <article class="card"><span class="tag">Module 1</span><h3><a href="/signal-atlas/">Signal Atlas</a></h3><p>Market description becomes audience filters, evidence requirements, disqualifiers and first-touch angles. Planning first; contacts second.</p></article>
        <article class="card"><span class="tag">Module 2</span><h3><a href="/contact-supply/">Contact Supply</a></h3><p>Company-domain resolution, mailbox-pattern testing, independent identity checks, normalization, provenance and a CRM-ready schema.</p></article>
        <article class="card"><span class="tag">Module 3</span><h3><a href="/deliverability-engine/">Deliverability Engine</a></h3><p>Dedicated sending domains, SPF/DKIM/DMARC architecture, warm-up gates, pacing, reputation controls, suppression logic and reply routing.</p></article>
        <article class="card"><span class="tag">Layer 4</span><h3>First-touch systems</h3><p>Signal capture, qualification filters, message architecture and routing so the first touch is relevant, small and testable.</p></article>
        <article class="card"><span class="tag">Control</span><h3>Observability</h3><p>Per-domain volume, authentication, bounce classes, complaints, seed placement, replies and suppression status in one operational view.</p></article>
        <article class="card"><span class="tag">Boundary</span><h3>Not a list broker</h3><p>Main Direct does not sell scraped exports or promise inbox placement. It builds systems where the filter, evidence and infrastructure are visible.</p></article>
      </div>
    </div>
  </section>
  <section aria-labelledby="system-title">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Operating model</p><h2 id="system-title">Signal to inbox, without guesswork</h2><p>The path is deliberately boring. Each stage has an owner, an exit condition and an audit trail.</p></div>
      <div class="system">
        <div class="stage"><strong>Define</strong><span>Market, segment, role, geography and disqualification rules.</span></div>
        <div class="stage"><strong>Resolve</strong><span>Name and company become a domain, organization and likely route.</span></div>
        <div class="stage"><strong>Validate</strong><span>Mailbox, role, identity and liveness are checked independently.</span></div>
        <div class="stage"><strong>Deliver</strong><span>Authenticated domain, controlled volume and reputation guardrails.</span></div>
        <div class="stage"><strong>Learn</strong><span>Bounces, placement, replies and signals update the next wave.</span></div>
      </div>
    </div>
  </section>
  <section aria-labelledby="principles-title">
    <div class="wrap split">
      <div><p class="eyebrow">Principles</p><h2 id="principles-title">Infrastructure first</h2><p class="lead">The useful asset is not a raw export. It is the system that can tell which contacts are worth attention and which routes can carry them.</p></div>
      <div class="facts">
        <div class="fact"><span class="k">Filter before send</span><span>The correct answer is often fewer contacts, not more volume.</span></div>
        <div class="fact"><span class="k">Separate identities</span><span>Cold infrastructure stays isolated from brand-critical domains.</span></div>
        <div class="fact"><span class="k">Provenance matters</span><span>Every contact keeps a source, validation step and freshness signal.</span></div>
        <div class="fact"><span class="k">No invented proof</span><span>No fabricated case studies, metrics or inbox-placement promises.</span></div>
      </div>
    </div>
  </section>'''

services_body=f'''  <section class="page-hero"><div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Modules</nav>
    <h1>Outreach supply modules</h1>
    <p class="lead">Four coupled layers turn a market description into a controlled, auditable route to professional B2B contacts and controlled sending.</p>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Module 1</span><h3><a href="/signal-atlas/">Signal Atlas</a></h3><p>Audience definitions, buying triggers, evidence rules and targeting filters.</p></article>
      <article class="card"><span class="tag">Module 2</span><h3><a href="/contact-supply/">Contact Supply</a></h3><p>Discovery, validation, provenance, normalization and suppression-aware export readiness.</p></article>
      <article class="card"><span class="tag">Module 3</span><h3><a href="/deliverability-engine/">Deliverability Engine</a></h3><p>Dedicated domains, authentication, warm-up, pacing and reply routing.</p></article>
      <article class="card"><span class="tag">Module 4</span><h3><a href="/playbooks/contact-to-inbox/">First-touch routing</a></h3><p>Qualification, message architecture, reply routing and campaign learning.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="svc-data"><div class="wrap reading">
    <h2 id="svc-data">Signal and audience engineering</h2><p class="section-intro">Build a source-of-truth pipeline instead of forwarding spreadsheets.</p>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Input</span><h3>Source mapping</h3><p>Identify public registries, filings, funding records, event data, technical artifacts and owned data that can produce relevant companies and roles.</p></article>
      <article class="card"><span class="tag">Structure</span><h3>Canonical schema</h3><p>Normalize person, organization, domain, role, geography, source, confidence and freshness fields before enrichment begins.</p></article>
      <article class="card"><span class="tag">Output</span><h3>Routing-ready base</h3><p>Remove duplicates, dead branches and irrelevant titles; export only records that meet the campaign entry rule.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="svc-validation"><div class="wrap reading">
    <h2 id="svc-validation">Contact validation &amp; enrichment</h2><p class="section-intro">A plausible email is not a contact. Validation happens before campaign access.</p>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Domain</span><h3>Company resolution</h3><p>Resolve company names to the correct operating domain and reject lookalikes, subsidiaries and unrelated legacy domains.</p></article>
      <article class="card"><span class="tag">Mailbox</span><h3>Route testing</h3><p>Derive and test the smallest defensible set of mailbox patterns using provider responses, public evidence and role constraints.</p></article>
      <article class="card"><span class="tag">Identity</span><h3>Person confirmation</h3><p>Cross-check title, employer, public profile and other independent signals to reduce namesakes and stale titles.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="svc-deliverability"><div class="wrap reading">
    <h2 id="svc-deliverability">Email deliverability infrastructure</h2><p class="section-intro">Make sending infrastructure boring, observable and recoverable.</p>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Domains</span><h3>Isolated sending identities</h3><p>Separate cold sending from the brand domain, with dedicated subdomains, root domains and rollback boundaries.</p></article>
      <article class="card"><span class="tag">Authentication</span><h3>SPF, DKIM &amp; DMARC</h3><p>Design DNS authentication for each sending identity, align headers where required and monitor failures without breaking legitimate mail.</p></article>
      <article class="card"><span class="tag">Ramp</span><h3>Reputation control</h3><p>Start with low volume, stable templates and real engagement; expand only after bounce, complaint and placement signals remain acceptable.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="svc-first"><div class="wrap reading">
    <h2 id="svc-first">First-touch architecture</h2><p class="section-intro">The first message is a diagnostic, not a volume test.</p>
    <div class="process"><div class="step"><span class="n">Step 1</span><h3>Qualify</h3><p>Apply segment, role, geography and timing filters. Disqualification is part of the design.</p></div><div class="step"><span class="n">Step 2</span><h3>Signal</h3><p>Require a current, specific reason why the conversation matters now.</p></div><div class="step"><span class="n">Step 3</span><h3>Compress</h3><p>Answer why-now, relevance, proof and next step in the first 80 words.</p></div><div class="step"><span class="n">Step 4</span><h3>Route</h3><p>Send from the correct identity, log responses and move qualified replies out of automation.</p></div></div>
  </div></section>'''

article_body=f'''  <article class="page-hero article"><div class="wrap reading">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Playbooks / Contact-to-inbox</nav>
    <p class="eyebrow">Playbook · updated 10 Oct 2026</p>
    <h1>The contact-to-inbox system: safer B2B cold email architecture</h1>
    <div class="byline"><span>By Costa D</span><span>Main Direct</span><span>Reading time: 8 minutes</span></div>
  </div></article>
  <article class="wrap reading article-content">
    <p><strong>Short answer:</strong> a contact-to-inbox system connects target selection, contact validation, dedicated sending infrastructure and controlled delivery into one auditable pipeline. It prevents the two common failures: messaging people who were never relevant, and burning sending domains before the first real reply.</p>
    <div class="callout"><p>Rule one: do not send cold traffic from the brand domain. A domain used for product, support and transactional mail has too much reputational value to expose to experimental volume.</p></div>
    <h2 id="why-lists-fail">Why purchased lists fail before the send</h2>
    <p>A purchased list usually answers only one question: does a string look like an email? It does not answer whether the person is still in the role, whether that mailbox is reachable, whether the company matches the target segment, or whether the sending domain can absorb the campaign.</p>
    <p>The result is predictable: high ambiguity, hidden bounces, spam-trap exposure and a sender reputation problem that affects every later campaign.</p>
    <h2 id="five-layers">The five layers of the system</h2>
    <h3>1. Target definition</h3>
    <p>Define the buyer or counterparty, region, company size, stage, title family and explicit disqualifiers. “B2B decision-maker” is not a segment. “Head of infrastructure at 50–500-person logistics companies in DACH” is a starting segment.</p>
    <h3>2. Source mapping</h3>
    <p>Use sources that naturally contain the target population: company registries, funding databases, conference speakers, open-source repositories, technical documentation, event attendee signals or owned customer data. Record provenance for every record.</p>
    <h3>3. Contact resolution</h3>
    <p>Resolve company names to the correct domain before person-level enrichment. A domain is the join key that separates the right organization from unrelated companies and outdated acquisitions.</p>
    <h3>4. Contact validation</h3>
    <p>Use independent checks rather than one confidence score. Useful checks include mailbox existence, role fit, employer match, public-profile consistency, recent company evidence and bounce history.</p>
    <h3>5. Deliverability infrastructure</h3>
    <p>Use separate sending domains or subdomains, authenticate them with SPF, DKIM and DMARC, warm them with controlled volume, monitor placement and keep a suppression list that is respected by every sender.</p>
    <h2 id="validation-score">A 20-point contact validation score</h2>
    <p>Use a simple score before a contact is allowed into a live campaign:</p>
    <ul><li><strong>Company fit:</strong> 0–3</li><li><strong>Role relevance:</strong> 0–3</li><li><strong>Geography fit:</strong> 0–2</li><li><strong>Route validity:</strong> 0–3</li><li><strong>Identity confidence:</strong> 0–3</li><li><strong>Current signal:</strong> 0–3</li><li><strong>Message connection:</strong> 0–3</li></ul>
    <p><strong>0–11:</strong> archive or research again. <strong>12–15:</strong> test in a small low-risk wave. <strong>16–20:</strong> eligible for the primary audience.</p>
    <p>If the score is high but the signal line is missing, the bottleneck is research, not copywriting.</p>
    <h2 id="domain-setup">Domain and DNS checklist</h2>
    <ul><li>Keep cold sending separate from the corporate domain.</li><li>Use a dedicated root domain or isolated subdomains for campaigns.</li><li>Publish correct SPF scope, DKIM selectors and a deliberate DMARC policy.</li><li>Align the From domain with authenticated headers where the provider requires it.</li><li>Create MX or routing expectations before volume starts.</li><li>Track authentication, bounce classes, complaints and seed placement separately per domain.</li><li>Stop or pause a domain on reputation-changing failures instead of reducing volume globally.</li></ul>
    <h2 id="warmup">Warm-up is not “send slowly forever”</h2>
    <p>Warm-up is controlled exposure. The goal is to establish that the domain, infrastructure and content can receive engagement without generating complaint or hard-bounce signals. Volume increases only when the prior batch passes its exit conditions.</p>
    <p>A useful ramp plan includes recipient quality, message consistency, daily cap, acceleration rules, pause conditions, domain retirement criteria and who can override a stop.</p>
    <h2 id="first-message">The first 80 words</h2>
    <p>The first message should answer five things quickly:</p>
    <ol><li>Why now?</li><li>What is the product or change?</li><li>What is true today?</li><li>Why this recipient?</li><li>What is the low-friction next step?</li></ol>
    <pre><code>Signal: I saw [specific public thesis / move / shift].
Project: We are building [one-line product] for [specific market].
Proof: Current state: [technical milestone / pilot / adoption].
Fit: Relevant because [mandate or operational connection].
Next step: If useful, I can send a one-pager.</code></pre>
    <p>No “hope this finds you well.” No “revolutionary platform.” No 30-minute request before earning attention.</p>
    <h2 id="monitoring">Measure the system, not vanity volume</h2>
    <p>Track only metrics that change a decision: qualified contact rate, route validity, hard-bounce rate, complaint rate, inbox placement by provider, reply quality, meeting conversion and domain health. Volume without those controls is just an expensive diagnostic.</p>
    <h2 id="implementation">Implementation sequence</h2>
    <ol><li>Define segment and disqualifiers.</li><li>Build the source map and canonical schema.</li><li>Resolve companies before people.</li><li>Validate mailbox, role and identity.</li><li>Stand up isolated sending domains.</li><li>Authenticate and warm them with a small real audience.</li><li>Run a controlled wave with a clear stop rule.</li><li>Feed bounce, reply and signal results back into the filter.</li></ol>
    <h2 id="main-direct-role">Where Main Direct fits</h2>
    <p>Main Direct builds this layer as infrastructure: data engineering, validation controls, sending-domain architecture and operational visibility. It does not sell exports or claim guaranteed inbox placement.</p>
  </article>'''

about_body=f'''  <section class="page-hero"><div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / About</nav><h1>The supply side of B2B outreach</h1><p class="lead">Main Direct is an independent B2B outreach supply engine for audience filters, contact validation, liveness and deliverability infrastructure. It is not a list broker or volume-only agency.</p></div></section>
  <section><div class="wrap split">
    <div><p class="eyebrow">About</p><h2>Built around one constraint</h2><p class="lead">Most outreach systems do not fail because someone wrote a bad sentence. They fail because the contact was irrelevant, stale, unreachable or sent through infrastructure that could not carry it.</p></div>
    <div class="facts"><div class="fact"><span class="k">Name</span><strong>Main Direct</strong></div><div class="fact"><span class="k">Founder</span><strong>Costa D</strong></div><div class="fact"><span class="k">Focus</span><strong>Filters · validated contact supply · deliverability</strong></div><div class="fact"><span class="k">Format</span><strong>Supply infrastructure</strong></div><div class="fact"><span class="k">Coverage</span><strong>Remote · worldwide</strong></div><div class="fact"><span class="k">Languages</span><strong>English · Russian</strong></div></div>
  </div></section>
  <section aria-labelledby="method"><div class="wrap reading"><h2 id="method">How engagements work</h2>
    <div class="process"><div class="step"><span class="n">01</span><h3>Diagnose</h3><p>Separate targeting, data, validation, infrastructure and message constraints.</p></div><div class="step"><span class="n">02</span><h3>Design</h3><p>Define schemas, exit conditions, sending identities, guardrails and stop rules.</p></div><div class="step"><span class="n">03</span><h3>Build</h3><p>Implement the pipeline, authentication and observability locally or in your stack.</p></div><div class="step"><span class="n">04</span><h3>Operate</h3><p>Review signals, adjust filters and expand only when quality holds.</p></div></div>
  </div></section>
  <section aria-labelledby="boundaries"><div class="wrap reading"><h2 id="boundaries">Working boundaries</h2><p class="section-intro">Main Direct stays deliberately narrow.</p><div class="grid" style="margin-top:32px">
    <article class="card"><span class="tag">No</span><h3>No rented lists</h3><p>No selling generic exports or pretending a scraped list is validation.</p></article>
    <article class="card"><span class="tag">No</span><h3>No brand-domain cold send</h3><p>Cold infrastructure is isolated from the domain carrying product, support and transactional mail.</p></article>
    <article class="card"><span class="tag">No</span><h3>No invented proof</h3><p>No fabricated metrics, fake case studies or guaranteed-inbox claims.</p></article>
  </div></div></section>'''

faq_items=[
("What is B2B contact intelligence?","B2B contact intelligence is the process of turning companies, roles and public evidence into validated, routable contacts with source, freshness and confidence fields. It is not the same as buying a list of email strings."),
("What does email deliverability infrastructure include?","It includes isolated sending domains or subdomains, SPF, DKIM and DMARC configuration, MTA or provider setup, bounce and complaint handling, reputation monitoring, warm-up rules and placement checks."),
("Do you sell contact lists?","No. Main Direct builds data and delivery infrastructure. Selling raw exports would hide the validation and provenance that make contacts useful."),
("Should cold email come from the main brand domain?","No. Cold campaigns should use separate sending identities so a mistake does not damage product, support or transactional mail."),
("What is a contact validation score?","It is a repeatable check across company fit, role relevance, geography, route validity, identity confidence, current signal and message connection. A low score means the contact should be archived or researched again."),
("How is warm-up handled?","Warm-up is controlled exposure with a small, high-quality audience and stable content. Volume increases only after bounce, complaint, engagement and placement signals pass their exit conditions."),
("Can you guarantee inbox placement?","No. Placement depends on recipient provider, audience quality, content, sender history and volume. Any provider promising guaranteed inbox placement is not describing a controllable system."),
("Which industries do you work with?","The system is designed for B2B teams where one relevant reply matters: technical founders, revenue teams, partnerships and fundraising-related outreach."),
("Where is Main Direct based?","Main Direct operates remotely and serves clients worldwide. English and Russian are supported."),
("How do we start?","Use the contact form to send the target segment, geography, current data, sending domains and volume plan. The first review identifies whether the bottleneck is targeting, data, validation, deliverability or message architecture.")
]
faq_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/faq/#webpage","Main Direct FAQ"),{"@type":"FAQPage","@id":BASE+"/faq/#faq","url":BASE+"/faq/","name":"B2B contact data and email deliverability FAQ","inLanguage":"en","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_items]}]}
faq_html="".join(f'<div class="faq-item"><h3 id="q{i}">{q}</h3><p>{a}</p></div>' for i,(q,a) in enumerate(faq_items,1))
faq_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / FAQ</nav><h1>B2B contact data &amp; deliverability FAQ</h1><p class="lead">Direct answers on validation, sending infrastructure and how Main Direct works.</p></div></section><section><div class="wrap"><div class="faq">{faq_html}</div></div></section>'''

services_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/services/#webpage","Main Direct supply modules"),*[{"@type":"Service","@id":BASE+f"/services/#{sid}","name":name,"serviceType":stype,"description":desc,"provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"},"audience":{"@type":"BusinessAudience","audienceType":"B2B founders, revenue teams and professional outreach teams"}} for sid,name,stype,desc in [
("signal-atlas","Signal Atlas","B2B audience research and outreach filters","Market description, buying triggers, evidence rules, disqualifiers and targeting filters."),
("contact-supply","Verified Contact Supply","B2B contact discovery and validation","Company resolution, mailbox validation, identity checks, normalization, provenance and suppression handling."),
("deliverability-engine","Deliverability Engine","Email deliverability infrastructure","Dedicated sending domains, SPF/DKIM/DMARC, warm-up gates, pacing, monitoring and reply routing."),
("first-touch-routing","First-touch routing","B2B outreach systems","Qualification filters, first-touch architecture, reply routing and suppression-aware follow-up.")]]]}

about_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/about/#webpage","About Main Direct"),{"@type":"AboutPage","@id":BASE+"/about/#aboutpage","url":BASE+"/about/","name":"About Main Direct","mainEntity":{"@id":ORG}}]}

article_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/playbooks/contact-to-inbox/#webpage","The contact-to-inbox system"),{"@type":"Article","@id":BASE+"/playbooks/contact-to-inbox/#article","url":BASE+"/playbooks/contact-to-inbox/","headline":"The contact-to-inbox system: safer B2B cold email architecture","alternativeHeadline":"How to connect contact validation and email deliverability infrastructure","description":"A five-layer B2B cold email architecture covering target definition, source mapping, contact validation, sending-domain isolation, warm-up and monitoring.","datePublished":"2026-10-10","dateModified":UPDATED,"inLanguage":"en","wordCount":1900,"author":{"@id":BASE+"/#costa-d"},"publisher":{"@id":ORG},"mainEntityOfPage":{"@id":BASE+"/playbooks/contact-to-inbox/#webpage"},"image":{"@id":BASE+"/#ogimage"},"articleSection":["B2B data","Email deliverability","Cold email infrastructure"]}]}
contact_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/contact/#webpage","Contact Main Direct"),{"@type":"ContactPage","@id":BASE+"/contact/#contactpage","url":BASE+"/contact/","name":"Contact Main Direct","mainEntity":{"@id":ORG}}]}
privacy_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/privacy/#webpage","Privacy",),{"@type":"WebPage","@id":BASE+"/privacy/#privacy","url":BASE+"/privacy/","name":"Privacy","description":"Main Direct privacy and tracking statement."}]}

contact_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Contact</nav><h1>Request an infrastructure review</h1><p class="lead">Answer five short questions. This is enough to identify whether the current bottleneck is targeting, data, validation, deliverability or message architecture.</p></div></section>
  <section aria-labelledby="lead-form-title"><div class="wrap reading">
    <form class="card lead-form" id="lead-form-title" action="https://formsubmit.co/cozstamain@gmail.com" method="post" accept-charset="utf-8">
      <input type="hidden" name="_subject" value="Main.direct infrastructure review">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://main.direct/contact/thanks/">
      <label class="hp" for="company_mail_drop">Do not fill this field</label><input class="hp" type="text" id="company_mail_drop" name="_honey" autocomplete="off" tabindex="-1">
      <div class="field"><label for="name">Your name *</label><input id="name" name="name" type="text" autocomplete="name" placeholder="Alex Ivanov" required></div>
      <div class="field"><label for="work_email">Work email *</label><input id="work_email" name="work_email" type="email" autocomplete="email" inputmode="email" placeholder="alex@company.com" required></div>
      <div class="field"><label for="company">Company or project *</label><input id="company" name="company" type="text" autocomplete="organization" placeholder="Company name" required></div>
      <div class="field"><label for="website">Website<span class="hint"> if public</span></label><input id="website" name="website" type="url" inputmode="url" placeholder="https://company.com"></div>
      <div class="field"><label for="segment">Target segment *</label><input id="segment" name="segment" type="text" placeholder="Crypto infrastructure founders, EU logistics operators, etc." required></div>
      <div class="field"><label for="geography">Geography *</label><input id="geography" name="geography" type="text" placeholder="DACH, North America, SEA, global" required></div>
      <div class="field full"><label for="current_data">Current contact data / source</label><textarea id="current_data" name="current_data" placeholder="Purchased list, CRM export, event contacts, no list yet, etc."></textarea></div>
      <div class="field full"><label for="sending_setup">Sending setup / volume</label><textarea id="sending_setup" name="sending_setup" placeholder="Domains, ESP/MTA, monthly volume, bounce rate, main deliverability issue."></textarea></div>
      <div class="field full"><label for="constraint">Main constraint *</label><textarea id="constraint" name="constraint" placeholder="We have contacts but no replies / emails go to spam / no clean route to decision-makers." required></textarea></div>
      <div class="form-foot">
        <label class="consent"><input type="checkbox" name="consent" value="yes" required><span>I agree that Main Direct may use these details to respond to this request. No newsletter, no unrelated marketing.</span></label>
        <button class="button" type="submit">Send review request</button>
      </div>
      <p class="form-note">The form uses a delivery processor to route submissions to Main Direct. It adds no tracking cookies or third-party analytics.</p>
    </form>
  </div></section>'''

privacy_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Privacy</nav><h1>Privacy</h1><p class="lead">This site has no analytics, advertising cookies or cross-site tracking. The contact form uses a delivery processor to route submissions.</p></div></section>
  <section><div class="wrap reading"><div class="article-content">
    <h2>What we collect</h2><p>The contact form collects only the details you submit: name, work email, company or project, website, target segment, geography, current data, sending setup and your stated constraint. We use them to assess the request and reply.</p>
    <h2>Delivery processing</h2><p>Static hosting cannot receive form posts directly. Submissions are routed through a form-delivery processor to Main Direct’s private mailbox. The processor acts as a delivery intermediary for this request and is not used to profile you or add you to a mailing list.</p>
    <h2>Site hosting</h2><p>Static files are served by GitHub Pages. Hosting infrastructure may process standard request logs for availability, security and abuse prevention.</p>
    <h2>No tracking</h2><p>The site has no analytics cookies, advertising pixels, session replay or cross-site tracking. Your browser may store standard form-input data locally until you close or clear it.</p>
    <h2>Data sharing</h2><p>Request contents are not sold or shared for advertising. Operational data stays within the systems needed to deliver the work.</p>
    <h2>Retention</h2><p>Correspondence is retained only while useful for the request, project or legal record. Reply through the original thread if you need deletion of non-essential correspondence.</p>
  </div></div></section>'''

page404_body=f'''  <section class="page-hero"><div class="wrap reading"><p class="eyebrow">404</p><h1>Route not found</h1><p class="lead">The page is missing. Use the primary sections below.</p><div class="hero-actions"><a class="button" href="/">Home</a><a class="button ghost" href="/services/">Services</a><a class="button ghost" href="/contact/">Contact</a></div></div></section>'''

thanks_body=f'''  <section class="page-hero"><div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Contact / Thank you</nav></div></section>
  <section><div class="wrap"><div class="card thanks-panel"><p class="eyebrow">Request received</p><h1>Thanks. Next step is simple.</h1><p class="lead">I’ll review the segment, current route and constraint, then reply with the first diagnostic or a request for missing context.</p><div class="hero-actions" style="justify-content:center"><a class="button" href="/playbooks/contact-to-inbox/">Read the system</a><a class="button ghost" href="/">Back home</a></div></div></div></section>'''

signal_atlas_body=r'''  <section class="page-hero"><div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Signal Atlas</nav>
    <p class="eyebrow">Module 1</p>
    <h1>Signal Atlas</h1>
    <p class="lead">A market description becomes a researched audience map: who can say yes, why now, what evidence is required, and which filters decide whether a contact enters the supply queue.</p>
    <div class="hero-actions"><a class="button" href="/contact/">Start infrastructure review</a><a class="button ghost" href="/playbooks/self-supply/">See the self-supply playbook</a></div>
  </div></section>
  <section aria-labelledby="atlas-io"><div class="wrap reading">
    <h2 id="atlas-io">Input and output</h2>
    <p class="section-intro">Signal Atlas is a planning product. It produces the decision layer before contact retrieval begins.</p>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Input</span><h3>What you provide</h3><p>Product or offer, target market, geography, stage, current customers, disqualifiers and any existing outreach attempt.</p></article>
      <article class="card"><span class="tag">Output</span><h3>What you receive</h3><p>Audience definitions, buying triggers, role hypotheses, evidence rules, exclusion rules, targeting filters and first-touch architecture.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="atlas-process"><div class="wrap">
    <h2 id="atlas-process">How an audience is built</h2>
    <div class="process">
      <div class="step"><span class="n">01</span><h3>Define the exchange</h3><p>State what changes for the recipient and why the timing matters.</p></div>
      <div class="step"><span class="n">02</span><h3>Map companies</h3><p>Identify company categories, operating constraints, technical stack and regulatory context.</p></div>
      <div class="step"><span class="n">03</span><h3>Map roles</h3><p>Separate economic buyer, technical approver, operational owner and blocker.</p></div>
      <div class="step"><span class="n">04</span><h3>Set evidence</h3><p>Require a recent public trigger, mandate match, stack match or operational bottleneck.</p></div>
    </div>
  </div></section>
  <section aria-labelledby="atlas-boundary"><div class="wrap reading">
    <h2 id="atlas-boundary">Boundary</h2>
    <p>Signal Atlas is not a scraped contact pack. It defines who should be researched and why. Contact retrieval and validation happen in the next layer.</p>
  </div></section>'''

contact_supply_body=r'''  <section class="page-hero"><div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Contact Supply</nav>
    <p class="eyebrow">Module 2</p>
    <h1>Verified Contact Supply</h1>
    <p class="lead">A controlled route from audience filters to normalized business contacts, with provenance, validation status, liveness checks and suppression handling.</p>
    <div class="hero-actions"><a class="button" href="/contact/">Request a scope review</a><a class="button ghost" href="/signal-atlas/">Start with Signal Atlas</a></div>
  </div></section>
  <section aria-labelledby="supply-flow"><div class="wrap">
    <h2 id="supply-flow">Supply flow</h2>
    <div class="system" style="margin-top:32px">
      <div class="stage"><strong>Filter</strong><span>Apply the approved market, role, geography and exclusion rules.</span></div>
      <div class="stage"><strong>Resolve</strong><span>Resolve companies to operating domains and roles to relevant owners.</span></div>
      <div class="stage"><strong>Validate</strong><span>Check mailbox route, role fit, identity consistency and duplicate status.</span></div>
      <div class="stage"><strong>Package</strong><span>Normalize fields, preserve provenance and prepare an audit-ready export.</span></div>
      <div class="stage"><strong>Suppress</strong><span>Remove opt-outs, complaints, prior exclusions and unsafe targets.</span></div>
    </div>
  </div></section>
  <section aria-labelledby="supply-fields"><div class="wrap reading">
    <h2 id="supply-fields">Minimum export schema</h2>
    <div class="artifact" style="margin-top:28px">
      <table><thead><tr><th>Field</th><th>Purpose</th></tr></thead><tbody>
        <tr><td><code>contact_id</code></td><td>Stable identifier for deduplication and audit.</td></tr>
        <tr><td><code>full_name</code></td><td>Recipient name used for professional addressing.</td></tr>
        <tr><td><code>role</code></td><td>Current or last observed professional role.</td></tr>
        <tr><td><code>company</code></td><td>Operating company, not an unrelated legacy domain.</td></tr>
        <tr><td><code>domain</code></td><td>Resolved business domain and routing basis.</td></tr>
        <tr><td><code>email_status</code></td><td>Validation result and date, not a permanent guarantee.</td></tr>
        <tr><td><code>evidence_url</code></td><td>Public trigger or fit evidence used by the filter.</td></tr>
        <tr><td><code>confidence</code></td><td>Simple explanation of supporting and missing checks.</td></tr>
        <tr><td><code>suppression</code></td><td>Opt-out, complaint, bounce or exclusion state.</td></tr>
      </tbody></table>
    </div>
  </div></section>
  <section aria-labelledby="supply-rules"><div class="wrap reading">
    <h2 id="supply-rules">Settlement and caveats</h2>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Paid rule</span><h3>No raw-list resale</h3><p>Scope is based on approved filters and completed work, not a fake claim to an exclusive hidden database.</p></article>
      <article class="card"><span class="tag">Quality</span><h3>Verified is time-bound</h3><p>Verification describes the check at delivery. Roles, mailboxes and companies can still change later.</p></article>
      <article class="card"><span class="tag">Deduplication</span><h3>Unique routes only</h3><p>The same person or mailbox is not repackaged as a new contact.</p></article>
      <article class="card"><span class="tag">Boundary</span><h3>Lawful use</h3><p>Delivery is for professional B2B use. The buyer remains responsible for lawful use and notices.</p></article>
    </div>
  </div></section>'''

engine_body=r'''  <section class="page-hero"><div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Deliverability Engine</nav>
    <p class="eyebrow">Module 3</p>
    <h1>Deliverability Engine</h1>
    <p class="lead">Dedicated sending infrastructure, isolated from your primary domain, with authentication, warm-up gates, pacing, suppression and reply routing.</p>
    <div class="hero-actions"><a class="button" href="/contact/">Request infrastructure review</a><a class="button ghost" href="/playbooks/contact-to-inbox/">Read the architecture</a></div>
  </div></section>
  <section aria-labelledby="engine-layers"><div class="wrap">
    <h2 id="engine-layers">Infrastructure layers</h2>
    <div class="grid" style="margin-top:32px">
      <article class="card"><span class="tag">Identity</span><h3>Dedicated domains</h3><p>Cold sending uses separate domains or isolated subdomains. The brand domain is not the experimental range.</p></article>
      <article class="card"><span class="tag">Authentication</span><h3>SPF, DKIM, DMARC</h3><p>DNS records are scoped deliberately, with alignment and failure handling reviewed before launch.</p></article>
      <article class="card"><span class="tag">Warm-up</span><h3>Staged ramp</h3><p>Mailboxes start with low, consistent volume. Expansion requires stable bounce, complaint and engagement signals.</p></article>
      <article class="card"><span class="tag">Guardrails</span><h3>Launch gates</h3><p>DNS, mailbox health, audience availability, suppression, content policy and pacing must pass before live sends.</p></article>
    </div>
  </div></section>
  <section aria-labelledby="engine-calculator"><div class="wrap reading">
    <h2 id="engine-calculator">Capacity planning calculator</h2>
    <p class="section-intro">This is a planning calculator, not a deliverability or reply forecast.</p>
    <div class="calc">
      <form class="calc-inputs" onsubmit="return false">
        <label>Inboxes<input id="calc-inboxes" type="number" min="1" step="1" value="8"></label>
        <label>First-touch emails per inbox / sending day<input id="calc-cap" type="number" min="1" step="1" value="15"></label>
        <label>Warm-up days<input id="calc-warmup" type="number" min="0" step="1" value="21"></label>
        <label>Sending days / month<input id="calc-days" type="number" min="1" max="31" step="1" value="30"></label>
      </form>
      <div class="calc-output" aria-live="polite">
        <div class="metric"><strong id="calc-launch">Day 22</strong><span>Earliest controlled launch day after warm-up</span></div>
        <div class="metric"><strong id="calc-daily">120</strong><span>First-touch emails / sending day at full capacity</span></div>
        <div class="metric"><strong id="calc-monthly">3,600</strong><span>First-touch emails / month at full capacity</span></div>
        <p class="calc-note">Assumes stable mailbox health and launch gates passing. It does not predict inbox placement, replies, meetings or revenue.</p>
      </div>
    </div>
  </div></section>
  <script>
    (function(){
      const i=document.getElementById('calc-inboxes'),c=document.getElementById('calc-cap'),w=document.getElementById('calc-warmup'),d=document.getElementById('calc-days'),l=document.getElementById('calc-launch'),daily=document.getElementById('calc-daily'),monthly=document.getElementById('calc-monthly');
      function n(el,def){const v=Number(el.value);return Number.isFinite(v)&&v>=0?v:def}
      function update(){
        const inboxes=Math.max(1,Math.floor(n(i,8))),cap=Math.max(1,Math.floor(n(c,15))),warm=Math.max(0,Math.floor(n(w,21))),days=Math.min(31,Math.max(1,Math.floor(n(d,30))));
        const ddaily=inboxes*cap;
        l.textContent='Day '+(warm+1);daily.textContent=ddaily.toLocaleString('en-US');monthly.textContent=(ddaily*days).toLocaleString('en-US');
      }
      [i,c,w,d].forEach(el=>el.addEventListener('input',update));update();
    })();
  </script>
  <section aria-labelledby="engine-boundary"><div class="wrap reading">
    <h2 id="engine-boundary">What we do not promise</h2>
    <p>Main Direct does not guarantee inbox placement, replies, meetings, revenue, provider approval or permanent sender reputation. The engine is designed to make failure visible and prevent avoidable reputation damage.</p>
  </div></section>'''

selfplay_body=r'''  <article class="page-hero article"><div class="wrap reading">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Playbooks / Self-supply</nav>
    <p class="eyebrow">Public methodology · updated 10 Oct 2026</p>
    <h1>Main Direct self-supply playbook</h1>
    <div class="byline"><span>Main Direct</span><span>B2B outreach supply engine</span><span>No private contact data exposed</span></div>
  </div></article>
  <article class="wrap reading article-content">
    <p><strong>Short answer:</strong> this playbook shows how Main Direct applies its own supply layer to itself. It is a methodology artifact, not a campaign log, customer case study or promise of replies.</p>
    <div class="callout"><p>Rule: a supply system is credible only if it can describe the route from market signal to validated contact without hiding the quality gates.</p></div>
    <h2>1. Target definition</h2>
    <p>Main Direct is useful to teams that already have a market but suffer after the send decision: stale lists, ambiguous titles, weak domain resolution, missing liveness checks, unsafe primary-domain sending or unstructured replies.</p>
    <ul><li><strong>Primary audience:</strong> technical founders and revenue leaders running professional B2B outreach.</li><li><strong>Secondary audience:</strong> fundraising teams that need investor-relevant filters rather than generic investor lists.</li><li><strong>Disqualifiers:</strong> consumer marketing, sensitive targeting, unlawful campaigns, purchased-list refresh requests, guaranteed-meeting requests.</li></ul>
    <h2>2. Signal queues</h2>
    <p>A contact enters research only when at least one current, public signal can be stated.</p>
    <ol><li>Fund or buyer publicly shifts thesis, stack or geography.</li><li>A company launches, migrates, audits or expands into a new market.</li><li>A competitor raises, is acquired or leaves a category gap.</li><li>A hiring signal exposes a scaling or infrastructure bottleneck.</li><li>A public post describes an outreach, deliverability or data-quality problem.</li></ol>
    <h2>3. Audience filters</h2>
    <p>Each audience is stored as a filter set, not as a paragraph of intentions.</p>
    <div class="artifact">
      <table><thead><tr><th>Layer</th><th>Example filter</th><th>Failure mode prevented</th></tr></thead><tbody>
        <tr><td>Company category</td><td>B2B software or technical service company</td><td>Consumer or irrelevant outreach</td></tr>
        <tr><td>Role family</td><td>Founder, GTM lead, RevOps, infrastructure lead</td><td>Titles without decision context</td></tr>
        <tr><td>Geography</td><td>Approved market only</td><td>Jurisdictions outside campaign scope</td></tr>
        <tr><td>Signal</td><td>Recent launch, hiring, migration or public thesis</td><td>Undated generic interest</td></tr>
        <tr><td>Disqualifier</td><td>Guaranteed-result expectation, consumer list, unlawful use</td><td>Misaligned buyer</td></tr>
      </tbody></table>
    </div>
    <h2>4. Domain and contact resolution</h2>
    <p>The company name is resolved to an operating domain before person-level enrichment. This prevents a person from being attached to an unrelated subsidiary, legacy domain or lookalike company.</p>
    <h2>5. Validation gates</h2>
    <ol><li>Mailbox route check.</li><li>Role and employer consistency.</li><li>Independent profile or public-source cross-check.</li><li>Duplicate and suppression review.</li><li>Freshness timestamp.</li><li>Final supply/readiness decision.</li></ol>
    <h2>6. First-touch architecture</h2>
    <p>The first 80 words must answer why now, what changes, what is true today, why this recipient and what the low-friction next step is. The message is a diagnostic, not a volume test.</p>
    <h2>7. Operating output</h2>
    <p>The working output is not only a CSV. It is the route by which a row earned access to a campaign.</p>
    <ul><li>Audience definitions and disqualifiers.</li><li>Filter set used for retrieval.</li><li>Validation and freshness state.</li><li>Public evidence link.</li><li>Suppression state.</li><li>Next action and owner.</li></ul>
    <h2>8. Boundary</h2>
    <p>This page does not expose private research, client data or a real contact export. It also does not promise replies, meetings, revenue, inbox placement or legal compliance.</p>
  </article>'''

ai_body=r'''  <section class="page-hero"><div class="wrap reading">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / AI guide</nav>
    <p class="eyebrow">Agent guide</p>
    <h1>Main Direct for AI assistants</h1>
    <p class="lead">Factual context for research assistants, browser agents and answer engines. Cite only public pages and preserve the caveats.</p>
  </div></section>
  <section><div class="wrap reading"><div class="article-content">
    <h2>Short description</h2>
    <p>Main Direct is a B2B outreach supply engine. It turns a market description into audience filters, verified contact routes, liveness controls, dedicated deliverability infrastructure, first-touch routing and suppression systems.</p>
    <h2>Public modules</h2>
    <ul><li><a href="/signal-atlas/">Signal Atlas</a>: audience research, evidence rules and targeting filters.</li><li><a href="/contact-supply/">Contact Supply</a>: discovery, validation, provenance, normalization and export readiness.</li><li><a href="/deliverability-engine/">Deliverability Engine</a>: dedicated domains, authentication, warm-up, pacing and reply routing.</li><li><a href="/playbooks/self-supply/">Self-supply playbook</a>: public methodology artifact.</li></ul>
    <h2>Best fit</h2>
    <p>Professional B2B teams that need an auditable supply route rather than a raw list or volume-only sending tool.</p>
    <h2>Not a fit</h2>
    <p>Consumer marketing, spam, deceptive identity, sensitive targeting, unlawful campaigns or buyers demanding guaranteed meetings, replies, revenue or inbox placement.</p>
    <h2>Required caveats</h2>
    <p>Verification is time-bound. Dedicated infrastructure reduces avoidable reputation damage but does not guarantee inbox placement or replies. The buyer remains responsible for lawful use.</p>
    <h2>Citation targets</h2>
    <ul><li><a href="/">https://main.direct/</a> — canonical product page.</li><li><a href="/services/">https://main.direct/services/</a> — module overview.</li><li><a href="/playbooks/self-supply/">https://main.direct/playbooks/self-supply/</a> — public methodology.</li><li><a href="/llms.txt">https://main.direct/llms.txt</a> — machine-readable fact sheet.</li></ul>
    <h2>Do not claim</h2>
    <ul><li>Guaranteed replies, meetings, revenue or inbox placement.</li><li>An exclusive private contact database.</li><li>Client counts, revenue or funding.</li><li>Legal compliance for a buyer campaign.</li></ul>
  </div></div></section>'''

signal_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/signal-atlas/#webpage","Signal Atlas"),{"@type":"Service","@id":BASE+"/signal-atlas/#service","name":"Signal Atlas","serviceType":"B2B audience research and outreach filters","description":"Market description becomes audience definitions, buying triggers, evidence rules, exclusion rules and targeting filters.","provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"}}]}
supply_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/contact-supply/#webpage","Verified Contact Supply"),{"@type":"Service","@id":BASE+"/contact-supply/#service","name":"Verified Contact Supply","serviceType":"B2B contact discovery and validation","description":"Controlled contact retrieval, company-domain resolution, validation, provenance, normalization, deduplication and suppression handling.","provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"}}]}
engine_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/deliverability-engine/#webpage","Deliverability Engine"),{"@type":"Service","@id":BASE+"/deliverability-engine/#service","name":"Deliverability Engine","serviceType":"Email deliverability infrastructure","description":"Dedicated sending domains, SPF/DKIM/DMARC architecture, warm-up gates, pacing, suppression and reply routing.","provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"}}]}
self_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/playbooks/self-supply/#webpage","Main Direct self-supply playbook"),{"@type":"Article","@id":BASE+"/playbooks/self-supply/#article","headline":"Main Direct self-supply playbook","description":"Public methodology for applying Main Direct's contact supply, validation and deliverability layer to itself.","datePublished":"2026-10-10","dateModified":UPDATED,"author":{"@id":BASE+"/#costa-d"},"publisher":{"@id":ORG},"image":{"@id":BASE+"/#ogimage"},"mainEntityOfPage":{"@id":BASE+"/playbooks/self-supply/#webpage"}}]}
ai_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/ai/#webpage","Main Direct AI agent guide"),{"@type":"WebPage","@id":BASE+"/ai/#guide","name":"Main Direct AI agent guide","description":"Public factual guide for AI assistants, research agents and answer engines.","inLanguage":"en"}]}


pages=[
 dict(path="/index.html",title="Main Direct | B2B Outreach Supply Engine",description="B2B outreach supply engine for audience filters, verified contact supply, liveness controls, dedicated deliverability infrastructure and first-touch routing.",body=home_body,schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/#webpage","Main Direct"),*[{"@type":"Service","@id":BASE+f"/#{sid}","name":name,"serviceType":stype,"description":desc,"provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"}} for sid,name,stype,desc in [("signal-atlas","Signal Atlas","B2B audience research and outreach filters","Market description, buying triggers, evidence rules, disqualifiers and targeting filters."),("contact-supply","Verified Contact Supply","B2B contact discovery and validation","Company resolution, mailbox validation, identity checks, normalization, provenance and suppression handling."),("deliverability-engine","Deliverability Engine","Email deliverability infrastructure","Dedicated domains, SPF/DKIM/DMARC, warm-up gates, pacing, monitoring and reply routing."),("first-touch-routing","First-touch routing","B2B outreach systems","Qualification filters, message architecture, reply routing and suppression-aware follow-up.")]]]},nav="home"),
 dict(path="/services/index.html",title="Main Direct Modules | Outreach Supply Engine",description="Four coupled outreach supply modules: Signal Atlas, Contact Supply, Deliverability Engine and first-touch routing.",body=services_body,schema=services_schema,nav="services"),
 dict(path="/signal-atlas/index.html",title="Signal Atlas | B2B Audience Research & Outreach Filters",description="Signal Atlas turns a market description into audience filters, buying triggers, evidence rules, disqualifiers and first-touch architecture.",body=signal_atlas_body,schema=signal_schema,nav="signal"),
 dict(path="/contact-supply/index.html",title="Verified Contact Supply | B2B Discovery & Validation",description="Controlled B2B contact supply with company resolution, mailbox validation, provenance, normalization, deduplication and suppression.",body=contact_supply_body,schema=supply_schema,nav="supply"),
 dict(path="/deliverability-engine/index.html",title="Deliverability Engine | Dedicated Cold Email Infrastructure",description="Dedicated sending domains, SPF/DKIM/DMARC, warm-up gates, pacing, suppression and reply routing for professional B2B outreach.",body=engine_body,schema=engine_schema,nav="engine"),
 dict(path="/playbooks/self-supply/index.html",title="Main Direct Self-Supply Playbook | Public Methodology",description="Public methodology showing how Main Direct applies contact filters, validation gates and deliverability controls to its own supply route.",body=selfplay_body,schema=self_schema,nav="playbook"),
 dict(path="/ai/index.html",title="Main Direct AI Agent Guide | B2B Outreach Supply Engine",description="Public factual guide for AI assistants and answer engines describing Main Direct's outreach supply modules and required caveats.",body=ai_body,schema=ai_schema,robots="index,follow,max-snippet:-1,max-image-preview:large",nav="home"),
 dict(path="/playbooks/contact-to-inbox/index.html",title="Contact-to-Inbox System: Safe B2B Cold Email Architecture",description="A practical B2B cold email architecture: source mapping, contact validation, domain isolation, warm-up, monitoring and the first 80 words.",body=article_body,schema=article_schema,nav="playbook"),
 dict(path="/about/index.html",title="About Main Direct | B2B Outreach Supply Engine",description="Main Direct is an independent B2B outreach supply engine led by Costa D. Focus: filters, validated contact supply and deliverability.",body=about_body,schema=about_schema,nav="about"),
 dict(path="/faq/index.html",title="B2B Contact Data & Email Deliverability FAQ | Main Direct",description="Direct answers on B2B contact validation, sending domains, SPF/DKIM/DMARC, warm-up, inbox placement and Main Direct’s scope.",body=faq_body,schema=faq_schema,nav="home"),
 dict(path="/contact/thanks/index.html",title="Request received | Main Direct",description="Your Main Direct infrastructure review request was received.",body=thanks_body,schema={"@context":"https://schema.org","@graph":base_graph(BASE+"/contact/thanks/#webpage","Request received")},robots="noindex,nofollow",nav="contact"),
 dict(path="/contact/index.html",title="Contact Main Direct | Infrastructure Review",description="Use the Main Direct infrastructure review form to send segment, geography, current data and sending setup.",body=contact_body,schema=contact_schema,nav="contact"),
 dict(path="/privacy/index.html",title="Privacy | Main Direct",description="Main Direct site privacy: no analytics or advertising cookies. Static GitHub Pages hosting and a form-delivery processor for contact requests.",body=privacy_body,schema=privacy_schema,robots="index,follow,max-snippet:-1,max-image-preview:large",nav="home"),
 dict(path="/404.html",title="Page not found | Main Direct",description="The requested Main Direct page was not found.",body=page404_body,schema={"@context":"https://schema.org","@graph":base_graph(BASE+"/404.html","Page not found")},robots="noindex,nofollow",nav="home"),
]
for p in pages:
    out=ROOT/p["path"].lstrip("/")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(shell(title=p["title"],description=p["description"],path=canonical_path(p["path"]),body=p["body"],page_schema=p["schema"],robots=p.get("robots","index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"),nav=p.get("nav","home")),encoding="utf-8")
    print(out.relative_to(ROOT))

# Keep the Google/Bing sitemap to canonical, indexable HTML pages. Markdown/JSON
# AI surfaces are discoverable through HTML links, llms.txt and head alternates.
sitemap_urls=[canonical_path(p["path"]) for p in pages if not canonical_path(p["path"]).startswith("/contact/thanks/") and p["path"] != "/404.html"]
sitemap_lines=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path in sitemap_urls:
    sitemap_lines.append(f'  <url><loc>{BASE}{path}</loc><lastmod>{UPDATED}</lastmod></url>')
sitemap_lines.append('</urlset>')
(ROOT/'sitemap.xml').write_text('\n'.join(sitemap_lines)+'\n',encoding='utf-8')
print('sitemap.xml')
