// Comportements communs des TP. Chargé par <script src="../../assets/tp.js"></script>.

// Liens a[download] : le fichier est récupéré tel quel (octets identiques, donc
// métadonnées intactes) puis enregistré. En cas d'échec, le lien s'ouvre normalement.
document.querySelectorAll("a[download]").forEach(function (lien) {
  lien.addEventListener("click", function (e) {
    if (!window.fetch || !window.URL || location.protocol === "file:") { return; }
    e.preventDefault();
    fetch(lien.href)
      .then(function (r) { if (!r.ok) { throw new Error("http"); } return r.blob(); })
      .then(function (blob) {
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = lien.getAttribute("download");
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      })
      .catch(function () { window.location.href = lien.href; });
  });
});

// Plan : met en évidence l'étape en cours de lecture.
(function () {
  var liens = document.querySelectorAll('nav.plan a[href^="#"]');
  if (!liens.length) { return; }
  var etapes = [];
  liens.forEach(function (lien) {
    var section = document.getElementById(lien.getAttribute("href").slice(1));
    if (section) { etapes.push({ lien: lien, section: section }); }
  });
  var attente = false;
  function actualiser() {
    attente = false;
    var courant = null;
    etapes.forEach(function (e) {
      if (e.section.getBoundingClientRect().top <= window.innerHeight * 0.3) { courant = e; }
    });
    etapes.forEach(function (e) {
      var actif = e === courant;
      e.lien.classList.toggle("actif", actif);
      if (actif) { e.lien.setAttribute("aria-current", "true"); } else { e.lien.removeAttribute("aria-current"); }
    });
  }
  window.addEventListener("scroll", function () {
    if (!attente) { attente = true; window.requestAnimationFrame(actualiser); }
  }, { passive: true });
  actualiser();
})();
