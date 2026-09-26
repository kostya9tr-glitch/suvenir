# -*- coding: utf-8 -*-
from common import page, BRAND, ADDRESS_STREET, ADDRESS_CITY, PHONE, EMAIL


def build_impressum():
    title = f"Impressum | {BRAND}"
    desc = f"Impressum von {BRAND} gemäss Schweizer Recht."
    body = f"""
    <section class="section">
      <div class="container legal">
        <h1>Impressum</h1>
        <h2>Anbieterkennzeichnung</h2>
        <p>{BRAND}<br>{ADDRESS_STREET}<br>{ADDRESS_CITY}<br>Schweiz</p>
        <p>Telefon: {PHONE}<br>E-Mail: {EMAIL}</p>
        <p>Inhaber/in: [Name der Inhaberin/des Inhabers]<br>Handelsregister-Nr. / UID: [CHE-XXX.XXX.XXX] (falls vorhanden)</p>

        <h2>Haftungsausschluss</h2>
        <p>Alle Inhalte dieser Website wurden mit Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte wird jedoch keine Gewähr übernommen. [Platzhalter — durch Rechtsberatung prüfen lassen.]</p>

        <h2>Urheberrecht</h2>
        <p>Die auf dieser Website veröffentlichten Inhalte, Bilder und Produktfotos sind urheberrechtlich geschützt. Eine Verwendung ohne vorherige schriftliche Zustimmung ist nicht gestattet.</p>

        <h2>Streitbeilegung</h2>
        <p>[Platzhalter — Hinweis zu Schlichtungsverfahren, sofern anwendbar.]</p>
      </div>
    </section>
    """
    return page(title, desc, "/impressum/", None, body, robots="noindex, follow")


def build_datenschutz():
    title = f"Datenschutzerklärung | {BRAND}"
    desc = f"Datenschutzerklärung von {BRAND} — Informationen zur Verarbeitung personenbezogener Daten gemäss revDSG."
    body = f"""
    <section class="section">
      <div class="container legal">
        <h1>Datenschutzerklärung</h1>
        <p>Diese Datenschutzerklärung informiert über Art, Umfang und Zweck der Bearbeitung von Personendaten auf dieser Website gemäss dem Schweizer Bundesgesetz über den Datenschutz (DSG).</p>

        <h2>Verantwortliche Stelle</h2>
        <p>{BRAND}<br>{ADDRESS_STREET}<br>{ADDRESS_CITY}<br>E-Mail: {EMAIL}</p>

        <h2>Kontaktformular</h2>
        <p>Wenn Sie uns über das Kontakt- oder Grosshandelsformular Anfragen zukommen lassen, werden Ihre Angaben zwecks Bearbeitung der Anfrage gespeichert. [Platzhalter — Formularverarbeitung/Versanddienst benennen, sobald technisch umgesetzt.]</p>

        <h2>Cookies</h2>
        <p>[Platzhalter — Angaben zu eingesetzten Cookies bzw. Bestätigung, dass aktuell keine Tracking-Cookies gesetzt werden.]</p>

        <h2>Google Maps</h2>
        <p>Auf der Kontaktseite ist eine Karte von Google Maps eingebunden. Beim Aufruf der Seite können Daten an Google LLC übertragen werden. [Platzhalter — auf Datenschutzerklärung von Google verweisen.]</p>

        <h2>Ihre Rechte</h2>
        <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung sowie Einschränkung der Bearbeitung Ihrer Personendaten. Anfragen richten Sie an {EMAIL}.</p>
      </div>
    </section>
    """
    return page(title, desc, "/datenschutz/", None, body, robots="noindex, follow")
