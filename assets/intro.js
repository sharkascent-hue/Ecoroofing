/* Opening animation. Inlined straight after the loader markup so it starts the moment
   the page arrives, without waiting for fonts or the animation libraries.
   The logo is on screen straight away, a gust of green leaves blows in and swirls into it,
   then the whole screen slides away to the left to open the home page. */
(function () {
  const html = document.documentElement, loader = document.getElementById('loader');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, touch = !matchMedia('(pointer: fine)').matches;
  const rand = (a, b) => a + Math.random() * (b - a);
  const signal = n => { window['__intro_' + n] = 1; dispatchEvent(new Event('intro:' + n)); };
  function finishIntro() { if (loader) loader.remove(); html.classList.remove('intro', 'intro-out'); signal('done'); }
  try { sessionStorage.setItem('eco_intro', '1'); } catch (e) {}
  if (!loader || !html.classList.contains('intro') || reduce || !loader.animate) { finishIntro(); return; }

  const W = innerWidth, H = innerHeight, mk = loader.querySelector('.mk');
  // leaves land on the leaves at the top of the roof in the logo
  const r = mk.getBoundingClientRect(), tx = r.left + r.width * .52, ty = r.top + r.height * .24;
  const n = touch ? 11 : 16;
  let landed = false;
  for (let k = 0; k < n; k++) {
    const lf = document.createElement('i'); lf.className = 'blowleaf' + (k % 3 === 1 ? ' b' : k % 5 === 0 ? ' c' : '');
    loader.appendChild(lf);
    const sx = W + rand(30, 120), sy = rand(H * .05, H * .95);                    // start off the right edge
    const mx = tx + rand(W * .12, W * .32), my = ty + rand(-H * .22, H * .22);    // swirl past the logo
    const ex = tx + rand(-26, 26), ey = ty + rand(-18, 14);                      // into the roof leaves
    const rot = rand(-200, -420);
    const a = lf.animate([
      { transform: `translate(${sx}px,${sy}px) rotate(0deg) scale(1)`, opacity: 0 },
      { opacity: 1, offset: .1 },
      { transform: `translate(${mx}px,${my}px) rotate(${rot * .6}deg) scale(1)`, offset: .6 },
      { transform: `translate(${ex}px,${ey}px) rotate(${rot}deg) scale(.25)`, opacity: 0 }
    ], { duration: rand(950, 1250), delay: 150 + k * 55, easing: 'cubic-bezier(.45,.05,.4,1)', fill: 'forwards' });
    a.onfinish = () => { lf.remove(); if (!landed) { landed = true; loader.classList.add('got'); } };
  }
  // the whole screen slides off to the left, revealing the home page
  setTimeout(() => {
    html.classList.add('intro-out'); signal('open');
    setTimeout(finishIntro, 900);
  }, 1950 + (n - 11) * 25);
})();
