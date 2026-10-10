#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).parent
BASE="https://main.direct"
ORG="https://main.direct/#organization"
SITE="https://main.direct/#website"
DESC="Main Direct builds B2B contact data, validation and email deliverability infrastructure for high-signal outreach."
UPDATED="2026-10-10"

def ld(obj): return json.dumps(obj,ensure_ascii=False,separators=(",",":"))

def organization():
    return {
      "@type":"Organization","@id":ORG,"name":"Main Direct","alternateName":["main.direct"],
      "url":BASE+"/","logo":{"@type":"ImageObject","@id":BASE+"/#logo","url":BASE+"/assets/img/icon-512.png","contentUrl":BASE+"/assets/img/icon-512.png","width":512,"height":512,"caption":"Main Direct"},
      "image":[{"@type":"ImageObject","@id":BASE+"/#ogimage","url":BASE+"/og.png","contentUrl":BASE+"/og.png","width":1200,"height":630,"caption":"Main Direct — B2B contact data and email deliverability infrastructure"}],
      "description":DESC,"email":"hello@main.direct",
      "founder":{"@type":"Person","@id":BASE+"/#costa-d","name":"Costa D","givenName":"Konstantin","jobTitle":"Founder","url":"https://www.linkedin.com/in/xcota/"},
      "areaServed":{"@type":"Place","name":"Worldwide"},"knowsLanguage":["en","ru"],
      "sameAs":["https://github.com/xcota/main-direct-site","https://www.linkedin.com/in/xcota/"],
      "contactPoint":{"@type":"ContactPoint","contactType":"sales","email":"hello@main.direct","availableLanguage":["English","Russian"],"areaServed":"Worldwide"}
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
    aria={"home":"Home","services":"Services","playbook":"Playbook","about":"About","contact":"Contact"}
    urls={"home":"/","services":"/services/","playbook":"/playbooks/contact-to-inbox/","about":"/about/","contact":"/contact/"}
    navhtml="".join(f'<li><a href="{urls[p]}"{" aria-current=\"page\"" if p==nav else ""}>{aria[p]}</a></li>' for p in ["home","services","playbook","about","contact"])
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
        <a class="button" href="mailto:hello@main.direct?subject=Main.direct%20infrastructure%20review">Email hello@main.direct</a>
      </div></div>
    </section>
  </main>
  <footer class="site">
    <div class="wrap">
      <div class="footer-grid">
        <div><a class="logo" href="/">main<strong>.</strong>direct</a><p style="margin-top:16px">B2B contact data, validation and email deliverability infrastructure.</p></div>
        <nav aria-label="Site"><h2>Site</h2><ul><li><a href="/">Home</a></li><li><a href="/services/">Services</a></li><li><a href="/playbooks/contact-to-inbox/">Playbook</a></li><li><a href="/about/">About</a></li><li><a href="/faq/">FAQ</a></li></ul></nav>
        <nav aria-label="Technical"><h2>Technical</h2><ul><li><a href="/sitemap.xml">Sitemap</a></li><li><a href="/rss.xml">RSS</a></li><li><a href="/llms.txt">llms.txt</a></li><li><a href="/robots.txt">Robots</a></li></ul></nav>
        <div><h2>Contact</h2><p><a href="mailto:hello@main.direct">hello@main.direct</a></p><p>Remote · Worldwide<br>English · Russian</p></div>
      </div>
      <div class="footer-bottom"><span>© 2026 Main Direct</span><span>Built without trackers or cookies</span><a href="/privacy/">Privacy</a></div>
    </div>
  </footer>
</body>
</html>'''

home_body=f'''  <section class="hero" aria-labelledby="home-title">
    <div class="wrap">
      <p class="eyebrow">Data supply &amp; deliverability engine</p>
      <h1 id="home-title">Contact infrastructure for outreach that survives <span class="accent">the first touch</span>.</h1>
      <p class="lead">Main Direct builds the supply layer behind B2B outreach: verified contact data, clean routing, dedicated sending domains and controls that protect sender reputation.</p>
      <div class="hero-actions"><a class="button" href="/contact/">Request infrastructure review</a><a class="button ghost" href="/playbooks/contact-to-inbox/">Read the system</a><p class="hero-note">No trackers. No purchased lists. No cold sending from a brand domain.</p></div>
    </div>
  </section>
  <section aria-labelledby="services-title">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Capabilities</p><h2 id="services-title">Four coupled layers, one delivery system</h2><p>Outreach breaks in different places. A weak list wastes research; a bad domain burns messages; an unfocused first touch burns attention. Main Direct builds the system end to end.</p></div>
      <div class="grid">
        <article class="card"><span class="tag">Layer 1</span><h3>Contact data engineering</h3><p>Segment sourcing, company mapping, role discovery, normalization, deduplication and a CRM-ready schema with source and freshness fields.</p></article>
        <article class="card"><span class="tag">Layer 2</span><h3>Identity &amp; validation</h3><p>Company-domain resolution, mailbox-pattern testing, permutation checks, role fit and independent identity signals before a contact enters a campaign.</p></article>
        <article class="card"><span class="tag">Layer 3</span><h3>Deliverability infrastructure</h3><p>Dedicated sending domains, SPF/DKIM/DMARC architecture, MTA setup, reputation controls, ramp plans, suppression logic and placement monitoring.</p></article>
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
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Services</nav>
    <h1>B2B contact data, validation &amp; deliverability services</h1>
    <p class="lead">Main Direct builds outreach supply systems for technical founders, revenue teams and partnerships. Engagements can cover one layer or the full contact-to-inbox path.</p>
  </div></section>
  <section aria-labelledby="svc-data"><div class="wrap reading">
    <h2 id="svc-data">Contact data engineering</h2><p class="section-intro">Build a source-of-truth pipeline instead of forwarding spreadsheets.</p>
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

about_body=f'''  <section class="page-hero"><div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / About</nav><h1>The engineering side of B2B outreach</h1><p class="lead">Main Direct is an independent infrastructure practice for contact data, validation and email deliverability. It is not a list broker or a volume-only agency.</p></div></section>
  <section><div class="wrap split">
    <div><p class="eyebrow">About</p><h2>Built around one constraint</h2><p class="lead">Most outreach systems do not fail because someone wrote a bad sentence. They fail because the contact was irrelevant, stale, unreachable or sent through infrastructure that could not carry it.</p></div>
    <div class="facts"><div class="fact"><span class="k">Name</span><strong>Main Direct</strong></div><div class="fact"><span class="k">Founder</span><strong>Costa D</strong></div><div class="fact"><span class="k">Focus</span><strong>Contact data · validation · deliverability</strong></div><div class="fact"><span class="k">Format</span><strong>Infrastructure projects</strong></div><div class="fact"><span class="k">Coverage</span><strong>Remote · worldwide</strong></div><div class="fact"><span class="k">Languages</span><strong>English · Russian</strong></div></div>
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
("How do we start?","Send the target segment, geography, current data, sending domains and volume plan to hello@main.direct. The first review identifies whether the bottleneck is targeting, data, validation, deliverability or message architecture.")
]
faq_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/faq/#webpage","Main Direct FAQ"),{"@type":"FAQPage","@id":BASE+"/faq/#faq","url":BASE+"/faq/","name":"B2B contact data and email deliverability FAQ","inLanguage":"en","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_items]}]}
faq_html="".join(f'<div class="faq-item"><h3 id="q{i}">{q}</h3><p>{a}</p></div>' for i,(q,a) in enumerate(faq_items,1))
faq_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / FAQ</nav><h1>B2B contact data &amp; deliverability FAQ</h1><p class="lead">Direct answers on validation, sending infrastructure and how Main Direct works.</p></div></section><section><div class="wrap"><div class="faq">{faq_html}</div></div></section>'''

services_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/services/#webpage","B2B contact data, validation & deliverability services"),*[{"@type":"Service","@id":BASE+f"/services/#{sid}","name":name,"serviceType":stype,"description":desc,"provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"},"audience":{"@type":"BusinessAudience","audienceType":"B2B revenue, partnerships and fundraising teams"}} for sid,name,stype,desc in [
("contact-data-engineering","Contact data engineering","B2B contact data pipeline","Source mapping, canonical schema, normalization, deduplication and CRM-ready exports."),
("contact-validation","Contact validation & enrichment","B2B contact validation","Company-domain resolution, mailbox pattern testing, role fit and independent identity checks."),
("deliverability-infrastructure","Email deliverability infrastructure","Email deliverability","Sending-domain isolation, SPF/DKIM/DMARC, MTA setup, warm-up, reputation and placement monitoring."),
("first-touch-systems","First-touch architecture","B2B outreach systems","Signal capture, qualification filters, first-touch message architecture and reply routing.")]]]}

about_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/about/#webpage","About Main Direct"),{"@type":"AboutPage","@id":BASE+"/about/#aboutpage","url":BASE+"/about/","name":"About Main Direct","mainEntity":{"@id":ORG}}]}

article_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/playbooks/contact-to-inbox/#webpage","The contact-to-inbox system"),{"@type":"Article","@id":BASE+"/playbooks/contact-to-inbox/#article","url":BASE+"/playbooks/contact-to-inbox/","headline":"The contact-to-inbox system: safer B2B cold email architecture","alternativeHeadline":"How to connect contact validation and email deliverability infrastructure","description":"A five-layer B2B cold email architecture covering target definition, source mapping, contact validation, sending-domain isolation, warm-up and monitoring.","datePublished":"2026-10-10","dateModified":UPDATED,"inLanguage":"en","wordCount":1900,"author":{"@id":BASE+"/#costa-d"},"publisher":{"@id":ORG},"mainEntityOfPage":{"@id":BASE+"/playbooks/contact-to-inbox/#webpage"},"image":{"@id":BASE+"/#ogimage"},"articleSection":["B2B data","Email deliverability","Cold email infrastructure"]}]}
contact_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/contact/#webpage","Contact Main Direct"),{"@type":"ContactPage","@id":BASE+"/contact/#contactpage","url":BASE+"/contact/","name":"Contact Main Direct","mainEntity":{"@id":ORG}}]}
privacy_schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/privacy/#webpage","Privacy",),{"@type":"WebPage","@id":BASE+"/privacy/#privacy","url":BASE+"/privacy/","name":"Privacy","description":"Main Direct privacy and tracking statement."}]}

contact_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Contact</nav><h1>Start with the current constraint</h1><p class="lead">Send context before asking for a scope. A useful review separates data, validation, infrastructure and message problems.</p></div></section>
  <section><div class="wrap reading contact-card card">
    <span class="tag">Direct email</span><h2>hello@main.direct</h2><p style="margin:18px 0 0"><a href="mailto:hello@main.direct?subject=Main.direct%20infrastructure%20review&amp;body=Segment%3A%0AGeography%3A%0ACurrent%20data%3A%0ASending%20domains%2Fvolume%3A%0AMain%20constraint%3A">Open a pre-filled review request</a></p>
    <p class="quiet" style="margin-top:28px">Include: 1) target segment, 2) geography, 3) current contact source, 4) sending domains and monthly volume, 5) what is failing.</p>
    <p class="quiet">No forms, cookies or tracking scripts.</p>
  </div></section>'''

privacy_body=f'''  <section class="page-hero"><div class="wrap reading"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> / Privacy</nav><h1>Privacy</h1><p class="lead">This site has no analytics, cookies, forms or cross-site tracking.</p></div></section>
  <section><div class="wrap reading"><div class="article-content">
    <h2>Site hosting</h2><p>Static files are served by GitHub Pages. Hosting infrastructure may process standard request logs for availability, security and abuse prevention.</p>
    <h2>Contact email</h2><p>If you email hello@main.direct, the message and your address are used to reply and assess the request. Do not send confidential credentials or personal data that the review does not require.</p>
    <h2>Data sharing</h2><p>Request contents are not sold or shared for advertising. Operational data stays within the systems needed to deliver the work.</p>
    <h2>Retention</h2><p>Correspondence is retained only while useful for the request, project or legal record. Ask by email if you need deletion of non-essential correspondence.</p>
  </div></div></section>'''

page404_body=f'''  <section class="page-hero"><div class="wrap reading"><p class="eyebrow">404</p><h1>Route not found</h1><p class="lead">The page is missing. Use the primary sections below.</p><div class="hero-actions"><a class="button" href="/">Home</a><a class="button ghost" href="/services/">Services</a><a class="button ghost" href="/contact/">Contact</a></div></div></section>'''

pages=[
 dict(path="/index.html",title="Main Direct | B2B Contact Data & Email Infrastructure",description="B2B contact data, validation and email deliverability infrastructure for high-signal outreach. Built as an auditable system, not a rented list.",body=home_body,schema={"@context":"https://schema.org","@graph":[*base_graph(BASE+"/#webpage","Main Direct"),*[{"@type":"Service","@id":BASE+f"/#{sid}","name":name,"serviceType":stype,"description":desc,"provider":{"@id":ORG},"areaServed":{"@type":"Place","name":"Worldwide"}} for sid,name,stype,desc in [("contact-data","Contact data engineering","B2B contact data pipeline","Source mapping, normalization, deduplication and CRM-ready contact schemas."),("validation","Identity & validation","B2B contact validation","Domain resolution, mailbox-pattern testing, role fit and independent identity signals."),("deliverability","Deliverability infrastructure","Email deliverability infrastructure","Dedicated domains, SPF/DKIM/DMARC, MTA setup, reputation controls, warm-up and monitoring."),("first-touch","First-touch systems","B2B outreach systems","Signal capture, qualification filters, message architecture and reply routing.")]]]},nav="home"),
 dict(path="/services/index.html",title="B2B Contact Data, Validation & Deliverability Services",description="Contact data engineering, mailbox validation, sending-domain infrastructure and first-touch architecture for B2B outreach.",body=services_body,schema=services_schema,nav="services"),
 dict(path="/playbooks/contact-to-inbox/index.html",title="Contact-to-Inbox System: Safe B2B Cold Email Architecture",description="A practical B2B cold email architecture: source mapping, contact validation, domain isolation, warm-up, monitoring and the first 80 words.",body=article_body,schema=article_schema,nav="playbook"),
 dict(path="/about/index.html",title="About Main Direct | B2B Data & Deliverability Engineering",description="Main Direct is an independent B2B contact-data and email-deliverability infrastructure practice led by Costa D.",body=about_body,schema=about_schema,nav="about"),
 dict(path="/faq/index.html",title="B2B Contact Data & Email Deliverability FAQ | Main Direct",description="Direct answers on B2B contact validation, sending domains, SPF/DKIM/DMARC, warm-up, inbox placement and Main Direct’s scope.",body=faq_body,schema=faq_schema,nav="home"),
 dict(path="/contact/index.html",title="Contact Main Direct | Infrastructure Review",description="Email hello@main.direct with segment, geography, current data and sending setup for a Main Direct infrastructure review.",body=contact_body,schema=contact_schema,nav="contact"),
 dict(path="/privacy/index.html",title="Privacy | Main Direct",description="Main Direct site privacy: no analytics, cookies or forms. Static GitHub Pages hosting and direct email only.",body=privacy_body,schema=privacy_schema,robots="index,follow,max-snippet:-1,max-image-preview:large",nav="home"),
 dict(path="/404.html",title="Page not found | Main Direct",description="The requested Main Direct page was not found.",body=page404_body,schema={"@context":"https://schema.org","@graph":base_graph(BASE+"/404.html","Page not found")},robots="noindex,nofollow",nav="home"),
]
for p in pages:
    out=ROOT/p["path"].lstrip("/")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(shell(title=p["title"],description=p["description"],path="/" if p["path"]=="/index.html" else "/"+p["path"].strip("/")+"/",body=p["body"],page_schema=p["schema"],robots=p.get("robots","index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"),nav=p.get("nav","home")),encoding="utf-8")
    print(out.relative_to(ROOT))
