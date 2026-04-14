export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    const path = url.pathname

    // upload user taste
    if (path === "/upload") {
      const user = request.headers.get("x-user")
      const tasteHeader = request.headers.get("x-taste")

      if (!user || !tasteHeader) {
        return Response.json(
          { error: "missing header: x-user or x-taste" },
          { status: 400 }
        )
      }

      const taste = tasteHeader
        .split(",")
        .map(Number)

      await env.TASTE_KV.put(
        `${user}`,
        JSON.stringify(taste)
      )

      return Response.json({
        ok: true,
        user,
        taste
      })
    }

    // find best match
    if (path === "/match") {
      const tasteHeader = request.headers.get("x-taste")

      if (!tasteHeader) {
        return Response.json(
          { error: "missing header: x-taste" },
          { status: 400 }
        )
      }

      const query = tasteHeader.split(",").map(Number)

      // get all keys
      const list = await env.TASTE_KV.list()

      let bestUser = null
      let bestScore = -Infinity

      for (const key of list.keys) {
        const raw = await env.TASTE_KV.get(key.name)
        if (!raw) continue

        const vec = JSON.parse(raw)

        const score = cosine(query, vec)

        if (score > bestScore) {
          bestScore = score
          bestUser = key.name
        }
      }

      return Response.json({
        ok: true,
        match: bestUser,
        score: bestScore
      })
      // {"ok":true,"match":"ray","score":-1.0000000000000002}
    }

    return new Response("Unknown Request", { status: 404 })
  }
}

function cosine(a, b) {
  let dot = 0
  let na = 0
  let nb = 0

  for (let i = 0; i < 6; i++) {
    dot += a[i] * b[i]
    na += a[i] * a[i]
    nb += b[i] * b[i]
  }

  return dot / (Math.sqrt(na) * Math.sqrt(nb))
}