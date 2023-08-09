export function request(_) { 
  return {}; 
}

export function response(ctx) {
  if (!ctx.stash.parent) return
  return { ...ctx.stash.parent, children: ctx.stash.children }; 
}