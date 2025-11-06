import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const insertLog = mutation({
  args: { message: v.string() },
  handler: async (ctx, args) => {
    await ctx.db.insert("logs", args);
  }
});


export const insertBikroyPost = mutation({
  args: {
    model: v.string(),
    battery_backup: v.optional(v.float64()),
    processor_name: v.string(),
    processor_generation: v.optional(v.string()),
    processor_wattage: v.optional(v.float64()),
    ram_size: v.float64(),
    ram_generation: v.optional(v.string()),
    gpu: v.optional(v.string()),
    gpu_vram: v.optional(v.float64()),
    ssd_size: v.float64(),
    hdd_size: v.float64(),
    display_size: v.float64(),
    display_resolution: v.optional(v.string()),
    time_used_in_moths: v.float64(),
    price: v.number(),
    url: v.string(),
    image_urls: v.array(v.string()),
    posted_at: v.string()
  },
  handler: async (ctx, args) => {
    await ctx.db.insert("bikroyPosts", args);
  }
})

export const getData = query({
  args: {
    model: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { model } = args;
    if (model) {
      return await ctx.db
        .query("bikroyPosts")
        .filter((q) => q.eq(q.field("model"), model))
        .order("desc")
        .collect();
    }
    return await ctx.db.query("bikroyPosts").order("desc").collect();
  }
})