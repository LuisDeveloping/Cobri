"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Search,
  Plus,
  Filter,
  Calendar,
  ArrowDownLeft,
  ArrowUpRight,
  Banknote,
  CreditCard,
  Smartphone,
  Download,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Label } from "@/components/ui/label"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05,
    },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

// Mock data
const payments = [
  {
    id: "PAG-001",
    chargeId: "COB-001",
    clientName: "Maria Garcia",
    amount: 35000,
    method: "sinpe",
    type: "full",
    date: "2024-01-15T10:30:00",
    reference: "SINPE-78234",
  },
  {
    id: "PAG-002",
    chargeId: "COB-003",
    clientName: "Ana Martinez",
    amount: 45000,
    method: "cash",
    type: "full",
    date: "2024-01-14T14:15:00",
    reference: null,
  },
  {
    id: "PAG-003",
    chargeId: "COB-004",
    clientName: "Luis Fernandez",
    amount: 35000,
    method: "sinpe",
    type: "partial",
    date: "2024-01-14T09:45:00",
    reference: "SINPE-78190",
  },
  {
    id: "PAG-004",
    chargeId: "COB-007",
    clientName: "Sofia Vargas",
    amount: 25000,
    method: "transfer",
    type: "full",
    date: "2024-01-14T16:20:00",
    reference: "BCR-445566",
  },
  {
    id: "PAG-005",
    chargeId: "COB-008",
    clientName: "Miguel Torres",
    amount: 10000,
    method: "cash",
    type: "partial",
    date: "2024-01-13T11:00:00",
    reference: null,
  },
  {
    id: "PAG-006",
    chargeId: "COB-009",
    clientName: "Carmen Jimenez",
    amount: 50000,
    method: "sinpe",
    type: "full",
    date: "2024-01-13T15:30:00",
    reference: "SINPE-78156",
  },
  {
    id: "PAG-007",
    chargeId: "COB-010",
    clientName: "Pedro Mora",
    amount: 20000,
    method: "transfer",
    type: "partial",
    date: "2024-01-12T10:00:00",
    reference: "BAC-112233",
  },
  {
    id: "PAG-008",
    chargeId: "COB-011",
    clientName: "Laura Castro",
    amount: 65000,
    method: "sinpe",
    type: "full",
    date: "2024-01-12T13:45:00",
    reference: "SINPE-78098",
  },
]

function formatCurrency(amount: number) {
  return new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
    minimumFractionDigits: 0,
  }).format(amount)
}

function formatDateTime(dateString: string) {
  const date = new Date(dateString)
  return {
    date: date.toLocaleDateString("es-CR", {
      day: "numeric",
      month: "short",
    }),
    time: date.toLocaleTimeString("es-CR", {
      hour: "2-digit",
      minute: "2-digit",
    }),
  }
}

function getMethodConfig(method: string) {
  switch (method) {
    case "sinpe":
      return {
        label: "SINPE Movil",
        icon: Smartphone,
        color: "text-primary",
        bg: "bg-primary/10",
      }
    case "cash":
      return {
        label: "Efectivo",
        icon: Banknote,
        color: "text-success",
        bg: "bg-success/10",
      }
    case "transfer":
      return {
        label: "Transferencia",
        icon: CreditCard,
        color: "text-accent",
        bg: "bg-accent/10",
      }
    default:
      return {
        label: "Otro",
        icon: CreditCard,
        color: "text-muted-foreground",
        bg: "bg-muted",
      }
  }
}

// Group payments by date
function groupPaymentsByDate(payments: typeof payments) {
  const groups: { [key: string]: typeof payments } = {}
  
  payments.forEach((payment) => {
    const date = new Date(payment.date).toLocaleDateString("es-CR", {
      weekday: "long",
      day: "numeric",
      month: "long",
    })
    if (!groups[date]) {
      groups[date] = []
    }
    groups[date].push(payment)
  })
  
  return groups
}

export default function PagosPage() {
  const [searchQuery, setSearchQuery] = useState("")
  const [methodFilter, setMethodFilter] = useState("all")
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const filteredPayments = payments.filter((payment) => {
    const matchesSearch =
      payment.clientName.toLowerCase().includes(searchQuery.toLowerCase()) ||
      payment.id.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (payment.reference && payment.reference.toLowerCase().includes(searchQuery.toLowerCase()))

    const matchesMethod = methodFilter === "all" || payment.method === methodFilter

    return matchesSearch && matchesMethod
  })

  const groupedPayments = groupPaymentsByDate(filteredPayments)

  const stats = {
    today: payments
      .filter((p) => new Date(p.date).toDateString() === new Date().toDateString())
      .reduce((sum, p) => sum + p.amount, 0),
    week: payments.reduce((sum, p) => sum + p.amount, 0),
    sinpe: payments.filter((p) => p.method === "sinpe").reduce((sum, p) => sum + p.amount, 0),
    cash: payments.filter((p) => p.method === "cash").reduce((sum, p) => sum + p.amount, 0),
  }

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
            Pagos
          </h1>
          <p className="text-muted-foreground">
            Historial de pagos y abonos recibidos
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline" className="gap-2">
            <Download className="size-4" />
            Exportar
          </Button>
          <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
            <DialogTrigger asChild>
              <Button className="gap-2">
                <Plus className="size-4" />
                Registrar Pago
              </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-[425px]">
              <DialogHeader>
                <DialogTitle>Registrar Pago</DialogTitle>
                <DialogDescription>
                  Registra un pago o abono para un cobro existente.
                </DialogDescription>
              </DialogHeader>
              <div className="grid gap-4 py-4">
                <div className="grid gap-2">
                  <Label htmlFor="charge">Cobro</Label>
                  <Select>
                    <SelectTrigger>
                      <SelectValue placeholder="Seleccionar cobro" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="cob-002">COB-002 - Carlos Rodriguez (15,000)</SelectItem>
                      <SelectItem value="cob-004">COB-004 - Luis Fernandez (50,000 pendiente)</SelectItem>
                      <SelectItem value="cob-005">COB-005 - Patricia Lopez (120,000)</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="grid gap-2">
                  <Label htmlFor="amount">Monto (CRC)</Label>
                  <Input id="amount" type="number" placeholder="0" />
                </div>
                <div className="grid gap-2">
                  <Label htmlFor="method">Metodo de pago</Label>
                  <Select>
                    <SelectTrigger>
                      <SelectValue placeholder="Seleccionar metodo" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="sinpe">SINPE Movil</SelectItem>
                      <SelectItem value="cash">Efectivo</SelectItem>
                      <SelectItem value="transfer">Transferencia</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="grid gap-2">
                  <Label htmlFor="reference">Referencia (opcional)</Label>
                  <Input id="reference" placeholder="Ej: SINPE-12345" />
                </div>
              </div>
              <DialogFooter>
                <Button variant="outline" onClick={() => setIsDialogOpen(false)}>
                  Cancelar
                </Button>
                <Button onClick={() => setIsDialogOpen(false)}>
                  Registrar Pago
                </Button>
              </DialogFooter>
            </DialogContent>
          </Dialog>
        </div>
      </motion.div>

      {/* Stats Cards */}
      <motion.div variants={item} className="grid gap-4 md:grid-cols-4">
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Recibido Hoy
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-success">
              {formatCurrency(stats.today)}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Esta Semana
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">
              {formatCurrency(stats.week)}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Por SINPE
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-primary">
              {formatCurrency(stats.sinpe)}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              En Efectivo
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-success">
              {formatCurrency(stats.cash)}
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Filters */}
      <motion.div variants={item} className="flex flex-col gap-4 md:flex-row md:items-center">
        <div className="relative flex-1 max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-muted-foreground" />
          <Input
            placeholder="Buscar por cliente, ID o referencia..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-9"
          />
        </div>
        <Select value={methodFilter} onValueChange={setMethodFilter}>
          <SelectTrigger className="w-[180px]">
            <Filter className="size-4 mr-2" />
            <SelectValue placeholder="Metodo" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Todos</SelectItem>
            <SelectItem value="sinpe">SINPE Movil</SelectItem>
            <SelectItem value="cash">Efectivo</SelectItem>
            <SelectItem value="transfer">Transferencia</SelectItem>
          </SelectContent>
        </Select>
      </motion.div>

      {/* Payment Timeline */}
      <motion.div variants={item} className="space-y-6">
        {Object.entries(groupedPayments).map(([date, dayPayments]) => (
          <div key={date}>
            <h3 className="text-sm font-medium text-muted-foreground mb-3 capitalize">
              {date}
            </h3>
            <Card className="bg-card border-border">
              <CardContent className="p-0">
                <div className="divide-y divide-border">
                  {dayPayments.map((payment, index) => {
                    const methodConfig = getMethodConfig(payment.method)
                    const MethodIcon = methodConfig.icon
                    const { time } = formatDateTime(payment.date)

                    return (
                      <motion.div
                        key={payment.id}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: index * 0.05 }}
                        className="flex items-center justify-between p-4 hover:bg-secondary/50 transition-colors"
                      >
                        <div className="flex items-center gap-4">
                          <div className={`p-2 rounded-lg ${methodConfig.bg}`}>
                            <MethodIcon className={`size-5 ${methodConfig.color}`} />
                          </div>
                          <div>
                            <div className="flex items-center gap-2">
                              <span className="font-medium text-foreground">
                                {payment.clientName}
                              </span>
                              <Badge
                                variant="outline"
                                className={payment.type === "full" ? "border-success/50 text-success" : "border-warning/50 text-warning"}
                              >
                                {payment.type === "full" ? "Pago completo" : "Abono"}
                              </Badge>
                            </div>
                            <div className="flex items-center gap-2 text-sm text-muted-foreground">
                              <span className="font-mono">{payment.id}</span>
                              <span>-</span>
                              <span>{methodConfig.label}</span>
                              {payment.reference && (
                                <>
                                  <span>-</span>
                                  <span className="font-mono">{payment.reference}</span>
                                </>
                              )}
                            </div>
                          </div>
                        </div>
                        <div className="text-right">
                          <div className="flex items-center gap-1 text-success font-semibold">
                            <ArrowDownLeft className="size-4" />
                            {formatCurrency(payment.amount)}
                          </div>
                          <div className="text-sm text-muted-foreground">{time}</div>
                        </div>
                      </motion.div>
                    )
                  })}
                </div>
              </CardContent>
            </Card>
          </div>
        ))}
      </motion.div>

      {/* Results info */}
      <motion.div variants={item} className="flex items-center justify-between text-sm text-muted-foreground">
        <span>
          Mostrando {filteredPayments.length} de {payments.length} pagos
        </span>
      </motion.div>
    </motion.div>
  )
}
