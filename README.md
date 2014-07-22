# Coming Soon

# py-email-obfuscate

## An empirically-based, email obfuscation library for Python.

This is a library based on the work of
[Silvan Mühlemann](http://techblog.tilllate.com/2008/07/20/ten-methods-to-obfuscate-e-mail-addresses-compared/)
(potentially NSFW), who created a honey-pot to test a variety of anti-spam
obfuscation techniques. This library implements two of three top solutions that
received no spam.

For browsers with javascript enabled, the mailto anchor is
[rot13](http://en.wikipedia.org/wiki/ROT13) encoded and decoded on page load.
For browsers with javascript disabled, there is a fallback to a noscript tag
that separates the email address with spans that have display:none style, so
that browser only displays the email address.

Example:

    from email_obfuscate import obfuscate

    obfuscate('example@exaple.com', text='My Email Address', noscript_preface='My Email Address: ')


returns

    <script type="text/javascript">document.write("<n uers=\"znvygb:rknzcyr@rkncyr.pbz\" ery=\"absbyybj\">Zl Rznvy Nqqerff</n>".replace(/[a-zA-Z]/g,function(e){return String.fromCharCode((e<="Z"?90:122)>=(e=e.charCodeAt(0)+13)?e:e-26)}));</script><noscript>My Email Address: <span class="obfuscated-email-noscript"><strong><u>exampl<span style="display:none;">null</span>e@exap<span style="display:none;">null</span>le.com</u></strong></span></noscript>

