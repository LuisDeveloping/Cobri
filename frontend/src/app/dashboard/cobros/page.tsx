"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Search,
  Plus,
  MoreHorizontal,
  Filter,
  Calendar,
  Clock,
  CheckCircle,
  AlertTriangle,
  Receipt,
  CreditCard,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
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
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

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
const charges = [
  {
    id: "COB-001",
    clientName: "Maria Garcia",
    concept: "Servicio de maquillaje",
    amount: 35000,
    paid: 35000,
    status: "paid",
    dueDate: "2024-01-15",
    createdAt: "2024-01-10",
  },
  {
    id: "COB-002",
    clientName: "Carlos Rodriguez",
    concept: "Corte de cabello + barba",
    amount: 15000,
    paid: 0,
    status: "pending",
    dueDate: "2024-01-20",
    createdAt: "2024-01-12",
  },
  {
    id: "COB-003",
    clientName: "Ana Martinez",
    concept: "Tratamiento capilar",
    amount: 45000,
    paid: 45000,
    status: "paid",
    dueDate: "2024-01-14",
    createdAt: "2024-01-08",
  },
  {
    id: "COB-004",
    clientName: "Luis Fernandez",
    concept: "Servicio a domicilio",
    amount: 85000,
    paid: 35000,
    status: "partial",
    dueDate: "2024-01-18",
    createdAt: "2024-01-05",
  },
  {
    id: "COB-005",
    clientName: "Patricia Lopez",
    concept: "Paquete mensual",
    amount: 120000,
    paid: 0,
    status: "overdue",
    dueDate: "2024-01-05",
    createdAt: "2024-01-01",
  },
  {
    id: "COB-006",
    clientName: "Roberto Sanchez",
    concept: "Mantenimiento de color",
    amount: 55000,
    paid: 0,
    status: "overdue",
    dueDate: "2024-01-02",
    createdAt: "2023-12-28",
  },
  {
    id: "COB-007",
    clientName: "Sofia Vargas",
    concept: "Corte y peinado",
    amount: 25000,
    paid: 25000,
    status: "paid",
    dueDate: "2024-01-16",
    createdAt: "2024-01-14",
  },
  {
    id: "COB-008",
    clientName: "Miguel Torres",
    concept: "Servicio express",
    amount: 18000,
    paid: 10000,
    status: "partial",
    dueDate: "2024-01-19",
    createdAt: "2024-01-15",
  },
]

function formatCurrency(amount: number) {
  return new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
    minimumFractionDigits: 0,
  }).format(amount)
}

function formatDate(dateString: string) {
  return new Date(dateString).toLocaleDateString("es-CR", {
    day: "numeric",
    month: "short",
  })
}

function getStatusConfig(status: string) {
  switch (status) {
    case "paid":
      return {
        label: "Pagado",
        badge: "bg-success/20 text-success hover:bg-success/30",
        icon: CheckCircle,
      }
    case "pending":
      return {
        label: "Pendiente",
        badge: "bg-warning/20 text-warning hover:bg-warning/30",
        icon: Clock,
      }
    case "partial":
      return {
        label: "Parcial",
        badge: "bg-primary/20 text-primary hover:bg-primary/30",
        icon: Receipt,
      }
    case "overdue":
      return {
        label: "Vencido",
        badge: "bg-destructive/20 text-destructive hover:bg-destructive/30",
        icon: AlertTriangle,
      }
    default:
      return {
        label: "Desconocido",
        badge: "bg-muted text-muted-foreground",
        icon: Receipt,
      }
  }
}

export default function CobrosPage() {
  const [searchQuery, setSearchQuery] = useState("")
  const [activeTab, setActiveTab] = useState("all")
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const filteredCharges = charges.filter((charge) => {
    const matchesSearch =
      charge.clientName.toLowerCase().includes(searchQuery.toLowerCase()) ||
      charge.concept.toLowerCase().includes(searchQuery.toLowerCase()) ||
      charge.id.toLowerCase().includes(searchQuery.toLowerCase())

    const matchesTab = activeTab === "all" || charge.status === activeTab

    return matchesSearch && matchesTab
  })

  const stats = {
    total: charges.reduce((sum, c) => sum + c.amount, 0),
    paid: charges.filter((c) => c.status === "paid").reduce((sum, c) => sum + c.amount, 0),
    pending: charges.filter((c) => c.status === "pending" || c.status === "partial").reduce((sum, c) => sum + (c.amount - c.paid), 0),
    overdue: charges.filter((c) => c.status === "overdue").reduce((sum, c) => sum + c.amount, 0),
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
            Cobros
          </h1>
          <p className="text-muted-foreground">
            Gestiona todos tus cobros y su estado de pago
          </p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button className="gap-2">
              <Plus className="size-4" />
              Nuevo Cobro
            </Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-[425px]">
            <DialogHeader>
              <DialogTitle>Crear Cobro</DialogTitle>
              <DialogDescription>
                Registra un nuevo cobro para un cliente.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="client">Cliente</Label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="Seleccionar cliente" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="maria">Maria Garcia</SelectItem>
                    <SelectItem value="carlos">Carlos Rodriguez</SelectItem>
                    <SelectItem value="ana">Ana Martinez</SelectItem>
                    <SelectItem value="luis">Luis Fernandez</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="grid gap-2">
                <Label htmlFor="concept">Concepto</Label>
                <Input id="concept" placeholder="Ej: Servicio de maquillaje" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="amount">Monto (CRC)</Label>
                <Input id="amount" type="number" placeholder="0" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="dueDate">Fecha de vencimiento</Label>
                <Input id="dueDate" type="date" />
              </div>
            </div>
            <DialogFooter>
              <Button variant="outline" onClick={() => setIsDialogOpen(false)}>
                Cancelar
              </Button>
              <Button onClick={() => setIsDialogOpen(false)}>
                Crear Cobro
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </motion.div>

      {/* Stats Cards */}
      <motion.div variants={item} className="grid gap-4 md:grid-cols-4">
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Total Cobros
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">
              {formatCurrency(stats.total)}
            </div>
            <p className="text-xs text-muted-foreground mt-1">
              {charges.length} cobros registrados
            </p>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Cobrado
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-success">
              {formatCurrency(stats.paid)}
            </div>
            <p className="text-xs text-muted-foreground mt-1">
              {charges.filter((c) => c.status === "paid").length} cobros pagados
            </p>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Pendiente
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-warning">
              {formatCurrency(stats.pending)}
            </div>
            <p className="text-xs text-muted-foreground mt-1">
              Por cobrar
            </p>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Vencido
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-destructive">
              {formatCurrency(stats.overdue)}
            </div>
            <p className="text-xs text-muted-foreground mt-1">
              {charges.filter((c) => c.status === "overdue").length} cobros vencidos
            </p>
          </CardContent>
        </Card>
      </motion.div>

      {/* Tabs and Filters */}
      <motion.div variants={item}>
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <TabsList className="bg-secondary">
              <TabsTrigger value="all" className="data-[state=active]:bg-background">
                Todos
              </TabsTrigger>
              <TabsTrigger value="pending" className="data-[state=active]:bg-background">
                Pendientes
              </TabsTrigger>
              <TabsTrigger value="partial" className="data-[state=active]:bg-background">
                Parciales
              </TabsTrigger>
              <TabsTrigger value="paid" className="data-[state=active]:bg-background">
                Pagados
              </TabsTrigger>
              <TabsTrigger value="overdue" className="data-[state=active]:bg-background">
                Vencidos
              </TabsTrigger>
            </TabsList>

            <div className="relative max-w-sm">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-muted-foreground" />
              <Input
                placeholder="Buscar cobros..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-9"
              />
            </div>
          </div>

          {/* Table */}
          <div className="mt-4">
            <Card className="bg-card border-border">
              <CardContent className="p-0">
                <Table>
                  <TableHeader>
                    <TableRow className="border-border hover:bg-transparent">
                      <TableHead className="text-muted-foreground">ID</TableHead>
                      <TableHead className="text-muted-foreground">Cliente</TableHead>
                      <TableHead className="text-muted-foreground">Concepto</TableHead>
                      <TableHead className="text-muted-foreground">Monto</TableHead>
                      <TableHead className="text-muted-foreground">Pagado</TableHead>
                      <TableHead className="text-muted-foreground">Pendiente</TableHead>
                      <TableHead className="text-muted-foreground">Estado</TableHead>
                      <TableHead className="text-muted-foreground">Vence</TableHead>
                      <TableHead className="text-muted-foreground w-[50px]"></TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {filteredCharges.map((charge) => {
                      const statusConfig = getStatusConfig(charge.status)
                      const StatusIcon = statusConfig.icon
                      const remaining = charge.amount - charge.paid

                      return (
                        <TableRow
                          key={charge.id}
                          className="border-border hover:bg-secondary/50"
                        >
                          <TableCell className="font-mono text-sm text-muted-foreground">
                            {charge.id}
                          </TableCell>
                          <TableCell>
                            <div className="flex items-center gap-3">
                              <Avatar className="h-8 w-8">
                                <AvatarFallback className="bg-primary/20 text-primary text-xs">
                                  {charge.clientName
                                    .split(" ")
                                    .map((n) => n[0])
                                    .join("")}
                                </AvatarFallback>
                              </Avatar>
                              <span className="font-medium text-foreground">
                                {charge.clientName}
                              </span>
                            </div>
                          </TableCell>
                          <TableCell className="text-muted-foreground max-w-[200px] truncate">
                            {charge.concept}
                          </TableCell>
                          <TableCell className="font-medium text-foreground">
                            {formatCurrency(charge.amount)}
                          </TableCell>
                          <TableCell className="text-success">
                            {charge.paid > 0 ? formatCurrency(charge.paid) : "-"}
                          </TableCell>
                          <TableCell className={remaining > 0 ? "text-warning" : "text-muted-foreground"}>
                            {remaining > 0 ? formatCurrency(remaining) : "-"}
                          </TableCell>
                          <TableCell>
                            <Badge className={statusConfig.badge}>
                              <StatusIcon className="size-3 mr-1" />
                              {statusConfig.label}
                            </Badge>
                          </TableCell>
                          <TableCell className="text-muted-foreground">
                            <div className="flex items-center gap-1">
                              <Calendar className="size-3" />
                              {formatDate(charge.dueDate)}
                            </div>
                          </TableCell>
                          <TableCell>
                            <DropdownMenu>
                              <DropdownMenuTrigger asChild>
                                <Button variant="ghost" size="icon" className="size-8">
                                  <MoreHorizontal className="size-4" />
                                </Button>
                              </DropdownMenuTrigger>
                              <DropdownMenuContent align="end">
                                {charge.status !== "paid" && (
                                  <>
                                    <DropdownMenuItem>
                                      <CreditCard className="mr-2 size-4" />
                                      Registrar pago
                                    </DropdownMenuItem>
                                    <DropdownMenuItem>
                                      <Receipt className="mr-2 size-4" />
                                      Registrar abono
                                    </DropdownMenuItem>
                                    <DropdownMenuSeparator />
                                  </>
                                )}
                                <DropdownMenuItem>Ver detalle</DropdownMenuItem>
                                <DropdownMenuItem>Editar</DropdownMenuItem>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem className="text-destructive">
                                  Eliminar
                                </DropdownMenuItem>
                              </DropdownMenuContent>
                            </DropdownMenu>
                          </TableCell>
                        </TableRow>
                      )
                    })}
                  </TableBody>
                </Table>
              </CardContent>
            </Card>
          </div>
        </Tabs>
      </motion.div>

      {/* Results info */}
      <motion.div variants={item} className="flex items-center justify-between text-sm text-muted-foreground">
        <span>
          Mostrando {filteredCharges.length} de {charges.length} cobros
        </span>
      </motion.div>
    </motion.div>
  )
}
