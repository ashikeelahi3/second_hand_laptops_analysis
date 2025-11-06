import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  logs: defineTable({
    message: v.string()
  }),
  bikroyPosts: defineTable({
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
  })
});
