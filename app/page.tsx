"use client";
import { createElement, useState } from "react";
import Script from "next/script";

const festivals = [
  ["Festival submissions", "17 entries", "Festival review in progress"],
  ["Official selections", "Pending", "Updates will appear here"],
  ["Screenings & Q&As", "Booking", "Schools, libraries, and community groups"],
];
const files = [
  ["Case overview", "Public PDF", "The Gary Jerome Weems Case", "A clear introduction to the story, the family's requests, and why this public archive exists.", "/archive/case-overview/justice-denied-case-overview.pdf"],
  ["Records guide", "Public PDF", "Source Records Inventory", "A guide to the police, medical, witness, legal, news, and family research held in the private collection.", "/archive/records-guide/gary-weems-records-inventory.pdf"],
  ["Legal history", "Public PDF", "Litigation & Advocacy Timeline", "A chronology of documented court milestones and the campaign for independent review and dignified reburial.", "/archive/legal-timeline/justice-denied-litigation-timeline.pdf"],
  ["Research", "Public PDF", "Unanswered Questions", "The identification, notification, first-response, medical, witness, property, and forensic questions guiding the film.", "/archive/research-questions/justice-denied-research-questions.pdf"],
];
const publicRecords = [
  ["16 pages", "Discovery Working File", "Research objectives, discovery index, proposed witnesses, and investigative questions.", [["OPEN PDF", "/archive/public-records/discovery-working-file-redacted.pdf"]]],
  ["52 pages · 5 volumes", "Police, Medical & Legal Records - Part 1", "First-response, police, medical examiner, witness, news, and related legal records.", Array.from({length:5},(_,i)=>[`VOLUME ${i+1}`, `/archive/public-records/police-medical-legal-records-part-1-volume-${String(i+1).padStart(2,"0")}-redacted.pdf`])],
  ["61 pages · 6 volumes", "Court & Correspondence Records - Part 2", "Court filings, attorney correspondence, emails, agency records, and related materials.", Array.from({length:6},(_,i)=>[`VOLUME ${i+1}`, `/archive/public-records/court-correspondence-records-part-2-volume-${String(i+1).padStart(2,"0")}-redacted.pdf`])],
  ["75 pages · 10 volumes", "Compiled Gary Weems Public Records", "A larger compiled record set with personal contact and identifying information redacted.", Array.from({length:10},(_,i)=>[`VOLUME ${i+1}`, `/archive/public-records/gary-weems-compiled-public-records-volume-${String(i+1).padStart(2,"0")}-redacted.pdf`])],
];

export default function Home() {
  const [menu, setMenu] = useState(false);
  const [notice, setNotice] = useState("");
  const soon = (text:string) => { setNotice(text); setTimeout(() => setNotice(""), 3500); };
  return <main>
    {notice && <div className="toast" role="status">{notice}</div>}
    <nav><a className="brand" href="#top"><b>JD</b> JUSTICE DENIED</a><button className="menu" onClick={()=>setMenu(!menu)}>MENU</button>
      <div className={menu ? "links open":"links"}>{[["The Story","story"],["Watch","watch"],["Archive","archive"],["Festival Status","festivals"],["Speaking","speak"],["Donate","support"]].map(x=><a key={x[1]} href={"#"+x[1]} onClick={()=>setMenu(false)}>{x[0]}</a>)}</div>
    </nav>
    <header className="hero" id="top">
      <div className="heroCopy">
        <p className="eyebrow">An independent documentary by Jestina Weems-Rosenduft</p><h1>JUSTICE<br/><i>DENIED</i></h1>
        <p className="lead">A daughter&apos;s fight to uncover the truth about her father&apos;s death—and reclaim the justice, dignity, and peace a system refused to give.</p>
        <div className="actions"><a className="btn red" href="#watch">Watch the teaser ▶</a><a className="btn clear" href="#support">Support the film</a></div>
      </div>
      <div className="heroArt"><img src="/images/justice-denied-cover-clean.jpg" alt="Justice Denied documentary film cover"/><span>OFFICIAL DOCUMENTARY ARTWORK</span></div>
    </header>

    <section id="story"><p className="num">01 / THE STORY</p><blockquote>“When the system says denied, we create our own justice and peace.”</blockquote>
      <div className="columns"><h2>A story buried<br/>for more than<br/><i>three decades.</i></h2><div>
        <p>On November 6, 1993, Gary Jerome Weems died after an encounter with police in Lowell, Massachusetts. His eight-year-old daughter was left with questions that would follow her into adulthood.</p>
        <p><strong>Justice Denied</strong> follows Jestina&apos;s fight for answers: exhumation, DNA testing, a second autopsy, and the right to bury her father with dignity—not in an unmarked pauper&apos;s grave.</p>
        <p>This is about what happens when official records conflict, institutions close ranks, and a daughter refuses to let silence become the final word.</p>
      </div></div></section>

    <section className="dark" id="watch"><Heading number="02 / WATCH" title="Enter the story." text="Watch the official teaser, then follow the making of the film." light/>
      <div className="video"><iframe src="https://www.youtube-nocookie.com/embed/mwPhMGvIWSM" title="Justice Denied official teaser" allowFullScreen/></div>
      <div className="videoGrid"><article><small>NOW PLAYING</small><h3>Official Teaser</h3><p>60 seconds · Justice Denied</p></article>
      <article onClick={()=>soon("Behind-the-scenes videos can be added as soon as they are uploaded.")}><small>COMING NEXT</small><h3>Behind the Scenes</h3><p>Production diaries & filmmaker notes</p></article>
      <article onClick={()=>soon("Interview clips can be linked here when they are ready.")}><small>ARCHIVE SERIES</small><h3>Voices & Interviews</h3><p>Extended conversations and context</p></article></div>
    </section>

    <section id="archive"><Heading number="03 / THE ARCHIVE" title="The record remains open." text="Explore documents, chronology, production history, and educational resources connected to the film."/>
      <div className="fileGrid">{files.map((f,i)=><article key={f[2]}><div className="filetop"><span>FILE 0{i+1}</span><span>{f[1]}</span></div><small>{f[0]}</small><h3>{f[2]}</h3><p>{f[3]}</p><a className="fileLink" href={f[4]} target="_blank" rel="noreferrer">OPEN PDF →</a></article>)}</div>
      <div className="recordsHeading"><p className="num">PUBLIC SOURCE RECORDS</p><h3>Read the underlying record.</h3><p>These are public-record copies with detected personal addresses, phone numbers, emails, signatures, identification details, and similar information blacked out.</p></div>
      <div className="contentWarning"><strong>Content warning:</strong> These files discuss death, substance use, medical findings, alleged police misconduct, and may contain distressing documentary images. Viewer discretion is advised.</div>
      <div className="recordGrid">{publicRecords.map((record,i)=><article key={String(record[1])}><div><span>RECORD {String(i+1).padStart(2,"0")}</span><span>{String(record[0])}</span></div><h3>{String(record[1])}</h3><p>{String(record[2])}</p><nav className="recordLinks" aria-label={`${record[1]} downloads`}>{(record[3] as string[][]).map(link=><a key={link[1]} href={link[1]} target="_blank" rel="noreferrer">{link[0]} →</a>)}</nav></article>)}</div>
      <p className="note">Redaction was applied conservatively for public release. The unchanged original records remain preserved separately.</p>
    </section>

    <section className="dark" id="festivals"><Heading number="04 / FESTIVAL JOURNEY" title="Follow the film." text="Track submissions, selections, awards, and upcoming public screenings." light/>
      <div className="status">{festivals.map((f,i)=><article key={f[0]}><span>0{i+1}</span><div><h3>{f[0]}</h3><p>{f[2]}</p></div><strong>{f[1]}</strong></article>)}</div><p className="updated">LAST UPDATED · AUGUST 2026</p>
    </section>

    <section className="speaker" id="speak"><div className="portrait" role="img" aria-label="Portrait of Jestina Weems-Rosenduft"><small>JESTINA WEEMS-ROSENDUFT</small></div><div className="speakerCopy">
      <p className="num">05 / BRING THE STORY TO YOUR COMMUNITY</p><h2>Book Jestina<br/>to speak.</h2>
      <p>Jestina Weems-Rosenduft is a transformational speaker, author, filmmaker, advocate, and homeschooling mother who turns lived experience into honest conversations about justice, resilience, creativity, faith, and finding your voice.</p>
      <ul><li>Film screenings + Q&A</li><li>Schools, colleges, and libraries</li><li>Keynotes + community conversations</li><li>Storytelling workshops</li></ul>
      <a className="btn red" href="mailto:JesTTMI@gmail.com?subject=Justice%20Denied%20Speaking%20Inquiry">Request speaking information →</a>
    </div></section>

    <section className="support" id="support"><p className="num">06 / SUPPORT THE WORK</p><h2>Help carry this story<br/>into the world.</h2>
      <p>Every contribution helps cover festival submissions, accessibility, travel, legal research, community screenings, and the continued fight to bring Gary Jerome Weems home with dignity.</p>
      <div className="stripeSupport" aria-label="Contribute securely to Justice Denied with Stripe">
        <Script src="https://js.stripe.com/v3/buy-button.js" strategy="afterInteractive" />
        {createElement("stripe-buy-button", {
          "buy-button-id": "buy_btn_1U6af0EvJA1BZEMRny7bwcw4",
          "publishable-key": "pk_live_51LsjDBEvJA1BZEMR3mDBoaCYlWQmwDDx7KvwPpqyp7nK9kiNvk05XZs9D5q9UTjURuQzVjEysL5OMPYRWp1LL2y0000WeToN56",
        })}
      </div>
      <div className="actions center"><a className="btn clear" href="mailto:JesTTMI@gmail.com?subject=Justice%20Denied%20Sponsorship">Become a sponsor</a></div>
      <small>Independent film. Community-powered. Every amount matters.</small>
    </section>
    <footer><a className="brand" href="#top"><b>JD</b> JUSTICE DENIED</a><p>© 2026 Justice Denied · A film by Jestina Weems-Rosenduft</p><a href="mailto:JesTTMI@gmail.com">Contact</a></footer>
  </main>
}
function Heading({number,title,text,light=false}:{number:string,title:string,text:string,light?:boolean}) {return <div className={"heading "+(light?"light":"")}><p className="num">{number}</p><h2>{title}</h2><p>{text}</p></div>}
