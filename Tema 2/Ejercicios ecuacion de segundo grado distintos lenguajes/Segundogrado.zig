const std = @import("std");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const n = 200;

    const a = try allocator.alloc(f64, n);
    const b = try allocator.alloc(f64, n);
    const c = try allocator.alloc(f64, n);
    const resultados_x1 = try allocator.alloc(f64, n);
    const resultados_x2 = try allocator.alloc(f64, n);
    defer allocator.free(a);
    defer allocator.free(b);
    defer allocator.free(c);
    defer allocator.free(resultados_x1);
    defer allocator.free(resultados_x2);

    @memset(a, 1.0);
    @memset(b, -5.0);
    @memset(c, 6.0);

    var i: usize = 0;
    while (i < n) : (i += 1) {
        const disc = b[i] * b[i] - 4.0 * a[i] * c[i];
        resultados_x1[i] = (-b[i] + std.math.sqrt(disc)) / (2.0 * a[i]);
        resultados_x2[i] = (-b[i] - std.math.sqrt(disc)) / (2.0 * a[i]);
    }

    std.debug.print("Control (Último resultado): x1 = {d}, x2 = {d}\n", .{ resultados_x1[n - 1], resultados_x2[n - 1] });
}