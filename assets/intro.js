/* Opening animation. Inlined straight after the loader markup so it starts the moment
   the page arrives, without waiting for fonts or the animation libraries.
   The house outline draws itself, two leaves grow out of the roof, the real logo settles in,
   then a breeze of leaves blows across as the screen fades away to the home page. */
(function () {
  const html = document.documentElement, loader = document.getElementById('loader');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, touch = !matchMedia('(pointer: fine)').matches;
  const rand = (a, b) => a + Math.random() * (b - a);
  const signal = n => { window['__intro_' + n] = 1; dispatchEvent(new Event('intro:' + n)); };
  function finishIntro() { if (loader) loader.remove(); html.classList.remove('intro', 'intro-out'); signal('done'); }
  try { sessionStorage.setItem('eco_intro', '1'); } catch (e) {}
  if (!loader || !html.classList.contains('intro') || reduce || !loader.animate) { finishIntro(); return; }

  // 1. the house outline draws itself
  [...loader.querySelectorAll('.ln')].forEach((p, i) => {
    const L = p.getTotalLength();
    p.style.strokeDasharray = L; p.style.strokeDashoffset = L;
    p.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 650, delay: 60 + i * 100, easing: 'cubic-bezier(.6,0,.2,1)', fill: 'forwards' });
  });
  // 2. leaves grow out of the roof
  [...loader.querySelectorAll('.lf')].forEach((l, i) => l.animate(
    [{ transform: 'scale(0) rotate(-30deg)', opacity: 0 }, { transform: 'scale(1.1) rotate(4deg)', opacity: 1, offset: .7 }, { transform: 'none', opacity: 1 }],
    { duration: 600, delay: 560 + i * 130, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'forwards' }));
  // 3. the drawing becomes the real logo and the name rises in
  setTimeout(() => loader.classList.add('lit'), 1050);
  // 4. a breeze of leaves carries the screen away
  setTimeout(() => {
    html.classList.add('intro-out'); signal('open');
    const W = innerWidth, H = innerHeight, n = touch ? 9 : 16;
    for (let k = 0; k < n; k++) {
      const lf = document.createElement('i'); lf.className = 'blowleaf' + (k % 3 ? '' : ' b');
      const y0 = rand(H * .1, H * .9), s = rand(.7, 1.4);
      lf.style.top = y0 + 'px'; document.body.appendChild(lf);
      lf.animate([
        { transform: `translate(-60px,0) rotate(0deg) scale(${s})`, opacity: 0 },
        { opacity: 1, offset: .12 },
        { transform: `translate(${W * .5}px,${rand(-90, 40)}px) rotate(${rand(160, 300)}deg) scale(${s})`, offset: .55 },
        { transform: `translate(${W + 80}px,${rand(-160, 20)}px) rotate(${rand(380, 620)}deg) scale(${s})`, opacity: 0 }
      ], { duration: rand(1100, 1600), delay: k * 45, easing: 'cubic-bezier(.35,.1,.5,1)', fill: 'forwards' }).onfinish = () => lf.remove();
    }
    setTimeout(finishIntro, 850);
  }, 2000);
})();
