# Ofx Parser REST API

REST API developed using Django

# API Documentation

## Transactions

Transactions are all the account movements present inside the .ofx report data.

### `/api/transactions`

#### Request

<table>
<thead>
<tr><th colspan=2>Data</th></tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td><code>https://jpricardo.pythonanywhere.com/api/transactions/</code></td>
</tr>

<tr>
<td>Methods</td>
<td><code>POST</code></td>
</tr>

<tr>
<td>Accept</td>
<td><code>application/json</code></td>
</tr>

<tr>
<td>Authentication Required</td>
<td><code>TRUE</code></td>
</tr>
</tbody>
</table>

#### Payload

<table>
<thead>
<tr><th colspan=2>Available Formats</th></tr>
</thead>
<tbody>

<tr>
<td>csv</td>
<td><code>.csv</code></td>
</tr>

</tbody>
</table>

#### Sample Request

```
{
	...,

	"payload": {
		"filename": "example.ofx"
		"base64content": "..."
		"format": "csv"
	},
}
```

#### Sample Response

```
{
	...,

	"data": {
		"filename": "example_output.csv"
		"base64content": "..."
	}
}
```
