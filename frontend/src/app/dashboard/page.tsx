"use client"

import { motion } from "framer-motion"
import {
  DollarSign,
  Users,
  Receipt,
  AlertCircle,
  TrendingUp,
  TrendingDown,
  ArrowUpRight,
  Plus,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts"

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

// Mock data
const revenueData = [
  { name: "Ene", total: 450000 },
  { name: "Feb", total: 380000 },
  { name: "Mar", total: 520000 },
  { name: "Abr", total: 490000 },
  { name: "May", total: 610000 },
  { name: "Jun", total: 580000 },
]

const weeklyData = [
  { day: "Lun", cobrado: 85000, pendiente: 25000 },
  { day: "Mar", cobrado: 120000, pendiente: 35000 },
  { day: "Mie", cobrado: 95000, pendiente: 20000 },
  { day: "Jue", cobrado: 140000, pendiente: 45000 },
  { day: "Vie", cobrado: 180000, pendiente: 30000 },
  { day: "Sab", cobrado: 220000, pendiente: 15000 },
  { day: "Dom", cobrado: 60000, pendiente: 10000 },
]

const recentActivity = [
  {
    id: 1,
    type: "payment",
    client: "Maria Garcia",
    amount: 25000,
    time: "Hace 5 min",
    status: "completed",
  },
  {
    id: 2,
    type: "charge",
    client: "Carlos Rodriguez",
    amount: 45000,
    time: "Hace 15 min",
    status: "pending",
  },
  {
    id: 3,
    type: "payment",
    client: "Ana Martinez",
    amount: 15000,
    time: "Hace 30 min",
    status: "completed",
  },
  {
    id: 4,
    type: "partial",
    client: "Luis Fernandez",
    amount: 10000,
    time: "Hace 1 hora",
    status: "partial",
  },
]

const pendingClients = [
  { name: "Roberto Sanchez", debt: 125000, days: 15 },
  { name: "Patricia Lopez", debt: 85000, days: 8 },
  { name: "Miguel Torres", debt: 45000, days: 3 },
]

function formatCurrency(amount: number) {
  return new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
    minimumFractionDigits: 0,
  }).format(amount)
}

export default function DashboardPage() {
  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="space-y-6"
    >
      {/* Header */}
      <motion.div variants={item} className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">
            Dashboard
          </h1>
          <p className="text-muted-foreground">
            Resumen de tu actividad de cobros y pagos
          </p>
        </div>
        <Button className="gap-2">
          <Plus className="size-4" />
          Nuevo Cobro
        </Button>
      </motion.div>

      {/* Stats Cards */}
      <motion.div
        variants={item}
        className="grid gap-4 md:grid-cols-2 lg:grid-cols-4"
      >
        <Card className="bg-card border-border">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Cobrado Hoy
            </CardTitle>
            <div className="p-2 rounded-lg bg-success/10">
              <DollarSign className="size-4 text-success" />
            </div>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">
              {formatCurrency(285000)}
            </div>
            <div className="flex items-center gap-1 text-xs text-success mt-1">
              <TrendingUp className="size-3" />
              <span>+12% vs ayer</span>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Pendiente Total
            </CardTitle>
            <div className="p-2 rounded-lg bg-warning/10">
              <Receipt className="size-4 text-warning" />
            </div>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">
              {formatCurrency(892500)}
            </div>
            <div className="flex items-center gap-1 text-xs text-warning mt-1">
              <AlertCircle className="size-3" />
              <span>23 cobros activos</span>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Clientes Activos
            </CardTitle>
            <div className="p-2 rounded-lg bg-primary/10">
              <Users className="size-4 text-primary" />
            </div>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">147</div>
            <div className="flex items-center gap-1 text-xs text-primary mt-1">
              <TrendingUp className="size-3" />
              <span>+5 esta semana</span>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Cobros Vencidos
            </CardTitle>
            <div className="p-2 rounded-lg bg-destructive/10">
              <AlertCircle className="size-4 text-destructive" />
            </div>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">8</div>
            <div className="flex items-center gap-1 text-xs text-destructive mt-1">
              <TrendingDown className="size-3" />
              <span>{formatCurrency(255000)} en riesgo</span>
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Charts */}
      <motion.div variants={item} className="grid gap-4 lg:grid-cols-7">
        <Card className="lg:col-span-4 bg-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Ingresos Mensuales</CardTitle>
            <CardDescription>
              Tendencia de cobros realizados en los ultimos 6 meses
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={revenueData}>
                  <defs>
                    <linearGradient id="colorTotal" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="hsl(var(--primary))" stopOpacity={0.3} />
                      <stop offset="95%" stopColor="hsl(var(--primary))" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                  <XAxis
                    dataKey="name"
                    stroke="hsl(var(--muted-foreground))"
                    fontSize={12}
                    tickLine={false}
                    axisLine={false}
                  />
                  <YAxis
                    stroke="hsl(var(--muted-foreground))"
                    fontSize={12}
                    tickLine={false}
                    axisLine={false}
                    tickFormatter={(value) => `${value / 1000}k`}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: "hsl(var(--card))",
                      border: "1px solid hsl(var(--border))",
                      borderRadius: "8px",
                    }}
                    labelStyle={{ color: "hsl(var(--foreground))" }}
                    formatter={(value: number) => [formatCurrency(value), "Total"]}
                  />
                  <Area
                    type="monotone"
                    dataKey="total"
                    stroke="hsl(var(--primary))"
                    strokeWidth={2}
                    fillOpacity={1}
                    fill="url(#colorTotal)"
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        <Card className="lg:col-span-3 bg-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Esta Semana</CardTitle>
            <CardDescription>Cobrado vs Pendiente por dia</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={weeklyData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                  <XAxis
                    dataKey="day"
                    stroke="hsl(var(--muted-foreground))"
                    fontSize={12}
                    tickLine={false}
                    axisLine={false}
                  />
                  <YAxis
                    stroke="hsl(var(--muted-foreground))"
                    fontSize={12}
                    tickLine={false}
                    axisLine={false}
                    tickFormatter={(value) => `${value / 1000}k`}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: "hsl(var(--card))",
                      border: "1px solid hsl(var(--border))",
                      borderRadius: "8px",
                    }}
                    labelStyle={{ color: "hsl(var(--foreground))" }}
                    formatter={(value: number) => formatCurrency(value)}
                  />
                  <Bar
                    dataKey="cobrado"
                    fill="hsl(var(--success))"
                    radius={[4, 4, 0, 0]}
                    name="Cobrado"
                  />
                  <Bar
                    dataKey="pendiente"
                    fill="hsl(var(--warning))"
                    radius={[4, 4, 0, 0]}
                    name="Pendiente"
                  />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Bottom Section */}
      <motion.div variants={item} className="grid gap-4 lg:grid-cols-2">
        {/* Recent Activity */}
        <Card className="bg-card border-border">
          <CardHeader>
            <div className="flex items-center justify-between">
              <div>
                <CardTitle className="text-foreground">Actividad Reciente</CardTitle>
                <CardDescription>Ultimos movimientos de hoy</CardDescription>
              </div>
              <Button variant="ghost" size="sm" className="gap-1 text-primary">
                Ver todo
                <ArrowUpRight className="size-3" />
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {recentActivity.map((activity) => (
                <div
                  key={activity.id}
                  className="flex items-center justify-between p-3 rounded-lg bg-secondary/50 hover:bg-secondary/80 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <Avatar className="h-9 w-9">
                      <AvatarFallback className="bg-primary/20 text-primary text-sm">
                        {activity.client
                          .split(" ")
                          .map((n) => n[0])
                          .join("")}
                      </AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium text-foreground">
                        {activity.client}
                      </p>
                      <p className="text-xs text-muted-foreground">{activity.time}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Badge
                      variant={
                        activity.status === "completed"
                          ? "default"
                          : activity.status === "partial"
                          ? "secondary"
                          : "outline"
                      }
                      className={
                        activity.status === "completed"
                          ? "bg-success/20 text-success hover:bg-success/30"
                          : activity.status === "partial"
                          ? "bg-warning/20 text-warning hover:bg-warning/30"
                          : "border-border"
                      }
                    >
                      {activity.status === "completed"
                        ? "Pagado"
                        : activity.status === "partial"
                        ? "Abono"
                        : "Pendiente"}
                    </Badge>
                    <span
                      className={`text-sm font-medium ${
                        activity.status === "completed"
                          ? "text-success"
                          : activity.status === "partial"
                          ? "text-warning"
                          : "text-foreground"
                      }`}
                    >
                      {activity.status === "pending" ? "-" : "+"}{formatCurrency(activity.amount)}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Pending Clients */}
        <Card className="bg-card border-border">
          <CardHeader>
            <div className="flex items-center justify-between">
              <div>
                <CardTitle className="text-foreground">Clientes con Deuda</CardTitle>
                <CardDescription>Clientes que requieren seguimiento</CardDescription>
              </div>
              <Button variant="ghost" size="sm" className="gap-1 text-primary">
                Ver todos
                <ArrowUpRight className="size-3" />
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {pendingClients.map((client) => (
                <div
                  key={client.name}
                  className="flex items-center justify-between p-3 rounded-lg bg-secondary/50 hover:bg-secondary/80 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <Avatar className="h-9 w-9">
                      <AvatarFallback className="bg-destructive/20 text-destructive text-sm">
                        {client.name
                          .split(" ")
                          .map((n) => n[0])
                          .join("")}
                      </AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium text-foreground">
                        {client.name}
                      </p>
                      <p className="text-xs text-muted-foreground">
                        {client.days} dias sin pagar
                      </p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-sm font-medium text-destructive">
                      {formatCurrency(client.debt)}
                    </p>
                    <Button
                      variant="ghost"
                      size="sm"
                      className="h-6 px-2 text-xs text-primary"
                    >
                      Enviar recordatorio
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </motion.div>
    </motion.div>
  )
}
